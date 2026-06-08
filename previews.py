# -*- coding: utf-8 -*-
"""BVA Flooring — 5 distinct homepage DESIGN DIRECTIONS for approval.
Run: py previews.py  ->  previews/v1..v5/index.html + previews/index.html
Each variant has its own fonts, palette, shape language and hero layout."""
import os
from build import (BRAND, LEGAL, TAGLINE, PHONE_E164, PHONE_DISP, WA, EMAIL, EXPERIENCE,
                   SERVICES, AREAS, SVG_PHONE, SVG_WA, wa_link)

ROOT = os.path.dirname(os.path.abspath(__file__))
ZIP = "34208"

LOGO = """<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-label="BVA Flooring">
<g transform="translate(60,72) rotate(-45)"><rect x="-34" y="-34" width="30" height="30" rx="3" fill="var(--mark1)"/><rect x="4" y="-34" width="30" height="30" rx="3" fill="var(--mark1)"/><rect x="-34" y="4" width="30" height="30" rx="3" fill="var(--mark2)"/><rect x="4" y="4" width="30" height="30" rx="3" fill="var(--mark2)"/></g>
<g transform="translate(60,40)"><polygon points="0,-22 -38,16 -27,16 0,-11 27,16 38,16" fill="var(--accent)"/></g></svg>"""

# ── 5 themes ─────────────────────────────────────────────────────────────────
THEMES = [
 {"id":"v1","name":"Copper Craft","tag":"Warm, premium, trustworthy",
  "gf":"Sora:wght@400;500;600;700;800&family=Source+Sans+3:wght@400;500;600;700",
  "fhead":"'Sora',sans-serif","fbody":"'Source Sans 3',sans-serif",
  "ink":"#15324F","ink2":"#0E2547","accent":"#BE7C3C","accent2":"#A2682E","accentSoft":"#FBF1E2",
  "bg":"#FBFAF8","surf":"#FFFFFF","band":"#F3EDE4","line":"#E7E0D6","text":"#23282E","muted":"#5C6571",
  "mark1":"#16335E","mark2":"#9EAAB8","rad":"14px","brad":"10px","hero":"split","h1w":"700","up":"-.02em"},
 {"id":"v2","name":"Midnight Brass","tag":"Luxe, high-end, editorial",
  "gf":"Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700",
  "fhead":"'Fraunces',serif","fbody":"'Inter',sans-serif",
  "ink":"#0E1A24","ink2":"#0A141C","accent":"#C9A24B","accent2":"#B0883A","accentSoft":"#1B2A35",
  "bg":"#0E1A24","surf":"#152532","band":"#0A141C","line":"#23394A","text":"#E8EDF1","muted":"#9DB0BE",
  "mark1":"#C9A24B","mark2":"#5C7180","rad":"6px","brad":"4px","hero":"dark","h1w":"600","up":"-.01em","dark":True},
 {"id":"v3","name":"Sage & Clay","tag":"Natural, organic, artisanal",
  "gf":"DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700",
  "fhead":"'DM Serif Display',serif","fbody":"'DM Sans',sans-serif",
  "ink":"#2F4A3C","ink2":"#23382D","accent":"#C26B4A","accent2":"#A9553A","accentSoft":"#F3E6DE",
  "bg":"#F7F3EC","surf":"#FFFFFF","band":"#EDE6D8","line":"#E0D8C8","text":"#2B2A26","muted":"#6B6657",
  "mark1":"#2F4A3C","mark2":"#A9B0A0","rad":"22px","brad":"50px","hero":"image","h1w":"400","up":"0"},
 {"id":"v4","name":"Bold Slate","tag":"Modern, high-impact, editorial",
  "gf":"Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700",
  "fhead":"'Space Grotesk',sans-serif","fbody":"'Inter',sans-serif",
  "ink":"#14181B","ink2":"#000000","accent":"#D2622D","accent2":"#B5511F","accentSoft":"#FBEADF",
  "bg":"#F4F4F1","surf":"#FFFFFF","band":"#14181B","line":"#E2E2DC","text":"#14181B","muted":"#585F66",
  "rad":"4px","brad":"2px","hero":"editorial","h1w":"700","up":"-.03em"},
 {"id":"v5","name":"Coastal Blue","tag":"Light, airy, Florida-friendly",
  "gf":"Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Public+Sans:wght@400;500;600;700",
  "fhead":"'Plus Jakarta Sans',sans-serif","fbody":"'Public Sans',sans-serif",
  "ink":"#1F6F8B","ink2":"#16526A","accent":"#E0A458","accent2":"#CE8E3D","accentSoft":"#FBF0DE",
  "bg":"#FBFCFE","surf":"#FFFFFF","band":"#EAF3F6","line":"#E2EAEF","text":"#1B2B33","muted":"#5A6B74",
  "mark1":"#1F6F8B","mark2":"#9EC2CE","rad":"18px","brad":"50px","hero":"soft","h1w":"800","up":"-.02em"},
]

