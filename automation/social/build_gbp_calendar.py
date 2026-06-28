#!/usr/bin/env python3
"""Gera a fila de posts do Google Business Profile (GBP) da BVA Flooring.

Mesma ideia da Triangle Flooring: rotaciona servico x cidade x foto real e
monta uma fila JSON que o Make le e publica no GBP (3x/semana, 09:00).
Claims 100% verdadeiros da BVA (52-Point Standard, licensed & insured, free 24h)
-- sem inventar contagem de projetos ou estrelas que a BVA ainda nao tem.

Uso:
    py automation/social/build_gbp_calendar.py [semanas] [data-inicio YYYY-MM-DD]

Saida (mesma pasta):
    calendar-<inicio>.json   fila pro Make (cada item = 1 post do GBP)
    preview-<inicio>.html    revisao visual de tudo
"""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

SITE = "https://bvaflooring.com"
IMG_BASE = f"{SITE}/images/social"   # criativos brandados (template BVA), gerados de /images/projects
PHONE = "(941) 807-0339"
STANDARD = "52-Point Floor-Ready Standard"

CITIES = ["Bradenton", "Sarasota", "Lakewood Ranch", "Palmetto", "Parrish",
          "Venice", "Tampa", "St. Petersburg"]
CITY_PATHS = {c: "/" + c.lower().replace(" ", "-").replace(".", "") + "/" for c in CITIES}

SERVICES = {
    "hardwood": {"name": "Hardwood Flooring", "kw": "hardwood flooring installation", "path": "/hardwood-flooring/"},
    "vinyl":    {"name": "Luxury Vinyl Plank", "kw": "luxury vinyl plank (LVP) installation", "path": "/vinyl-plank-flooring/"},
    "stairs":   {"name": "Stair Treads", "kw": "vinyl stair tread installation", "path": "/stair-treads/"},
}

# Banco de fotos reais (ja no ar em /images/projects/). service = chave de SERVICES.
BANK = [
    {"service": "hardwood", "city": "Bradenton",      "file": "hardwood-flooring-installation-bradenton-fl.jpg",     "desc": "a solid hardwood floor installed in a Bradenton living room"},
    {"service": "hardwood", "city": "Lakewood Ranch", "file": "engineered-hardwood-flooring-lakewood-ranch-fl.jpg",  "desc": "engineered hardwood installed in a Lakewood Ranch home"},
    {"service": "hardwood", "city": "Sarasota",       "file": "hardwood-floor-installation-sarasota-fl.jpg",        "desc": "a hardwood floor installation in a Sarasota home"},
    {"service": "vinyl",    "city": "Sarasota",       "file": "luxury-vinyl-plank-flooring-sarasota-fl.jpg",        "desc": "100% waterproof luxury vinyl plank in a Sarasota home"},
    {"service": "vinyl",    "city": "Tampa",          "file": "waterproof-vinyl-plank-installation-tampa-fl.jpg",   "desc": "a waterproof vinyl plank installation in Tampa"},
    {"service": "vinyl",    "city": "Venice",         "file": "luxury-vinyl-plank-flooring-venice-fl.jpg",          "desc": "luxury vinyl plank (LVP) flooring in a Venice home"},
    {"service": "vinyl",    "city": "St. Petersburg", "file": "wood-look-vinyl-plank-flooring-st-petersburg-fl.jpg","desc": "wood-look vinyl plank in a St. Petersburg room"},
    {"service": "vinyl",    "city": "Palmetto",       "file": "glue-down-vinyl-plank-flooring-palmetto-fl.jpg",     "desc": "glue-down luxury vinyl plank in Palmetto"},
    {"service": "vinyl",    "city": "Parrish",        "file": "glue-down-luxury-vinyl-flooring-parrish-fl.jpg",     "desc": "glue-down luxury vinyl flooring in a Parrish home"},
    {"service": "stairs",   "city": "Bradenton",      "file": "vinyl-stair-tread-installation-bradenton-fl.jpg",    "desc": "a vinyl stair tread installation in Bradenton"},
    {"service": "stairs",   "city": "Tampa",          "file": "waterproof-vinyl-stair-treads-tampa-fl.jpg",         "desc": "waterproof vinyl stair treads installed in Tampa"},
    {"service": "stairs",   "city": "Lakewood Ranch", "file": "vinyl-stair-tread-installation-lakewood-ranch-fl.jpg","desc": "a vinyl stair tread and riser installation in Lakewood Ranch"},
]

