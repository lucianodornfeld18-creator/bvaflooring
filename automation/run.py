#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BVA Flooring — autonomous blog post generator (2x / week).

Pipeline (one post per run):
  pick next topic (topics.json) -> Claude API writes post JSON -> validate (HARD GATE)
  -> save automation/posts/<slug>.json -> build.py regenerates site
  -> build dist/ -> wrangler pages deploy -> git commit/push -> log

If validation fails twice, NOTHING is published that run (safe by default).

Env:
  ANTHROPIC_API_KEY   (required — same key as Triangle Flooring)
  BVA_BLOG_MODEL      (optional, default claude-sonnet-4-6)
  TODAY=YYYY-MM-DD    (optional; defaults to system date)
Usage:
  py automation/run.py            # full run + deploy
  py automation/run.py --dry      # pick topic only, no API call
  py automation/run.py --no-deploy
"""
import os, re, sys, json, subprocess, datetime, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
POSTS = HERE / "posts"
TOPICS = HERE / "topics.json"
PUBLOG = HERE / "published_log.json"
MODEL = os.environ.get("BVA_BLOG_MODEL", "claude-sonnet-4-6")
MAX_TRIES = 2

# Load automation/.env (KEY=VALUE lines) if present — local secret store (gitignored).
_envf = HERE / ".env"
if _envf.exists():
    for _line in _envf.read_text(encoding="utf-8").splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

sys.path.insert(0, str(ROOT))
import build, content   # reuse site data + renderer

# ── valid internal URLs (links must point to these) ─────────────────────────
def valid_urls():
    u = {"/", "/about/", "/contact/", "/blog/"}
    for s in build.SERVICES:
        u.add(f"/{s['slug']}/")
        for slug, _ in build.AREAS:
            u.add(f"/{slug}/"); u.add(f"/{s['slug']}/{slug}/")
    for p in content.BLOG_POSTS:
        u.add(f"/blog/{p['slug']}/")
    return u

def price_reference():
    lines = []
    for s in build.SERVICES:
        rows = content.SVC_DATA[s["slug"]]["prices"]
        rng = "; ".join(f"{re.sub('&amp;','&',lbl)}: {pr}" for lbl, pr, _ in rows)
        lines.append(f"- {s['name']}: {rng}")
    return "\n".join(lines)

def today():
    return datetime.date.fromisoformat(os.environ.get("TODAY") or datetime.date.today().isoformat())

def published_slugs():
    s = {p["slug"] for p in content.BLOG_POSTS}
    for f in POSTS.glob("*.json"):
        s.add(f.stem)
    if PUBLOG.exists():
        try: s |= {x["slug"] for x in json.load(open(PUBLOG, encoding="utf-8"))}
        except Exception: pass
    return s

def pick_topic():
    topics = json.load(open(TOPICS, encoding="utf-8"))
    done = published_slugs()
    for t in topics:
        if t.get("status") == "published": continue
        if t["slug"] in done: continue
        if (ROOT / "blog" / t["slug"] / "index.html").exists(): continue
        return t, topics
    return None, topics

# ── prompt ──────────────────────────────────────────────────────────────────
SCHEMA = '''{
 "slug": "kebab-case-no-year",
 "title": "<= 65 chars, keyword-first, unique",
 "h1": "question-style headline",
 "dek": "120-158 char meta description / intro",
 "cat": "Cost Guide | Comparison | Buyer's Guide | How-To",
 "emoji": "one relevant emoji",
 "read": "N min",
 "date": "YYYY-MM-DD",
 "mod": "YYYY-MM-DD",
 "body": [["H2 question heading", "<p>...</p><p>...</p>"], ...],
 "faqs": [["Question?", "Answer (plain text or simple <strong>)."], ...],
 "links": [["Anchor label", "/real/internal/url/"], ...]
}'''

def build_prompt(topic, d, correction=None):
    urls = "\n".join("- " + u for u in sorted(valid_urls()))
    system = (
        "You are the autonomous blog writer for BVA Flooring (BVA Services Corp), a licensed, insured "
        "flooring installer in Bradenton & the Tampa Bay Gulf Coast, FL. Phone (941) 807-0339. Founded 2020. "
        "Voice: practical, honest, locally-rooted, no hype.\n\n"
        "Write ONE informational blog post as a SINGLE JSON object matching this schema EXACTLY:\n"
        f"```json\n{SCHEMA}\n```\n\n"
        "HARD RULES:\n"
        "- 1,200-1,800 words across body[].html; >=5 question-style H2 sections; >=4 and <=6 FAQs.\n"
        "- INFORMATIONAL only. Do NOT duplicate a transactional '{service} {city}' landing page; write the "
        "guide/explainer angle.\n"
        "- links: 3-6 items, EVERY url MUST be from the SITE URLS list below (verbatim). Always include the "
        "topic's funnel target. No external links, no invented URLs.\n"
        "- NEVER invent reviews, review counts, star counts, ratings, awards, certifications, license numbers, "
        "named customers, or statistics. You may say 'licensed & insured', '5-star workmanship pledge', "
        "'52-Point Floor-Ready Standard', '6+ years of Gulf Coast experience' - nothing numeric beyond that.\n"
        "- Prices: stay CONSISTENT with BVA's published ranges (below). Never quote installed prices below "
        "these floors. Use ranges, always add 'free written estimate'.\n"
        "- NAP must stay exactly: BVA Flooring, (941) 807-0339, Bradenton FL 34208. Invent no other phone/address.\n"
        "- title <=65 chars; dek 120-158 chars; both unique. Output ONLY the JSON in one ```json fenced block.\n\n"
        "## BVA PUBLISHED PRICE RANGES (be consistent)\n" + price_reference() + "\n\n"
        "## SITE URLS (link only to these)\n" + urls + "\n"
    )
    user = (
        f"Today is {d.isoformat()} ({d.strftime('%A')}).\n"
        f"TOPIC: {topic['title']}\n"
        f"Use slug: {topic['slug']}\n"
        f"Funnel target (must be in links): {topic.get('funnel')}\n"
        f"Set date and mod to {d.isoformat()}. Write the full post JSON now."
    )
    if correction:
        user += "\n\n## YOUR PREVIOUS DRAFT WAS REJECTED. Fix EVERY issue:\n" + correction
    return system, user

def call_api(system, user):
    import anthropic
    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL, max_tokens=8000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")

def extract_json(text):
    m = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S) or re.search(r"(\{.*\})", text, re.S)
    if not m: raise ValueError("no JSON object in model response")
    return json.loads(m.group(1))

# ── validation (HARD GATE) ──────────────────────────────────────────────────
def validate(p):
    fails = []
    for k in ["slug", "title", "dek", "body", "faqs", "links"]:
        if not p.get(k): fails.append(f"missing/empty '{k}'")
    if fails: return fails
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", p["slug"]): fails.append("slug not kebab-case")
    if p["slug"] in published_slugs(): fails.append("slug already published (cannibalization)")
    if len(p["title"]) > 65: fails.append(f"title {len(p['title'])}>65")
    if not (110 <= len(p["dek"]) <= 160): fails.append(f"dek len {len(p['dek'])} not 110-160")
    body_txt = " ".join(h + " " + html for h, html in p["body"])
    words = len(re.sub(r"<[^>]+>", " ", body_txt).split())
    if words < 1000: fails.append(f"body only {words} words (<1000)")
    if len(p["body"]) < 5: fails.append(f"only {len(p['body'])} H2 sections (<5)")
    if not (4 <= len(p["faqs"]) <= 6): fails.append(f"{len(p['faqs'])} FAQs (need 4-6)")
    vu = valid_urls()
    if not (3 <= len(p["links"]) <= 6): fails.append(f"{len(p['links'])} links (need 3-6)")
    for l in p["links"]:
        if len(l) != 2 or l[1] not in vu: fails.append(f"bad/unknown link url: {l}")
    full = body_txt + " " + " ".join(q + " " + a for q, a in p["faqs"])
    for pat, why in [
        (r"\b\d+\s*(?:\+\s*)?(?:5[- ]?star|five[- ]?star)\b", "fabricated star count"),
        (r"\b\d+\s*(?:google\s+)?reviews?\b", "fabricated review count"),
        (r"\b(?:rated|rating)\s*(?:of\s*)?\d", "fabricated rating"),
        (r"\b\d{2,}\+?\s*(?:projects|installs|homes|jobs|clients)\b", "fabricated project/client count"),
        (r"\blicens\w*\s*#?\s*\d", "fabricated license number"),
        (r"\baward[- ]winning\b|\b#1\b|\bbest in\b", "unverifiable superlative"),
    ]:
        if re.search(pat, full, re.I): fails.append(f"forbidden claim ({why})")
    return fails

# ── deploy ──────────────────────────────────────────────────────────────────
def sh(cmd, cwd=ROOT):
    print("  $", cmd)
    return subprocess.run(cmd, cwd=str(cwd), shell=True, text=True)

def build_site():
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, "build.py"], cwd=str(ROOT), env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("build.py failed:\n" + (r.stdout + r.stderr)[-1000:])
    print("  built site")

def build_dist():
    dist = ROOT / "dist"
    if dist.exists(): shutil.rmtree(dist)
    dist.mkdir()
    skip_dirs = {"previews", "dist", "__pycache__", "automation", ".git"}
    for item in ROOT.iterdir():
        if item.name.startswith(".") or item.name in skip_dirs: continue
        if item.suffix == ".py" or item.name in {"README.md", "run_blog.bat"}: continue
        (shutil.copytree if item.is_dir() else shutil.copy2)(item, dist / item.name)
    print("  built dist/")

def deploy():
    build_dist()
    r = sh("npx --yes wrangler@latest pages deploy dist --project-name bvaflooring "
           "--branch main --commit-dirty=true")
    if r.returncode != 0:
        print("  ! wrangler deploy returned nonzero (check output)")

def git_sync(slug):
    sh("git add -A")
    sh(f'git commit -q -m "post: {slug} (auto)" '
       f'-m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"')
    sh("git push -q origin main")

# ── main ────────────────────────────────────────────────────────────────────
def main():
    d = today()
    topic, topics = pick_topic()
    if not topic:
        print("No unpublished topics left. Add more to topics.json. Nothing to do.")
        return
    if "--dry" in sys.argv:
        print(f"[dry] {d.isoformat()} -> would write '{topic['title']}' (slug={topic['slug']}, "
              f"funnel={topic.get('funnel')}); model={MODEL}")
        return

    print(f"== BVA blog run {d.isoformat()} | topic: {topic['title']} ==")
    POSTS.mkdir(parents=True, exist_ok=True)
    correction = None
    for attempt in range(1, MAX_TRIES + 1):
        if correction: print(f"== retry {attempt}/{MAX_TRIES} ==")
        system, user = build_prompt(topic, d, correction)
        try:
            p = extract_json(call_api(system, user))
        except Exception as e:
            correction = f"Your output could not be parsed as JSON ({e}). Return ONLY one ```json block."
            continue
        p.setdefault("date", d.isoformat()); p.setdefault("mod", d.isoformat())
        p["slug"] = (p.get("slug") or topic["slug"]).strip("/").replace("blog/", "")
        fails = validate(p)
        if fails:
            print("  VALIDATION FAILED:"); [print("   - FAIL", f) for f in fails]
            correction = "Fix EVERY one of these:\n" + "\n".join("- " + f for f in fails)
            continue
        json.dump(p, open(POSTS / f"{p['slug']}.json", "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"  wrote automation/posts/{p['slug']}.json ({attempt} attempt[s])")
        build_site()
        log = json.load(open(PUBLOG, encoding="utf-8")) if PUBLOG.exists() else []
        log.append({"slug": p["slug"], "date": d.isoformat(), "title": p["title"]})
        json.dump(log, open(PUBLOG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        for t in topics:
            if t["slug"] == topic["slug"]: t["status"] = "published"
        json.dump(topics, open(TOPICS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if "--no-deploy" not in sys.argv:
            deploy()
            try: git_sync(p["slug"])
            except Exception as e: print("  ! git sync skipped:", e)
        print(f"PUBLISHED /blog/{p['slug']}/")
        return
    print(f"Exhausted {MAX_TRIES} attempts; validator still failing. Nothing published.")

if __name__ == "__main__":
    main()