def css(t):
    dark = t.get("dark")
    return f"""
:root{{--ink:{t['ink']};--ink2:{t['ink2']};--accent:{t['accent']};--accent2:{t['accent2']};
--accentSoft:{t['accentSoft']};--bg:{t['bg']};--surf:{t['surf']};--band:{t['band']};--line:{t['line']};
--text:{t['text']};--muted:{t['muted']};--mark1:{t.get('mark1',t['accent'])};--mark2:{t.get('mark2','#9aa')};
--rad:{t['rad']};--brad:{t['brad']};--fhead:{t['fhead']};--fbody:{t['fbody']};--wa:#25D366}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:var(--fbody);background:var(--bg);color:var(--text);line-height:1.65;font-size:16.5px;-webkit-font-smoothing:antialiased}}
img{{max-width:100%;display:block}}
a{{color:inherit;text-decoration:none}}
h1,h2,h3{{font-family:var(--fhead);font-weight:{t['h1w']};line-height:1.12;letter-spacing:{t['up']};color:{'#fff' if dark else 'var(--ink2)'}}}
h1{{font-size:clamp(2.1rem,5.2vw,3.4rem)}}h2{{font-size:clamp(1.6rem,3.4vw,2.3rem)}}h3{{font-size:1.2rem}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 22px}}
.eyebrow{{font-family:var(--fhead);font-size:.75rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);display:inline-block;margin-bottom:.7rem}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:14px 26px;border-radius:var(--brad);font-family:var(--fhead);font-weight:600;font-size:.96rem;border:none;cursor:pointer;transition:.2s}}
.btn-p{{background:var(--accent);color:#fff}}.btn-p:hover{{background:var(--accent2)}}
.btn-o{{background:transparent;color:{'#fff' if dark else 'var(--ink)'};border:1.5px solid {'rgba(255,255,255,.4)' if dark else 'var(--ink)'}}}
.btn-o:hover{{background:{'#fff' if dark else 'var(--ink)'};color:{'var(--ink2)' if dark else '#fff'}}}
.hdr{{position:sticky;top:0;z-index:50;background:{t['bg']}ee;backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}}
.nav{{display:flex;align-items:center;justify-content:space-between;max-width:1180px;margin:0 auto;padding:13px 22px;gap:1rem}}
.brand{{display:flex;align-items:center;gap:11px}}.brand svg{{width:42px;height:42px}}
.bnm{{font-family:var(--fhead);font-weight:800;font-size:1.2rem;color:{'#fff' if dark else 'var(--ink2)'};line-height:1}}
.bsb{{font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);font-weight:600;font-family:var(--fbody)}}
.menu{{display:flex;gap:1.3rem;list-style:none;align-items:center}}
.menu a{{font-family:var(--fhead);font-weight:500;font-size:.94rem;color:{'#cdd8e0' if dark else 'var(--ink2)'}}}
.menu a:hover{{color:var(--accent)}}
.nav-ph{{font-family:var(--fhead);font-weight:700;color:{'#fff' if dark else 'var(--ink)'};font-size:.95rem;display:flex;align-items:center;gap:6px}}
.nav-ph svg{{width:15px;height:15px}}
@media(max-width:900px){{.menu{{display:none}}}}
section{{padding:4.4rem 0}}
.shead{{max-width:720px;margin:0 auto 2.6rem;text-align:center}}
.shead p{{color:var(--muted);margin-top:.5rem;font-size:1.05rem}}
.proof{{background:var(--ink2);color:#fff;padding:1.1rem 0}}
.proof .row{{display:flex;flex-wrap:wrap;justify-content:center;gap:1rem 2.6rem;text-align:center}}
.proof b{{display:block;font-family:var(--fhead);font-size:1.3rem;color:#fff}}
.proof b.a{{color:var(--accent)}}
.proof div{{font-size:.88rem;color:#ffffffbb}}
.sgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.3rem}}
.scard{{background:var(--surf);border:1px solid var(--line);border-radius:var(--rad);padding:1.6rem;transition:.2s;color:var(--text)}}
.scard:hover{{transform:translateY(-4px);box-shadow:0 18px 40px {'#00000055' if dark else 'rgba(20,40,70,.13)'};border-color:var(--accent)}}
.sic{{width:52px;height:52px;border-radius:calc(var(--rad) - 4px);background:var(--accentSoft);display:grid;place-items:center;font-size:1.7rem;margin-bottom:1rem}}
.scard h3{{color:{'#fff' if dark else 'var(--ink2)'};margin-bottom:.4rem}}
.scard p{{color:var(--muted);font-size:.95rem;margin-bottom:.8rem}}
.scard .m{{font-family:var(--fhead);font-weight:600;font-size:.88rem;color:var(--accent)}}
.fgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.4rem}}
.feat{{background:var(--band);border-radius:var(--rad);padding:1.6rem;color:{'#dfe7ec' if dark else 'var(--text)'}}}
.feat .n{{font-family:var(--fhead);font-size:1.5rem;font-weight:700;color:var(--accent);margin-bottom:.4rem}}
.feat h3{{font-size:1.1rem;margin-bottom:.4rem;color:{'#fff' if dark else 'var(--ink2)'}}}
.feat p{{color:{'#aebcc6' if dark else 'var(--muted)'};font-size:.94rem}}
.fcta{{background:{('linear-gradient(160deg,#0A141C,#152532)' if dark else 'linear-gradient(160deg,var(--ink2),var(--ink))')};color:#fff;text-align:center;padding:4.6rem 0}}
.fcta h2{{color:#fff;margin-bottom:.7rem}}.fcta p{{color:#ffffffcc;max-width:600px;margin:0 auto 1.4rem}}
.fcta .ph{{font-family:var(--fhead);font-size:1.6rem;font-weight:800;color:#fff;display:inline-block;margin:.5rem 0}}
.fcta .bts{{display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap}}
footer{{background:{'#070F16' if dark else 'var(--ink2)'};color:#ffffffb0;padding:3rem 0 1.6rem;font-size:.9rem}}
.fg{{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:2rem;margin-bottom:2rem}}
footer h4{{color:#fff;font-size:.8rem;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.9rem;font-family:var(--fhead)}}
footer a{{color:#ffffff9e}}footer a:hover{{color:var(--accent)}}footer li{{list-style:none;margin-bottom:.5rem}}
.fbrand{{display:flex;align-items:center;gap:10px;margin-bottom:.9rem}}.fbrand svg{{width:40px;height:40px}}.fbrand b{{font-family:var(--fhead);color:#fff;font-size:1.15rem}}
.fbot{{border-top:1px solid #ffffff22;padding-top:1.2rem;font-size:.82rem;color:#ffffff80}}
.tag{{display:inline-flex;align-items:center;gap:6px;font-family:var(--fhead);font-weight:600;font-size:.9rem;color:{'#dfe7ec' if dark else 'var(--text)'}}}
.tag::before{{content:'✓';color:var(--accent);font-weight:800}}
.hero-split{{display:grid;grid-template-columns:1.2fr .9fr;gap:2.4rem;align-items:center;padding:3.6rem 0}}
.hero-split .lead{{font-size:1.1rem;color:var(--muted);margin:1rem 0 1.5rem;max-width:540px}}
.ecard{{background:var(--surf);border:1px solid var(--line);border-radius:var(--rad);padding:1.7rem;box-shadow:0 20px 46px rgba(20,40,70,.14)}}
.ecard h3{{margin-bottom:.2rem}}.ecard .s{{color:var(--muted);font-size:.88rem;margin-bottom:1rem}}
.ecard label{{font-family:var(--fhead);font-size:.74rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:{'#cdd8e0' if dark else 'var(--ink2)'};display:block;margin:.55rem 0 .25rem}}
.ecard input,.ecard select{{width:100%;padding:11px 13px;border:1.5px solid var(--line);border-radius:calc(var(--brad));background:var(--bg);font-family:var(--fbody);color:var(--text)}}
.ecard .btn{{width:100%;margin-top:1rem;justify-content:center}}
.htrust{{display:flex;flex-wrap:wrap;gap:.5rem 1.3rem;margin-top:1.4rem}}
.stars{{color:#F2B84B;letter-spacing:2px}}
.hero-dark{{text-align:center;padding:5rem 0 4.4rem;position:relative}}
.hero-dark .rule{{width:60px;height:2px;background:var(--accent);margin:0 auto 1.4rem}}
.hero-dark .lead{{color:#c9d4dc;font-size:1.15rem;max-width:640px;margin:1.2rem auto 1.8rem}}
.hero-img{{display:grid;grid-template-columns:1.05fr 1fr;gap:2.4rem;align-items:center;padding:3.4rem 0}}
.hero-img .ph{{aspect-ratio:4/3;border-radius:var(--rad);background:linear-gradient(135deg,var(--ink),var(--accent));position:relative;overflow:hidden;box-shadow:0 24px 50px rgba(40,40,30,.2)}}
.hero-img .ph span{{position:absolute;bottom:14px;left:14px;background:#ffffffe6;color:var(--ink2);padding:7px 14px;border-radius:50px;font-family:var(--fhead);font-weight:700;font-size:.82rem}}
.hero-img .lead{{font-size:1.12rem;color:var(--muted);margin:1rem 0 1.6rem}}
.hero-ed{{padding:3.6rem 0 3rem;border-bottom:3px solid var(--ink2)}}
.hero-ed h1{{font-size:clamp(2.6rem,7vw,5rem);line-height:.98}}
.hero-ed .lead{{font-size:1.18rem;color:var(--muted);max-width:620px;margin:1.4rem 0 1.7rem}}
.hero-ed .meta{{display:flex;gap:2rem;flex-wrap:wrap;margin-top:2rem;border-top:1px solid var(--line);padding-top:1.4rem}}
.hero-ed .meta b{{font-family:var(--fhead);font-size:1.7rem;color:var(--ink2);display:block}}
.hero-ed .meta span{{font-size:.84rem;color:var(--muted)}}
.hero-soft{{position:relative;padding:3.8rem 0;background:radial-gradient(900px 400px at 80% 0%,var(--band),transparent),var(--bg)}}
.hero-soft .grid{{display:grid;grid-template-columns:1.15fr .85fr;gap:2.4rem;align-items:center}}
.hero-soft .lead{{font-size:1.12rem;color:var(--muted);margin:1rem 0 1.6rem;max-width:520px}}
.hero-soft .glass{{background:#ffffffcc;backdrop-filter:blur(8px);border:1px solid var(--line);border-radius:var(--rad);padding:1.7rem;box-shadow:0 20px 46px rgba(31,111,139,.15)}}
@media(max-width:880px){{.hero-split,.hero-img,.hero-soft .grid{{grid-template-columns:1fr;gap:1.6rem}}.fg{{grid-template-columns:1fr 1fr}}.ecard,.glass{{max-width:440px}}}}
.wafloat{{position:fixed;bottom:20px;right:20px;z-index:60;background:var(--wa);color:#fff;padding:12px 18px;border-radius:50px;font-family:var(--fhead);font-weight:600;font-size:.9rem;display:flex;align-items:center;gap:8px;box-shadow:0 8px 24px rgba(37,211,102,.45)}}
.wafloat svg{{width:19px;height:19px}}
.vbar{{position:sticky;top:0;z-index:80;background:var(--ink2);color:#fff;text-align:center;padding:8px;font-family:var(--fhead);font-size:.84rem;letter-spacing:.02em}}
.vbar a{{color:var(--accent);font-weight:700}}
"""