# Templates GBP (sem hashtag; keyword+cidade na 1a frase; CTA + telefone no fim).
GBP_TEMPLATES = [
    "{kw_title} in {city}, FL — {desc}. Every BVA Flooring job runs through our {standard}, built for Florida humidity with documented moisture testing. Licensed & insured, with a free written estimate in 24 hours. Call {phone}.",
    "Recent BVA project: {desc}, in {city}, FL. Comparing flooring contractors in {city}? Ask to see real local work — this is ours. One accountable local crew, licensed & insured. Free estimate: {phone}.",
    "Why {city} homeowners choose BVA for {kw}: moisture-tested installs, honest written pricing, and our {standard}. {desc}. Free in-home estimate within 24 hours — {phone}.",
    "{kw_title} done right in {city}, FL. {desc}. New name, old-school standard: one crew, measurable quality, and a written workmanship warranty. Free 24-hour estimate at {phone}.",
]


def pick(seq, i):
    return seq[i % len(seq)]


def build(weeks, start):
    posts = []
    gbp_days = [1, 3, 5]  # ter / qui / sab
    i = 0
    for w in range(weeks):
        for slot in range(3):
            img = pick(BANK, i)
            svc = SERVICES[img["service"]]
            city = img["city"]
            link = SITE + CITY_PATHS.get(city, svc["path"])
            tpl = pick(GBP_TEMPLATES, i)
            caption = tpl.format(
                kw=svc["kw"], kw_title=svc["kw"].capitalize(), svc_name=svc["name"],
                city=city, desc=img["desc"], phone=PHONE, link=link, standard=STANDARD)
            d = start + timedelta(days=w * 7 + gbp_days[slot])
            posts.append({
                "date": d.strftime("%Y-%m-%dT") + "09:00:00",
                "channel": "gbp",
                "service": img["service"], "city": city,
                "image_url": f"{IMG_BASE}/{img['file']}",
                "caption": caption,
                "cta_type": "CALL",
                "cta_phone": PHONE,
                "link": link,
            })
            i += 1
    return posts


def preview_html(posts):
    cards = []
    for p in posts:
        cards.append(f"""<div class="card">
<img src="{p['image_url'].replace(IMG_BASE, '../../images/social')}" loading="lazy">
<div class="body"><span class="ch">Google Posts</span>
<span class="dt">{p['date'][:16].replace('T', ' ')}</span>
<pre>{p['caption']}</pre>
<div class="meta">{p['city']} · {p['service']} · CTA: Call {p['cta_phone']}</div></div></div>""")
    return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<title>Preview — Fila GBP BVA Flooring</title><style>
body{{font-family:'Segoe UI',sans-serif;background:#fbfaf8;padding:24px;color:#1b2330}}
h1{{color:#0E2547}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-top:18px}}
.card{{background:#fff;border-radius:12px;overflow:hidden;border:1px solid #E3DDD3;box-shadow:0 1px 3px rgba(14,37,71,.08)}}
.card img{{width:100%;aspect-ratio:1/1;object-fit:cover;display:block}}.body{{padding:14px}}
.ch{{font-size:.72rem;font-weight:700;text-transform:uppercase;padding:2px 10px;border-radius:20px;background:#EAF0F8;color:#0E2547}}
.dt{{float:right;font-size:.8rem;color:#5d6675}}
pre{{white-space:pre-wrap;font-family:inherit;font-size:.86rem;margin-top:10px;line-height:1.5}}
.meta{{margin-top:8px;font-size:.78rem;color:#5d6675;border-top:1px dashed #E3DDD3;padding-top:8px}}
</style></head><body><h1>📅 Fila GBP — BVA Flooring ({len(posts)} posts)</h1>
<p>Google Posts 3x/semana (ter/qui/sáb, 09:00). Gerado por build_gbp_calendar.py. O Make lê o calendar-*.json e publica no GBP.</p>
<div class="grid">{''.join(cards)}</div></body></html>"""


def main():
    weeks = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    if len(sys.argv) > 2:
        start = datetime.strptime(sys.argv[2], "%Y-%m-%d")
    else:
        start = datetime.now() + timedelta(days=(7 - datetime.now().weekday()) % 7 or 7)
    posts = build(weeks, start)
    stamp = start.strftime("%Y-%m-%d")
    here = Path(__file__).parent
    (here / f"calendar-{stamp}.json").write_text(json.dumps(posts, indent=2, ensure_ascii=False), encoding="utf-8")
    (here / f"preview-{stamp}.html").write_text(preview_html(posts), encoding="utf-8")
    print(f"{len(posts)} GBP posts -> calendar-{stamp}.json + preview-{stamp}.html ({weeks} semanas, inicio {stamp})")


if __name__ == "__main__":
    main()