def header(t):
    dark=t.get("dark")
    links="".join(f'<li><a href="#">{x}</a></li>' for x in ["Home","Services","Service Areas","About","Contact"])
    return f"""<header class="hdr"><div class="nav">
<a class="brand" href="#">{LOGO}<span><span class="bnm">{BRAND}</span><br><span class="bsb">{TAGLINE}</span></span></a>
<ul class="menu">{links}</ul>
<a class="nav-ph" href="tel:{PHONE_E164}">{SVG_PHONE}{PHONE_DISP}</a></div></header>"""

def services_grid():
    return "".join(
        f'<a class="scard" href="#"><div class="sic">{s["icon"]}</div><h3>{s["name"]}</h3>'
        f'<p>{s["blurb"]}</p><span class="m">Explore {s["short"]} →</span></a>' for s in SERVICES)

FEATS=[("01","One crew, start to finish","The team that measures your floor installs it — and answers when you call after."),
       ("02","Built for Florida humidity","Documented moisture testing and a 48–72 hr acclimation window on every single job."),
       ("03","Written, itemized pricing","Material, labor, prep and haul-away in writing within 24 hours. No surprise upcharges."),
       ("04","A standard you can audit","Every floor passes our 52-Point Floor-Ready inspection before we call it done.")]

def estimate_card(extra_cls=""):
    opts="".join(f"<option>{s['name']}</option>" for s in SERVICES)
    return f"""<div class="ecard {extra_cls}"><h3>Free Flooring Estimate</h3><p class="s">No obligation · reply in 24 hours</p>
<label>Name</label><input placeholder="Your name">
<label>Phone</label><input placeholder="{PHONE_DISP}">
<label>Project</label><select>{opts}</select>
<a class="btn btn-p" href="#">Request My Estimate</a></div>"""

def hero(t):
    trust='<span class="tag">Licensed & insured</span><span class="tag">Since 2020</span><span class="tag">52-Point Standard</span><span class="tag"><span class="stars">★★★★★</span></span>'
    H1='Flooring Installation in Bradenton, FL'
    style=t["hero"]
    if style=="split":
        return f"""<section><div class="wrap hero-split"><div>
<span class="eyebrow">Bradenton · Sarasota · Tampa Bay</span>
<h1>{H1} — Done Right the First Time</h1>
<p class="lead">Hardwood, luxury vinyl plank, tile, laminate & stairs — installed for Florida humidity by one accountable local crew.</p>
<div style="display:flex;gap:.7rem;flex-wrap:wrap"><a class="btn btn-p" href="#">Get My Free Quote</a><a class="btn btn-o" href="tel:{PHONE_E164}">{SVG_PHONE} {PHONE_DISP}</a></div>
<div class="htrust">{trust}</div></div>{estimate_card()}</div></section>"""
    if style=="dark":
        return f"""<section class="hero-dark"><div class="wrap"><div class="rule"></div>
<span class="eyebrow">Bradenton · Sarasota · Tampa Bay</span>
<h1>{H1}<br>Crafted to Last a Lifetime</h1>
<p class="lead">Hardwood, luxury vinyl plank, tile and stairs — installed for the Gulf Coast with documented moisture testing and a written workmanship warranty.</p>
<div class="bts" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap"><a class="btn btn-p" href="#">Get My Free Quote</a><a class="btn btn-o" href="tel:{PHONE_E164}">{SVG_PHONE} {PHONE_DISP}</a></div>
<div class="htrust" style="justify-content:center">{trust}</div></div></section>"""
    if style=="image":
        return f"""<section><div class="wrap hero-img"><div>
<span class="eyebrow">Bradenton · Sarasota · Tampa Bay</span>
<h1>{H1}, Done by Hand</h1>
<p class="lead">Real craftsmanship for real Florida homes — hardwood, vinyl plank, tile, laminate and stairs, installed for the way Gulf-Coast houses actually live.</p>
<div style="display:flex;gap:.7rem;flex-wrap:wrap"><a class="btn btn-p" href="#">Get My Free Quote</a><a class="btn btn-o" href="tel:{PHONE_E164}">{SVG_PHONE} {PHONE_DISP}</a></div>
<div class="htrust">{trust}</div></div>
<div class="ph"><span>📷 AI / project photo here</span></div></div></section>"""
    if style=="editorial":
        return f"""<section class="hero-ed"><div class="wrap">
<span class="eyebrow">Bradenton · Sarasota · Tampa Bay</span>
<h1>Floors that<br>outlast the<br><span style="color:var(--accent)">Florida humidity.</span></h1>
<p class="lead">Hardwood, luxury vinyl plank, tile, laminate & stairs — installed by one accountable local crew, measured and warrantied in writing.</p>
<div style="display:flex;gap:.7rem;flex-wrap:wrap"><a class="btn btn-p" href="#">Get My Free Quote</a><a class="btn btn-o" href="tel:{PHONE_E164}">{SVG_PHONE} {PHONE_DISP}</a></div>
<div class="meta"><div><b>52</b><span>Point Floor-Ready Standard</span></div><div><b>Since 2020</b><span>Gulf Coast experience</span></div><div><b>24 hr</b><span>Free written estimate</span></div><div><b>8</b><span>Cities served</span></div></div></div></section>"""
    return f"""<section class="hero-soft"><div class="wrap grid"><div>
<span class="eyebrow">Bradenton · Sarasota · Tampa Bay</span>
<h1>{H1} — Clean, Quick, Guaranteed</h1>
<p class="lead">Waterproof vinyl plank, hardwood, tile, laminate & stairs for Florida living — installed by one friendly local crew you can actually reach.</p>
<div style="display:flex;gap:.7rem;flex-wrap:wrap"><a class="btn btn-p" href="#">Get My Free Quote</a><a class="btn btn-o" href="tel:{PHONE_E164}">{SVG_PHONE} {PHONE_DISP}</a></div>
<div class="htrust">{trust}</div></div>{estimate_card("glass")}</div></section>"""

def render(t):
    svc=services_grid()
    feats="".join(f'<div class="feat"><div class="n">{n}</div><h3>{h}</h3><p>{p}</p></div>' for n,h,p in FEATS)
    foot_links="".join(f"<li><a href='#'>{s['name']}</a></li>" for s in SERVICES)
    nextv={"v1":"v2","v2":"v3","v3":"v4","v4":"v5","v5":"v1"}[t["id"]]
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BRAND} — {t['name']} (Design Option {t['id'][-1]}/5)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={t['gf']}&display=swap" rel="stylesheet">
<style>{css(t)}</style></head><body>
<div class="vbar">Design Option {t['id'][-1]} of 5 · <b>{t['name']}</b> — {t['tag']} &nbsp;·&nbsp; <a href="../index.html">◀ All options</a> &nbsp;·&nbsp; <a href="../{nextv}/index.html">Next ▶</a></div>
{header(t)}
{hero(t)}
<div class="proof"><div class="wrap"><div class="row">
<div><b class="a">52-Point</b>Floor-Ready Standard</div><div><b>Since 2020</b>Gulf Coast experience</div>
<div><b>24 hr</b>Free written estimate</div><div><b>8 cities</b>Across Tampa Bay</div>
<div><b class="a">★★★★★</b>Workmanship pledge</div></div></div></div>
<section><div class="wrap"><div class="shead"><span class="eyebrow">What We Install</span><h2>Flooring Services Across Tampa Bay</h2><p>Six core services, one standard of work.</p></div><div class="sgrid">{svc}</div></div></section>
<section style="background:var(--band)"><div class="wrap"><div class="shead"><span class="eyebrow">Why BVA</span><h2>A New Name, an Old-School Standard</h2></div><div class="fgrid">{feats}</div></div></section>
<section class="fcta"><div class="wrap"><span class="eyebrow">Ready when you are</span><h2>Get Your Free Flooring Estimate</h2>
<p>Free measurement. Locked-in pricing. Written workmanship warranty across Bradenton & Tampa Bay.</p>
<a class="ph" href="tel:{PHONE_E164}">📞 {PHONE_DISP}</a>
<div class="bts"><a class="btn btn-p" href="#">Get My Free Quote</a><a class="btn btn-o" href="{wa_link()}">{SVG_WA} WhatsApp Us</a></div></div></section>
<footer><div class="wrap"><div class="fg">
<div><div class="fbrand">{LOGO}<b>{BRAND}</b></div><p style="color:#ffffff9e;max-width:340px">Professional flooring installation across Bradenton, Sarasota & the Tampa Bay Gulf Coast. Installed for Florida humidity, backed in writing.</p></div>
<div><h4>Services</h4><ul>{foot_links}</ul></div>
<div><h4>Contact</h4><ul><li><a href="tel:{PHONE_E164}">{PHONE_DISP}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Bradenton, FL {ZIP}</li><li>Mon–Sat · 7 AM – 7 PM</li></ul></div>
</div><div class="fbot">© 2026 {LEGAL} ({BRAND}) · Licensed & insured · Serving Bradenton & Tampa Bay, FL {ZIP}</div></div></footer>
<a class="wafloat" href="{wa_link()}">{SVG_WA} Free Quote</a>
</body></html>"""

def chooser():
    cards=""
    for t in THEMES:
        sw="".join(f'<span style="background:{c}"></span>' for c in [t['ink'],t['accent'],t['band'],t['bg']])
        head=t['fhead'].split(',')[0].replace("'","")
        body=t['fbody'].split(',')[0].replace("'","")
        cards+=f"""<a class="opt" href="{t['id']}/index.html">
<div class="sw">{sw}</div><div class="ot"><b>Option {t['id'][-1]} · {t['name']}</b><span>{t['tag']}</span>
<span class="ff">{head} + {body}</span></div></a>"""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BRAND} — Choose a Design (5 options)</title>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:Inter,sans-serif;background:#0E1A24;color:#fff;padding:3rem 1.2rem;min-height:100vh}}
.h{{max-width:880px;margin:0 auto 2.2rem;text-align:center}}
.h h1{{font-family:Sora,sans-serif;font-size:2.2rem;margin-bottom:.5rem}}.h p{{color:#9db0be}}
.grid{{max-width:880px;margin:0 auto;display:grid;gap:1rem}}
.opt{{display:flex;gap:1.2rem;align-items:center;background:#152532;border:1px solid #23394a;border-radius:14px;padding:1.1rem 1.3rem;color:#fff;text-decoration:none;transition:.2s}}
.opt:hover{{border-color:#C9A24B;transform:translateY(-2px)}}
.sw{{display:flex;gap:5px;flex-shrink:0}}.sw span{{width:26px;height:46px;border-radius:6px;border:1px solid #ffffff22}}
.ot{{display:flex;flex-direction:column;gap:3px}}.ot b{{font-family:Sora,sans-serif;font-size:1.1rem}}
.ot span{{color:#9db0be;font-size:.9rem}}.ot .ff{{color:#C9A24B;font-size:.8rem;letter-spacing:.03em}}
</style></head><body>
<div class="h"><h1>BVA Flooring — 5 Design Directions</h1><p>Click any option to preview the full homepage. Then tell me the number you want.</p></div>
<div class="grid">{cards}</div></body></html>"""

def main():
    print("Building 5 design previews ->", os.path.join(ROOT,"previews"))
    for t in THEMES:
        d=os.path.join(ROOT,"previews",t["id"])
        os.makedirs(d,exist_ok=True)
        open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(render(t))
        print("  +",f"previews/{t['id']}/index.html",f"({t['name']})")
    open(os.path.join(ROOT,"previews","index.html"),"w",encoding="utf-8").write(chooser())
    print("  + previews/index.html (chooser)")
    print("Done.")

if __name__=="__main__":
    main()
