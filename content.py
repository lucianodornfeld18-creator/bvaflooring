# -*- coding: utf-8 -*-
"""BVA Flooring — page bodies & original copy. Imported by build.py."""
import re
from build import (BRAND, LEGAL, TAGLINE, DOMAIN, PHONE_E164, PHONE_DISP, WA, EMAIL,
                   BASE_CITY, STATE, EXPERIENCE, STANDARD, SERVICES, SVC, AREAS, CITIES,
                   head, header, footer, wa_float, wa_banner, final_cta, MENU_JS, jsonld,
                   sc_org, sc_localbiz, sc_breadcrumb, sc_website, crumbs, faq_block,
                   SVG_PHONE, SVG_WA, wa_link)

# ── Logo (compact, transparent bg; whitened in footer via CSS) ──────────────
LOGO_SVG = """<svg width="120" height="120" viewBox="0 0 120 120" role="img" xmlns="http://www.w3.org/2000/svg">
<title>BVA Flooring</title>
<g transform="translate(60,72) rotate(-45)">
<rect x="-34" y="-34" width="30" height="30" rx="3" fill="#16335E"/>
<rect x="4" y="-34" width="30" height="30" rx="3" fill="#16335E"/>
<rect x="-34" y="4" width="30" height="30" rx="3" fill="#9EAAB8"/>
<rect x="4" y="4" width="30" height="30" rx="3" fill="#9EAAB8"/></g>
<g transform="translate(60,40)"><polygon points="0,-22 -38,16 -27,16 0,-11 27,16 38,16" fill="#C0843C"/></g>
</svg>"""

STARS = '<span class="stars">★★★★★</span>'

# ── Proprietary 52-Point standard (same across service pages) ───────────────
CHECKLIST = [
 ("📐","Site &amp; Subfloor","Assessment", [
   "Full walk-through &amp; scope confirmation","Existing floor &amp; subfloor type logged",
   "Flatness check to 3/16\" over 10  ft","Slab crack &amp; control-joint mapping",
   "Soft-spot &amp; squeak probe","Transition &amp; threshold heights measured",
   "Doorway &amp; jamb undercut plan","Trim / baseboard condition noted",
   "Furniture &amp; appliance move plan","Pet &amp; family access plan",
   "Photo documentation of starting state","Written measurement &amp; waste calc"]),
 ("💧","Moisture &amp; Humidity","Control", [
   "Digital subfloor moisture reading","Calcium-chloride or RH probe on slab",
   "Ambient humidity &amp; temp logged","Vapor barrier spec confirmed",
   "Perimeter expansion gap planned","Wet-area waterproofing checked",
   "AC running for stable interior RH","Concrete cure age verified (new builds)",
   "Manufacturer moisture limits cross-checked","Go / no-go sign-off before install"]),
 ("📦","Material Prep &amp;","Acclimation", [
   "Product matched to room &amp; traffic","Batch / dye-lot numbers verified",
   "48–72 hr on-site acclimation","Boxes opened &amp; cross-stacked",
   "Defect &amp; shade sort","Underlayment / pad selected",
   "Layout &amp; seam plan drawn","Start wall &amp; sightline chosen",
   "Stagger / random-length pattern set","Cut-station &amp; dust control set up"]),
 ("🔨","Installation","Craft", [
   "Subfloor cleaned &amp; fastened","Self-leveler where needed",
   "Underlayment seams taped","Precision jamb &amp; casing undercuts",
   "Tight, staggered end-joints","Expansion gaps held at perimeter",
   "Adhesive / lock-engagement checked row-by-row","Tile back-buttered &amp; lippage-tuned",
   "Even grout joints &amp; full coverage","Stair treads glued &amp; mechanically set",
   "Transitions &amp; reducers fitted","Level &amp; hollow-spot tap test"]),
 ("✨","Finish, Cleanup &amp;","Sign-off", [
   "Color-matched fill &amp; putty","Shoe molding / quarter-round reinstalled",
   "Caulk &amp; silicone at wet edges","Full vacuum &amp; damp clean",
   "Haul-away of debris &amp; offcuts","Care &amp; maintenance hand-off",
   "Final walk-through with you","Written workmanship warranty issued"]),
]

def checklist_section():
    cards=""
    for emoji,cat,cat2,items in CHECKLIST:
        lis="".join(f"<li>{it}</li>" for it in items)
        cards+=(f'<div class="chk"><div class="chk-h"><span class="e">{emoji}</span>'
                f'<div><b>{cat} {cat2}</b><span>{len(items)} checkpoints</span></div></div>'
                f'<ol>{lis}</ol></div>')
    total=sum(len(i[3]) for i in CHECKLIST)
    return (f'<section><div class="wrap"><div class="shead"><span class="eyebrow">Our Standard</span>'
            f'<h2>The {STANDARD}</h2><p>Every BVA floor passes the same {total}-point Floor-Ready '
            f'inspection — from subfloor moisture to the final baseboard — before we call a job done. '
            f'It is how a new company earns trust the hard way: by being measurable.</p></div>'
            f'<div class="chk-grid">{cards}</div></div></section>')

def stat_badge(extra=""):
    return (f'<div class="stat"><span class="i">🏅</span><div>'
            f'<p>Every BVA floor passes a 52-point Floor-Ready inspection before we call it done.</p>'
            f'<p class="s">{EXPERIENCE} of Gulf Coast flooring experience · Licensed &amp; insured · {STARS} workmanship</p>'
            f'</div></div>')

# ── Per-service data ────────────────────────────────────────────────────────
SVC_DATA = {
 "hardwood-flooring":{
   "intro":("Real wood rewards good installation and punishes shortcuts — especially in Florida. "
            "Engineered hardwood is the Gulf-Coast workhorse because its layered core shrugs off the "
            "humidity swings that make solid planks cup. Whichever you choose, the result lives or dies "
            "on acclimation, moisture testing, and a flat subfloor."),
   "included":["Engineered &amp; solid hardwood","Site-finished &amp; prefinished options","Documented moisture testing",
               "48–72 hr acclimation","Precision jamb undercuts","Color-matched fill &amp; putty",
               "Stair nosing &amp; transitions","Shoe molding reinstall"],
   "prices":[("Engineered hardwood — installed","$9–$14 / sq ft","Most popular for FL humidity"),
             ("Solid / site-finished — installed","$12–$18 / sq ft","Sand &amp; finish on site"),
             ("Stair nosing &amp; transitions","$45–$90 / piece","Matched to your floor"),
             ("Tear-out &amp; haul-away","$1.50–$3 / sq ft","Old floor removal")],
 },
 "vinyl-plank-flooring":{
   "intro":("Waterproof, scratch-tough, and warm underfoot, luxury vinyl plank is the floor Florida "
            "homeowners and rental owners pick when they want wood looks without wood worries. The catch: "
            "rigid-core LVP telegraphs every bump in the subfloor. Flat-and-clean prep is the whole game."),
   "included":["Rigid-core SPC &amp; floating LVP","100% waterproof wear layers","Subfloor leveling &amp; prep",
               "Moisture barrier where needed","Tight, staggered seams","Square, sightline-true layout",
               "Transitions &amp; T-moldings","Quarter-round reinstall"],
   "prices":[("Floating LVP (5–6 mm) — installed","$5–$8 / sq ft","Great everyday waterproof floor"),
             ("Rigid-core SPC — installed","$6–$9 / sq ft","Most durable / pet &amp; rental friendly"),
             ("Labor only (you supply material)","$2.50–$4 / sq ft","Supply-your-own installs"),
             ("Subfloor leveling","$1–$3 / sq ft","As needed for flatness")],
 },
 "tile-installation":{
   "intro":("Tile is the most permanent floor you can buy — which means a bad set is the most expensive "
            "to fix. Lippage, hollow spots, and crooked grout lines are all preventable with the right "
            "mortar coverage, layout, and a dead-flat base. We set tile to last decades, not seasons."),
   "included":["Porcelain, ceramic &amp; large-format","Showers, floors &amp; lanais","Waterproofing at wet areas",
               "Crack-isolation membrane","Back-buttered full coverage","Lippage-tuned, level sets",
               "Even, sealed grout joints","Demo &amp; subfloor prep"],
   "prices":[("Porcelain / ceramic floor — installed","$9–$15 / sq ft","Standard field tile"),
             ("Large-format (24\"+) — installed","$13–$20 / sq ft","Leveling-clip set"),
             ("Shower / wet wall — installed","$18–$28 / sq ft","Full waterproofing"),
             ("Demo &amp; prep","$2–$4 / sq ft","Old tile removal &amp; flatten")],
 },
 "laminate-flooring":{
   "intro":("Modern laminate has come a long way — high-AC-rating planks look convincingly like wood and "
            "stand up to kids, pets, and traffic for a fraction of the cost. The difference between a floor "
            "that looks built-in and one that looks cheap is almost entirely in the seams and the prep."),
   "included":["AC4 &amp; AC5 commercial-grade","Wood, stone &amp; tile looks","Quality underlayment",
               "Subfloor flatten &amp; clean","Tight, level seams","Expansion gaps held true",
               "Transitions &amp; reducers","Baseboard / shoe reinstall"],
   "prices":[("AC4 laminate — installed","$4.50–$7 / sq ft","Great value, residential"),
             ("AC5 commercial-grade — installed","$6–$8.50 / sq ft","Highest traffic / rentals"),
             ("Underlayment upgrade","$0.40–$1 / sq ft","Sound &amp; moisture"),
             ("Labor only (you supply material)","$2–$3.50 / sq ft","Supply-your-own installs")],
 },
 "stair-treads":{
   "intro":("Stairs are the hardest-working surface in the house and the most visible. Swapping tired carpet "
            "for solid wood treads transforms a staircase — but it is precision joinery, not plank-laying. "
            "Every tread has to be solid, quiet, and consistent, with overhangs and risers that line up."),
   "included":["Carpet-to-wood conversions","Retreads over existing stairs","Solid &amp; stained treads",
               "Matching risers &amp; nosing","Glued &amp; mechanically fastened","Squeak elimination",
               "Stain &amp; seal to match floors","Quiet, code-minded rise/run"],
   "prices":[("Retread over existing","$80–$150 / tread","Cap existing stringers"),
             ("Full reface (tread + riser)","$130–$220 / step","New tread &amp; riser"),
             ("Carpet-to-wood conversion","$140–$240 / step","Remove carpet, build out"),
             ("Matching stain &amp; seal","$25–$50 / step","Color-matched to your floor")],
 },
 "floor-repair":{
   "intro":("Not every floor problem needs a full tear-out. Water-damaged boards, a few hollow tiles, an "
            "annoying squeak, or a failed seam can usually be fixed in place — if you catch it before it "
            "spreads. We diagnose honestly and fix the cause, not just the symptom."),
   "included":["Water-damaged board replacement","Hollow / cracked tile re-set","Squeak &amp; movement fixes",
               "Failed seam &amp; gap repair","Transition &amp; threshold fixes","Subfloor patch &amp; flatten",
               "Color &amp; grain matching","Honest repair-vs-replace advice"],
   "prices":[("Diagnostic visit","$95–$175","Credited toward the repair"),
             ("Board / plank replacement","$8–$20 / sq ft","Match &amp; blend"),
             ("Hollow / cracked tile re-set","$25–$55 / tile","Re-bed &amp; re-grout"),
             ("Water-damage section","$400–$1,400","Scope-dependent")],
 },
}

def price_table(svc, city):
    s=SVC_DATA[svc["slug"]]
    rows=""
    for label,price,note in s["prices"]:
        rows+=f'<tr><td>{label}</td><td class="pr">{price}</td><td>{note}</td></tr>'
    return (f'<section class="pricing"><div class="wrap"><div class="shead">'
            f'<span class="eyebrow">Transparent Pricing</span>'
            f'<h2>{svc["short"]} Prices in {city} (2026)</h2>'
            f'<p>Real Gulf-Coast market ranges — no "call for pricing" games. '
            f'Your written, custom estimate is free: <a href="tel:{PHONE_E164}">{PHONE_DISP}</a>.</p></div>'
            f'{stat_badge()}'
            f'<div class="ptab"><table><thead><tr><th>Option</th><th>Typical Range</th><th>Notes</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
            f'<p class="pnote">* Final price depends on material, square footage, prep &amp; access. '
            f'<a href="/contact/#quote">Get a free custom estimate →</a></p></div></section>')

def included_section(svc):
    s=SVC_DATA[svc["slug"]]
    items="".join(f'<span>✓ {it}</span>' for it in s["included"])
    return (f'<section class="intro"><div class="wrap"><div class="shead">'
            f'<span class="eyebrow">What\'s Included</span><h2>What a {svc["short"]} Job With BVA Covers</h2></div>'
            f'<div class="nbhd" style="max-width:980px">{items}</div></div></section>')

# ── Service-city FAQs ───────────────────────────────────────────────────────
def svc_city_faqs(svc, city):
    short=svc["short"]
    return [
     (f"How much does {short.lower()} cost in {city}, FL?",
      f"Most {city} {short.lower()} projects land within the ranges in the table above, which reflect real "
      f"Gulf-Coast market rates for 2026. Your exact price depends on square footage, the material you pick, "
      f"how much subfloor prep is needed, and access. We give you a free, written, itemized estimate so you "
      f"can compare apples to apples — no vague phone guesses."),
     (f"How long does a {short.lower()} install take in {city}?",
      f"A typical {city} room or two is usually 1–3 working days once materials are on site and acclimated. "
      f"Whole-home jobs run longer. Because Florida humidity demands a 48–72 hour acclimation window for many "
      f"products, we build that into the schedule up front instead of rushing it."),
     (f"Do you handle the humidity issues common in {city} homes?",
      f"Yes — it is the core of how we work. Every BVA install includes documented subfloor moisture testing, "
      f"ambient humidity logging, and a go/no-go sign-off before a single plank goes down. That is what keeps "
      f"{city} floors from cupping, gapping, or peeling a season later."),
     (f"Do you offer a warranty on {short.lower()} in {city}?",
      f"Every job comes with a written BVA workmanship warranty on top of the manufacturer's product warranty. "
      f"We are licensed, insured, and local — if anything needs attention, you call us directly, not a hotline."),
     (f"Will you move furniture and haul away the old floor?",
      f"In most {city} homes, yes. We include a furniture and appliance move plan and debris haul-away in the "
      f"estimate so there are no surprise line items. Anything outside normal scope is spelled out in writing first."),
    ]

# ── Pages ───────────────────────────────────────────────────────────────────
FOUND_OPTS = ["— How did you find us? —","Google Search","Google Maps","Facebook / Instagram",
              "Friend or family referral","Saw your work / drove by","Nextdoor","Yelp / Angi / Thumbtack","Other"]

def quote_form(compact=False):
    from build import WEB3FORMS_KEY
    svc_opts="".join(f"<option>{s['name']}</option>" for s in SERVICES)
    city_opts="<option value=''>— Select —</option>"+"".join(f"<option>{nm}</option>" for _,nm in AREAS)
    found_opts="".join((f"<option value=''>{o}</option>" if o.startswith('—') else f"<option>{o}</option>") for o in FOUND_OPTS)
    if WEB3FORMS_KEY:
        top=(f'<form action="https://api.web3forms.com/submit" method="POST">'
             f'<input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">'
             f'<input type="hidden" name="subject" value="New Quote Request — {BRAND}">'
             f'<input type="hidden" name="from_name" value="{BRAND} Website">'
             f'<input type="hidden" name="redirect" value="https://{DOMAIN}/thanks/">'
             f'<input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">')
    else:
        top='<form action="/thanks/" method="get">'
    if compact:
        return (top+
          '<label>Name</label><input name="name" placeholder="Your name" required autocomplete="name">'
          f'<label>Phone</label><input name="phone" type="tel" placeholder="{PHONE_DISP}" required autocomplete="tel">'
          f'<label>Service Needed</label><select name="service">{svc_opts}</select>'
          '<label>Tell us about your project</label><textarea name="message" placeholder="Rooms, approx. square footage, timeline, products you have in mind, current floor..."></textarea>'
          f'<label>How did you find us?</label><select name="found">{found_opts}</select>'
          '<button class="btn btn-primary" type="submit">Request My Estimate</button>'
          f'<p class="fine">Prefer to talk now? Call or text {PHONE_DISP}</p></form>')
    return (top+
      '<div class="frow"><div><label>Name</label><input name="name" placeholder="Your name" required autocomplete="name"></div>'
      f'<div><label>Phone</label><input name="phone" type="tel" placeholder="{PHONE_DISP}" required autocomplete="tel"></div></div>'
      '<label>Email</label><input name="email" type="email" placeholder="you@email.com" autocomplete="email">'
      f'<div class="frow"><div><label>City</label><select name="city">{city_opts}</select></div>'
      f'<div><label>Service Needed</label><select name="service">{svc_opts}</select></div></div>'
      '<label>Approx. square footage <span style="text-transform:none;font-weight:400;color:var(--muted)">(optional)</span></label><input name="sqft" placeholder="e.g. 1,200 sq ft">'
      '<label>Tell us about your project</label><textarea name="message" placeholder="Rooms, timeline, products you have in mind, current floor..."></textarea>'
      f'<label>How did you hear about us?</label><select name="found">{found_opts}</select>'
      '<button class="btn btn-primary" type="submit">Send My Request</button>'
      f'<p class="fine">Prefer WhatsApp? <a href="{wa_link()}" target="_blank" rel="noopener" style="color:var(--copper-dk);font-weight:700">Message us →</a> · We never spam.</p></form>')

# ── Recent project photos (real BVA installs; SEO/GEO/AEO filenames + alt) ───
# tuple: (service_slug, filename, alt_text, caption, city)
PROJECTS = [
 ("hardwood-flooring","hardwood-flooring-installation-bradenton-fl.jpg",
   "Solid hardwood floor installation in a Bradenton, FL home by BVA Flooring","Solid Hardwood Installation","Bradenton, FL"),
 ("hardwood-flooring","engineered-hardwood-flooring-lakewood-ranch-fl.jpg",
   "Engineered hardwood flooring installed in a Lakewood Ranch, FL living room","Engineered Hardwood","Lakewood Ranch, FL"),
 ("hardwood-flooring","hardwood-floor-installation-sarasota-fl.jpg",
   "Hardwood floor installation in a Sarasota, FL home by BVA Flooring","Hardwood Floor Install","Sarasota, FL"),
 ("vinyl-plank-flooring","luxury-vinyl-plank-flooring-sarasota-fl.jpg",
   "100% waterproof luxury vinyl plank flooring installed in a Sarasota, FL home","Luxury Vinyl Plank","Sarasota, FL"),
 ("vinyl-plank-flooring","waterproof-vinyl-plank-installation-tampa-fl.jpg",
   "Waterproof luxury vinyl plank flooring installation in Tampa, FL","Waterproof Vinyl Plank","Tampa, FL"),
 ("vinyl-plank-flooring","luxury-vinyl-plank-flooring-venice-fl.jpg",
   "Luxury vinyl plank (LVP) flooring in a Venice, FL home","Luxury Vinyl Plank","Venice, FL"),
 ("vinyl-plank-flooring","wood-look-vinyl-plank-flooring-st-petersburg-fl.jpg",
   "Wood-look luxury vinyl plank flooring in a St. Petersburg, FL room","Wood-Look Vinyl Plank","St. Petersburg, FL"),
 ("vinyl-plank-flooring","glue-down-vinyl-plank-flooring-palmetto-fl.jpg",
   "Glue-down luxury vinyl plank flooring installed in Palmetto, FL","Glue-Down Vinyl Plank","Palmetto, FL"),
 ("vinyl-plank-flooring","glue-down-luxury-vinyl-flooring-parrish-fl.jpg",
   "Glue-down luxury vinyl flooring in a Parrish, FL home","Glue-Down Luxury Vinyl","Parrish, FL"),
 ("stair-treads","vinyl-stair-tread-installation-bradenton-fl.jpg",
   "Vinyl stair tread installation on a staircase in Bradenton, FL","Vinyl Stair Treads","Bradenton, FL"),
 ("stair-treads","waterproof-vinyl-stair-treads-tampa-fl.jpg",
   "Waterproof vinyl stair treads installed in a Tampa, FL home","Vinyl Stair Treads","Tampa, FL"),
 ("stair-treads","vinyl-stair-tread-installation-lakewood-ranch-fl.jpg",
   "Vinyl stair tread and riser installation in Lakewood Ranch, FL","Vinyl Stair Treads","Lakewood Ranch, FL"),
]

def projects_gallery(slug=None, limit=None, heading=None, sub=None, bg=False):
    items=[p for p in PROJECTS if slug is None or p[0]==slug]
    if not items: return ""
    if limit: items=items[:limit]
    cards="".join(
      f'<figure class="proj"><img src="/images/projects/{f}" alt="{alt}" loading="lazy" decoding="async" width="800" height="600">'
      f'<figcaption><b>{cap}</b><span>{city}</span></figcaption></figure>'
      for _,f,alt,cap,city in items)
    h=heading or "Recent Flooring Projects Across Tampa Bay"
    s=sub or "Real installs from Bradenton to St. Petersburg — hardwood, waterproof luxury vinyl plank, and stair treads."
    style=' style="background:var(--sand)"' if bg else ''
    return (f'<section class="projsec"{style}><div class="wrap"><div class="shead">'
            f'<span class="eyebrow">Our Work</span><h2>{h}</h2><p>{s}</p></div>'
            f'<div class="projgrid">{cards}</div></div></section>')

def page_home():
    title=f"Flooring Installation Bradenton FL · Tampa Bay | {BRAND}"
    desc=("Flooring installation in Bradenton, Sarasota & Tampa Bay, FL — hardwood, waterproof "
          "vinyl plank, tile, laminate & stair treads. Licensed, insured, built for Florida "
          f"humidity. Free 24-hr estimate · {PHONE_DISP}.")
    svc_cards="".join(
        f'<a class="svc-card" href="/{s["slug"]}/"><div class="svc-ic">{s["icon"]}</div>'
        f'<h3>{s["name"]}</h3><p>{s["blurb"]}</p><span class="more">Explore {s["short"]} →</span></a>'
        for s in SERVICES)
    area_tags="".join(f'<a class="rel" href="/{slug}/"><b>{nm}, FL</b><span>Flooring installation &amp; repair</span></a>'
                      for slug,nm in AREAS)
    feats=[("01","One crew, start to finish","No revolving subcontractors. The team that measures your floor is the team that installs it — and the one you call after."),
           ("02","Built for Florida humidity","Documented moisture testing and a 48–72 hr acclimation window on every job. We install for the Gulf Coast, not a generic spec sheet."),
           ("03","Written, itemized pricing","Material, labor, prep, and haul-away in writing within 24 hours — so you can compare honestly and avoid mid-job upcharges."),
           ("04","A standard you can audit","Every floor passes the 52-Point Floor-Ready inspection before we call it done. New company, measurable quality.")]
    feat_html="".join(f'<div class="feat"><div class="n">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n,t,d in feats)
    home_faqs=[
     ("Where does BVA Flooring install?",
      "We install across Bradenton, Sarasota, Lakewood Ranch, Palmetto, Parrish, Venice, Tampa, and St. Petersburg — "
      "Manatee, Sarasota, Hillsborough, and Pinellas counties along the Gulf Coast."),
     ("Is BVA Flooring licensed and insured?",
      "Yes. BVA Services Corp is a licensed and insured flooring installer. We are locally owned and you deal directly with us — never a call center."),
     ("How fast can I get an estimate?",
      "Call, text, or WhatsApp and we return a free, written estimate within 24 hours. Measurements are free and there is no obligation."),
     ("What flooring is best for Florida homes?",
      "For most Gulf-Coast homes, waterproof luxury vinyl plank and engineered hardwood handle humidity best, with porcelain tile ideal for wet areas. We help you match the right product to each room — free."),
    ]
    faq_html, faq_schema = faq_block(home_faqs)
    schema=jsonld(sc_org(), sc_website(),
                  sc_localbiz("/","Flooring installation contractor serving Bradenton and Tampa Bay, FL — hardwood, luxury vinyl plank, tile, laminate, stair treads, and floor repair."),
                  sc_breadcrumb([("Home",None)]), faq_schema)
    return (head(title,desc,"/") + header() +
     f"""<section class="hero"><div class="hero-grid">
<div><span class="eyebrow" style="color:#E8C79A">Bradenton · Sarasota · Tampa Bay</span>
<h1>Flooring Installation in Bradenton, FL — <b>Done Right the First Time</b></h1>
<p class="hero-lead">Hardwood, luxury vinyl plank, tile, laminate, and stairs — installed for Florida humidity by one accountable local crew. Free, written estimate in 24 hours.</p>
<div class="hero-cta"><a href="/contact/#quote" class="btn btn-primary">Get My Free Quote</a>
<a href="tel:{PHONE_E164}" class="btn btn-ghost">{SVG_PHONE} {PHONE_DISP}</a></div>
<div class="hero-trust"><span>Licensed &amp; insured</span><span>{EXPERIENCE} experience</span><span>52-Point Standard</span><span>{STARS} workmanship</span></div></div>
<div class="ecard"><h3>Free Flooring Estimate</h3><p class="sub">No obligation · reply within 24 hours</p>
{quote_form(compact=True)}</div></div></section>

<div class="proof"><div class="wrap"><div class="proof-row">
<div><b class="cu">52-Point</b>Floor-Ready Standard</div>
<div><b>{EXPERIENCE}</b>Gulf Coast experience</div>
<div><b>24 hr</b>Free written estimate</div>
<div><b>8 cities</b>Across Tampa Bay</div>
<div><b class="cu">{STARS}</b>Workmanship pledge</div>
</div></div></div>

<section><div class="wrap"><div class="shead"><span class="eyebrow">What We Install</span>
<h2>Flooring Services Across Tampa Bay</h2><p>Six core services, one standard of work. Click any service for pricing, scope, and our full process.</p></div>
<div class="svc-grid">{svc_cards}</div></div></section>

{projects_gallery(limit=8, bg=True)}

<section class="intro"><div class="wrap"><div class="shead"><span class="eyebrow">Why BVA</span>
<h2>A New Name, Built on an Old-School Standard</h2><p>BVA is a young company on purpose — lean, local, and obsessive about the parts other installers skip.</p></div>
<div class="feat-grid">{feat_html}</div></div></section>

<section><div class="wrap"><div class="shead"><span class="eyebrow">Service Areas</span>
<h2>Serving 8 Cities Across the Gulf Coast</h2><p>From the Manatee River to Tampa Bay — local crews who know the homes, the HOAs, and the humidity.</p></div>
<div class="rel-grid">{area_tags}</div></div></section>

{checklist_section()}

<section class="faqs"><div class="wrap"><div class="shead"><span class="eyebrow">FAQ</span><h2>Common Questions</h2></div>{faq_html}</div></section>

{wa_banner()}
{final_cta()}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_service_index(svc):
    s=SVC_DATA[svc["slug"]]
    title=f"{svc['name']} Bradenton & Tampa Bay FL | {BRAND}"
    desc=(f"{svc['short']} installation in Bradenton, Sarasota & Tampa Bay, FL. "
          f"Transparent pricing, 52-point standard, licensed & insured. Free 24-hr estimate — {PHONE_DISP}.")[:158]
    bc=[("Home","/"),("Services","/hardwood-flooring/"),(svc['name'],None)]
    faqs=svc_city_faqs(svc, "Tampa Bay")
    faq_html,faq_schema=faq_block(faqs)
    city_links="".join(
        (f'<a class="rel" href="/{svc["slug"]}/bradenton/"><b>{nm}</b><span>{svc["short"]} in {nm}, FL</span></a>'
         if slug=="bradenton" else
         f'<a class="rel" href="/{slug}/"><b>{nm}</b><span>{svc["short"]} in {nm}, FL</span></a>')
        for slug,nm in AREAS)
    schema=jsonld(sc_localbiz(f"/{svc['slug']}/", f"{svc['name']} installation across Bradenton and Tampa Bay, FL.", suffix=svc['short']),
                  sc_breadcrumb(bc), faq_schema)
    return (head(title,desc,f"/{svc['slug']}/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">{svc['name']}</span>
<h1>{svc['name']} in <b>Bradenton &amp; Tampa Bay</b></h1>
<p>{s['intro']}</p>
<div class="phero-trust"><span>Licensed &amp; insured</span><span>52-Point Standard</span><span>Free 24-hr estimate</span></div></div></section>
<section class="intro"><div class="wrap"><div class="prose">
<p><strong>{BRAND}</strong> installs {svc['short'].lower()} the way it should be done on the Gulf Coast: moisture-tested, acclimated, and finished by one accountable crew. Below you'll find transparent pricing and the exact scope we cover — then pick your city for local detail.</p></div></div></section>
{included_section(svc)}
{price_table(svc, "Tampa Bay")}
{projects_gallery(slug=svc['slug'], heading=f"Recent {svc['name']} Projects in Tampa Bay", bg=True)}
{checklist_section()}
<section><div class="wrap"><div class="shead"><span class="eyebrow">Choose Your City</span>
<h2>{svc['name']} Near You</h2><p>Local pages with neighborhood-level detail and city-specific pricing.</p></div>
<div class="rel-grid">{city_links}</div></div></section>
<section class="faqs"><div class="wrap"><div class="shead"><span class="eyebrow">FAQ</span><h2>{svc['short']} Questions</h2></div>{faq_html}</div></section>
{wa_banner()}
{final_cta()}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_service_city(svc, city_slug):
    c=CITIES[city_slug]; city=c["name"]; s=SVC_DATA[svc["slug"]]
    title=f"{svc['short']} {city} FL | {BRAND} · Free Estimate"
    desc=(f"{svc['name']} in {city}, FL — {', '.join(c['hoods'][:3])} & all of {c['county']}. "
          f"Transparent pricing, moisture-tested installs, licensed & insured. Free estimate {PHONE_DISP}.")[:158]
    bc=[("Home","/"),(svc['name'],f"/{svc['slug']}/"),(city,None)]
    faqs=svc_city_faqs(svc, city)
    faq_html,faq_schema=faq_block(faqs)
    hoods="".join(f'<span>{h}</span>' for h in c["hoods"])
    zips="".join(f'<span>{z}</span>' for z in c["zips"])
    related_cards="".join(f'<a class="rel" href="/{o["slug"]}/bradenton/"><b>{o["short"]} in {city}</b><span>See pricing &amp; scope →</span></a>'
                          for o in SERVICES if o["slug"]!=svc["slug"])
    schema=jsonld(sc_localbiz(f"/{svc['slug']}/{city_slug}/",
                    f"{svc['name']} in {city}, FL by {BRAND}. {s['intro'][:120]}", city=city, suffix=f"{svc['short']} {city}"),
                  sc_breadcrumb(bc), faq_schema)
    return (head(title,desc,f"/{svc['slug']}/{city_slug}/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">{svc['name']} · {city}, FL</span>
<h1>{svc['short']} in <b>{city}, FL</b> — Florida-Tough, Done Once</h1>
<p>Moisture-tested, acclimated, and finished by one local crew across {c['county']}. Free written estimate in 24 hours.</p>
<div class="phero-trust"><span>Licensed &amp; insured</span><span>{EXPERIENCE} experience</span><span>52-Point Standard</span></div></div></section>
<section class="intro"><div class="wrap"><div class="prose">
<p>{c['intro']}</p>
<p>{s['intro']} In {city}, that matters near {c['landmarks']} — where older slabs, waterfront moisture, and new-build concrete all behave differently. <strong>{BRAND}</strong> installs {svc['short'].lower()} for those real conditions, not a generic national spec.</p>
<p>From <strong>{c['hoods'][0]}</strong> and <strong>{c['hoods'][1]}</strong> to <strong>{c['hoods'][2]}</strong> and beyond, every {city} job runs through our {STANDARD} — documented moisture readings, a 48–72 hour acclimation window, and a written workmanship warranty when we're done.</p></div></div></section>
{included_section(svc)}
{price_table(svc, city)}
{checklist_section()}
<section class="neighborhoods" style="background:var(--sand);padding:4.2rem 0"><div class="wrap"><div class="shead">
<span class="eyebrow">{city} Coverage</span><h2>Neighborhoods &amp; Communities We Serve in {city}</h2>
<p>From {c['hoods'][0]} to {c['hoods'][-1]} — and every street in between across {c['county']}.</p></div>
<div class="nbhd">{hoods}</div><div class="zips">{zips}</div></div></section>
<section class="faqs"><div class="wrap"><div class="shead"><span class="eyebrow">FAQ</span>
<h2>{svc['short']} in {city} — Your Questions</h2></div>{faq_html}</div></section>
<section><div class="wrap"><div class="shead"><span class="eyebrow">More in {city}</span>
<h2>Other Flooring Services in {city}</h2></div><div class="rel-grid">{related_cards}</div></div></section>
{wa_banner()}
{final_cta(f"Serving every neighborhood in {city} and across {c['county']}. Free measurement, locked-in pricing, written warranty.")}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_city_hub(city_slug):
    c=CITIES[city_slug]; city=c["name"]
    title=f"Flooring {city} FL | Hardwood, Vinyl, Tile · {BRAND}"
    desc=(f"Flooring installation in {city}, FL — hardwood, luxury vinyl plank, tile, laminate & stairs across "
          f"{c['county']}. Licensed, insured, free 24-hr estimate. {PHONE_DISP}.")[:158]
    bc=[("Home","/"),("Service Areas","/bradenton/"),(city,None)]
    svc_cards="".join(
        f'<a class="svc-card" href="/{s["slug"]}/{city_slug}/"><div class="svc-ic">{s["icon"]}</div>'
        f'<h3>{s["name"]} in {city}</h3><p>{s["blurb"]}</p><span class="more">View {s["short"]} in {city} →</span></a>'
        for s in SERVICES)
    hoods="".join(f'<span>{h}</span>' for h in c["hoods"])
    zips="".join(f'<span>{z}</span>' for z in c["zips"])
    faqs=[
     (f"What flooring services do you offer in {city}?",
      f"All six of our core services in {city}: hardwood, luxury vinyl plank, tile, laminate, stair treads, and floor repair — "
      f"installed across {c['county']} and backed by our 52-Point Floor-Ready Standard."),
     (f"Do you give free estimates in {city}?",
      f"Yes. Free, no-obligation, written estimates within 24 hours anywhere in {city}. Call, text, or WhatsApp {PHONE_DISP}."),
     (f"Which {city} neighborhoods do you serve?",
      f"All of them — from {c['hoods'][0]} and {c['hoods'][1]} to {c['hoods'][-1]}, covering ZIP codes {', '.join(c['zips'][:5])} and more."),
     (f"Why pick a newer company for my {city} floors?",
      f"Because we compete on craft, not coasting on a name. {EXPERIENCE} of Gulf Coast experience, one accountable crew, "
      f"a measurable 52-point standard, and a written warranty. You deal directly with us."),
    ]
    faq_html,faq_schema=faq_block(faqs)
    schema=jsonld(sc_localbiz(f"/{city_slug}/",
                    f"Flooring installation in {city}, FL — hardwood, vinyl plank, tile, laminate, stairs, and repair across {c['county']}.",
                    city=city, suffix=city),
                  sc_breadcrumb(bc), faq_schema)
    return (head(title,desc,f"/{city_slug}/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">{city}, {STATE} · {c['county']}</span>
<h1>Flooring Installation in <b>{city}, FL</b></h1>
<p>Hardwood, luxury vinyl plank, tile, laminate, and stairs — installed for Gulf-Coast humidity by one accountable local crew. Free written estimate in 24 hours.</p>
<div class="phero-trust"><span>Licensed &amp; insured</span><span>{EXPERIENCE} experience</span><span>52-Point Standard</span></div></div></section>
<section class="intro"><div class="wrap"><div class="prose">
<p>{c['intro']}</p>
<p><strong>{BRAND}</strong> serves all of {city} and {c['county']} — near {c['landmarks']}. Pick a service below for {city}-specific pricing, scope, and our full installation process.</p></div></div></section>
<section><div class="wrap"><div class="shead"><span class="eyebrow">{city} Services</span>
<h2>What We Install in {city}</h2></div><div class="svc-grid">{svc_cards}</div></div></section>
<section class="neighborhoods" style="background:var(--sand);padding:4.2rem 0"><div class="wrap"><div class="shead">
<span class="eyebrow">{city} Coverage</span><h2>{city} Neighborhoods We Serve</h2></div>
<div class="nbhd">{hoods}</div><div class="zips">{zips}</div></div></section>
{checklist_section()}
<section class="faqs"><div class="wrap"><div class="shead"><span class="eyebrow">FAQ</span><h2>{city} Flooring Questions</h2></div>{faq_html}</div></section>
{wa_banner()}
{final_cta(f"Serving every neighborhood in {city} and across {c['county']}. Free measurement, locked-in pricing, written warranty.")}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_about():
    title=f"About {BRAND} | Local Flooring Installers, Bradenton FL"
    desc=(f"BVA Services Corp is a licensed, insured flooring installer serving Bradenton & Tampa Bay. "
          f"{EXPERIENCE} of Gulf Coast experience, one accountable crew, a measurable 52-point standard.")[:158]
    bc=[("Home","/"),("About",None)]
    vals=[("Accountability","One crew, one point of contact, one name on the warranty. You always know who installed your floor and who to call."),
          ("Craft over speed","We would rather schedule the acclimation window than rush a floor that fails in a year. The boring steps are the whole job."),
          ("Honest pricing","Itemized, written quotes. No 'call for pricing,' no surprise subfloor upcharges mid-project."),
          ("Built for Florida","Every install is moisture-tested and acclimated for Gulf-Coast humidity — because a national spec sheet doesn't know Bradenton in August.")]
    val_html="".join(f'<div class="feat"><h3>{t}</h3><p>{d}</p></div>' for t,d in vals)
    schema=jsonld({"@context":"https://schema.org","@type":"AboutPage","url":f"https://{DOMAIN}/about/",
                   "name":f"About {BRAND}","isPartOf":{"@id":f"https://{DOMAIN}/#website"},
                   "about":{"@id":f"https://{DOMAIN}/#organization"}},
                  sc_org(), sc_breadcrumb(bc))
    return (head(title,desc,"/about/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">About Us</span>
<h1>Meet <b>{BRAND}</b></h1><p>A local, licensed flooring company built on one idea: the parts most installers skip are exactly the parts that make a floor last.</p>
<div class="phero-trust"><span>Licensed &amp; insured</span><span>{EXPERIENCE} experience</span><span>Locally owned</span></div></div></section>
<section class="intro"><div class="wrap"><div class="prose">
<p><strong>{LEGAL}</strong> — operating as {BRAND} — installs floors across Bradenton, Sarasota, Lakewood Ranch, and the wider Tampa Bay Gulf Coast. We're a newer company, and we treat that as an advantage: small enough that the owner is on your job, focused enough to do the unglamorous steps right.</p>
<p>Behind BVA is <strong>{EXPERIENCE} of hands-on Gulf Coast flooring experience</strong>. That experience taught us a simple lesson — almost every flooring failure in Florida traces back to moisture and prep, not the product. So we built our whole process around it: documented moisture testing, real acclimation, flat subfloors, and a {STANDARD} that every single job has to pass before we call it finished.</p>
<p>We're licensed, insured, and locally owned. When you hire BVA, you're not getting a rotating cast of subcontractors and a corporate hotline — you're getting one crew, one standard, and one name on the written warranty.</p>{stat_badge()}</div></div></section>
<section style="background:var(--sand)"><div class="wrap"><div class="shead"><span class="eyebrow">What We Stand For</span>
<h2>How We Work</h2></div><div class="feat-grid">{val_html}</div></div></section>
{checklist_section()}
{wa_banner()}
{final_cta()}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_contact():
    title=f"Contact {BRAND} | Free Flooring Estimate · Bradenton FL"
    desc=(f"Get a free flooring estimate from BVA Flooring in 24 hours. Call, text, or WhatsApp {PHONE_DISP}. "
          f"Serving Bradenton, Sarasota & Tampa Bay, FL.")[:158]
    bc=[("Home","/"),("Contact",None)]
    city_opts=''.join(f'<option>{nm}</option>' for _,nm in AREAS)
    schema=jsonld({"@context":"https://schema.org","@type":"ContactPage","url":f"https://{DOMAIN}/contact/",
                   "name":f"Contact {BRAND}","isPartOf":{"@id":f"https://{DOMAIN}/#website"}},
                  sc_localbiz("/contact/", f"Contact {BRAND} for a free flooring estimate in Bradenton and Tampa Bay, FL."),
                  sc_breadcrumb(bc))
    return (head(title,desc,"/contact/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">Contact</span>
<h1>Get Your <b>Free Estimate</b></h1><p>Call, text, or WhatsApp — we reply within 24 hours, 7 days a week. Free measurement, no obligation.</p></div></section>
<section class="intro"><div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;max-width:1000px;align-items:start">
<div class="ecard" id="quote" style="box-shadow:var(--sh-lg)"><h3>Request a Free Quote</h3><p class="sub">Reply within 24 hours · no obligation</p>
{quote_form(compact=False)}</div>
<div><h2 style="margin-bottom:1rem">Talk to a Real Person</h2>
<p style="color:var(--muted)">No call centers, no phone trees. You reach the people who actually install your floor.</p>
<div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.4rem">
<a href="tel:{PHONE_E164}" class="btn btn-ink" style="justify-content:flex-start">{SVG_PHONE} Call {PHONE_DISP}</a>
<a href="{wa_link()}" target="_blank" rel="noopener" class="btn btn-primary" style="justify-content:flex-start">{SVG_WA} WhatsApp Us</a>
<a href="mailto:{EMAIL}" class="btn btn-outline" style="justify-content:flex-start">✉ {EMAIL}</a></div>
<div style="margin-top:1.8rem;padding:1.4rem;background:var(--sand);border-radius:14px">
<p style="margin:0 0 .5rem"><strong>Hours:</strong> Mon–Sat · 7 AM – 7 PM</p>
<p style="margin:0 0 .5rem"><strong>Service area:</strong> Bradenton, Sarasota, Lakewood Ranch, Palmetto, Parrish, Venice, Tampa &amp; St. Petersburg</p>
<p style="margin:0"><strong>Licensed &amp; insured</strong> · {LEGAL}</p></div></div></div></section>
{wa_banner()}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_404():
    return (head("Page Not Found | "+BRAND, "The page you're looking for moved or doesn't exist. Find flooring services across Bradenton & Tampa Bay.","/404.html") + header() +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">404</span>
<h1>That Page <b>Slipped a Plank</b></h1><p>The page you're looking for moved or never existed. Let's get you back on solid ground.</p>
<div class="fcta-btns" style="margin-top:1.4rem"><a href="/" class="btn btn-primary">Back to Home</a>
<a href="tel:{PHONE_E164}" class="btn btn-ghost">{SVG_PHONE} {PHONE_DISP}</a></div></div></section>
<section><div class="wrap"><div class="shead"><h2>Popular Pages</h2></div>
<div class="rel-grid">
<a class="rel" href="/hardwood-flooring/"><b>Hardwood Flooring</b><span>Engineered &amp; solid</span></a>
<a class="rel" href="/vinyl-plank-flooring/"><b>Luxury Vinyl Plank</b><span>Waterproof LVP/SPC</span></a>
<a class="rel" href="/tile-installation/"><b>Tile Installation</b><span>Porcelain &amp; large-format</span></a>
<a class="rel" href="/bradenton/"><b>Bradenton, FL</b><span>All services</span></a>
</div></div></section>
{footer()}{wa_float()}{MENU_JS}</body></html>""")

# ── Thanks page ─────────────────────────────────────────────────────────────
def page_thanks():
    return (head(f"Thank You | {BRAND}", "Thanks for reaching out to BVA Flooring. We'll reply within 24 hours with your free estimate.","/thanks/") + header() +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">Request Received</span>
<h1>Thanks — <b>We're On It</b></h1><p>Your request reached the BVA Flooring team. We'll get back to you within 24 hours with next steps. Need us sooner? Call or WhatsApp now.</p>
<div class="fcta-btns" style="margin-top:1.4rem"><a href="tel:{PHONE_E164}" class="btn btn-primary">{SVG_PHONE} {PHONE_DISP}</a>
<a href="{wa_link()}" target="_blank" rel="noopener" class="btn btn-ghost">{SVG_WA} WhatsApp Us</a></div></div></section>
<section><div class="wrap"><div class="shead"><h2>While You Wait</h2></div><div class="rel-grid">
<a class="rel" href="/blog/"><b>Flooring Cost Guides</b><span>2026 prices &amp; tips →</span></a>
<a class="rel" href="/hardwood-flooring/"><b>Our Services</b><span>See scope &amp; pricing →</span></a>
<a class="rel" href="/about/"><b>About BVA</b><span>How we work →</span></a>
</div></div></section>
{footer()}{wa_float()}{MENU_JS}</body></html>""")

# ── Blog ────────────────────────────────────────────────────────────────────
AUTHOR="The BVA Flooring Team"
BLOG_POSTS=[
 {"slug":"vinyl-plank-flooring-cost-bradenton","emoji":"🧱","cat":"Cost Guide","read":"8 min",
  "date":"2026-05-12","mod":"2026-06-05",
  "title":"How Much Does Vinyl Plank Flooring Cost in Bradenton, FL? (2026)",
  "h1":"How Much Does Vinyl Plank Flooring Cost in Bradenton, FL? (2026 Guide)",
  "dek":"Real installed prices for luxury vinyl plank in Bradenton and Tampa Bay — what drives the number, where homeowners overpay, and how to get an honest quote.",
  "links":[("Luxury Vinyl Plank service","/vinyl-plank-flooring/"),("LVP in Bradenton","/vinyl-plank-flooring/bradenton/"),("Get a free estimate","/contact/")],
  "body":[
   ("The short answer",
    "<p>In Bradenton, most luxury vinyl plank (LVP) projects in 2026 run <strong>$5 to $9 per square foot installed</strong>, materials and labor combined. A typical 1,000 sq ft job therefore lands somewhere between <strong>$5,000 and $9,000</strong> — with the final number driven mostly by the plank you choose and how much subfloor prep your home needs.</p><p>That's a wide range on purpose. Anyone who quotes you an exact price over the phone, sight unseen, is guessing. The honest version is a written, itemized estimate after a free measurement — which is exactly how we quote every BVA job.</p>"),
   ("What you're actually paying for",
    "<p>LVP pricing breaks down into four parts: the plank itself, the labor to install it, subfloor prep, and the extras (transitions, trim, tear-out, haul-away). Here's how each moves the number.</p>"
    "<p><strong>The plank ($2.50–$5/sq ft material):</strong> Thicker rigid-core SPC with a heavier wear layer (12–20 mil) costs more and lasts longer — the right call for pets, rentals, and busy households. Thin floating LVP is cheaper but dents and telegraphs subfloor flaws.</p>"
    "<p><strong>Labor ($2.50–$4/sq ft):</strong> Straight rooms with simple layouts cost less; lots of doorways, closets, angles, and stairs cost more because they're slower and waste more material.</p>"
    "<p><strong>Subfloor prep ($1–$3/sq ft when needed):</strong> Rigid-core LVP is unforgiving — it shows every bump. If your slab isn't flat, it needs leveling first. Skipping this is the #1 reason cheap LVP jobs fail.</p>"
    "<p><strong>Extras:</strong> Removing old flooring, hauling it away, new baseboards or quarter-round, and transition strips all add up. A good quote lists them so there are no surprises mid-job.</p>"),
   ("Why Bradenton homes need extra care",
    "<p>Bradenton sits between the Gulf and the Manatee River, and the humidity here is no joke. LVP is waterproof, so the plank itself shrugs off moisture — but the subfloor underneath does not. A damp slab that isn't tested and sealed can grow mold under a perfectly waterproof floor, and trapped moisture can break down adhesives over time.</p><p>This is why every BVA install includes documented moisture testing and the right vapor strategy before we lay a single plank. It's the boring step that separates a floor that lasts 20 years from one that fails in two.</p>"),
   ("Where homeowners overpay (and underpay)",
    "<p><strong>Overpaying:</strong> Buying premium plank for low-traffic guest rooms, or paying big-box markup on installation that's then subcontracted to the lowest bidder anyway.</p><p><strong>Underpaying (the expensive kind):</strong> Taking the cheapest quote that skips subfloor prep and acclimation. We've been hired to rip out and redo more than a few 'bargain' floors that buckled within 18 months. The redo always costs more than doing it right once.</p>"),
   ("How to get an honest number",
    "<p>Get at least two written, itemized estimates after an in-home measurement. Compare the line items, not just the bottom line — look for who includes subfloor prep, moisture testing, tear-out, and a written warranty. The cheapest top-line price often hides the most expensive omissions.</p>"),
  ],
  "faqs":[
   ("Is vinyl plank cheaper than tile or hardwood in Bradenton?","Generally yes. Installed LVP ($5–$9/sq ft) typically costs less than porcelain tile ($9–$15/sq ft) or hardwood ($9–$18/sq ft), while still being waterproof and durable — which is why it's the most popular floor in Tampa Bay homes and rentals."),
   ("How long does LVP installation take?","A typical Bradenton room or two is usually 1–2 days. Whole-home jobs take longer, especially if the subfloor needs leveling. We give you a firm timeline with your written estimate."),
   ("Does vinyl plank add value to a Florida home?","Quality, professionally installed LVP is a strong selling point in Florida because buyers know it's waterproof and low-maintenance. Cheap, visibly failing LVP does the opposite — installation quality is what protects the value."),
   ("Can you install LVP over my existing tile?","Often yes, if the tile is sound and flat. Rigid-core LVP can sometimes float over existing hard floors with the right prep, saving tear-out cost. We'll tell you honestly after measuring whether that's a good idea in your home."),
  ]},
 {"slug":"hardwood-vs-vinyl-plank-florida","emoji":"🪵","cat":"Comparison","read":"9 min",
  "date":"2026-05-24","mod":"2026-06-06",
  "title":"Hardwood vs. Vinyl Plank in Florida: Which Lasts Longer in the Humidity?",
  "h1":"Hardwood vs. Vinyl Plank in Florida: Which One Actually Lasts?",
  "dek":"The honest trade-offs between hardwood and luxury vinyl plank for Gulf-Coast homes — moisture, value, looks, and which one we'd pick for each room.",
  "links":[("Hardwood Flooring","/hardwood-flooring/"),("Luxury Vinyl Plank","/vinyl-plank-flooring/"),("Talk to BVA","/contact/")],
  "body":[
   ("The Florida-specific answer",
    "<p>In a perfect, climate-controlled vacuum, real hardwood wins on character and resale. In a real Florida home — with humidity swings, the occasional leak, sandy feet, and AC that gets turned off when you travel — <strong>luxury vinyl plank is the safer, lower-stress choice for most rooms</strong>. Hardwood still has its place; it just needs the right room and the right installer.</p>"),
   ("Moisture: the deciding factor",
    "<p>Gulf-Coast humidity runs 70–85% outdoors against the 45–55% your AC holds inside. Solid hardwood reacts to that swing — it expands and contracts, and over time can cup, gap, or crown if it wasn't acclimated and moisture-tested before install.</p><p>Engineered hardwood (a real-wood top layer over a stable plywood core) handles humidity far better than solid and is the version we recommend for almost every Florida hardwood job. Luxury vinyl plank, being 100% waterproof, sidesteps the moisture problem entirely at the plank level — which is why it dominates Florida rentals and family homes.</p>"),
   ("Durability and daily life",
    "<p>LVP resists scratches, dents, spills, and pets better than hardwood, and it never needs refinishing. Hardwood scratches more easily but has a trump card: it can be sanded and refinished multiple times over decades, so a worn hardwood floor can be made new again, while worn LVP must be replaced.</p><p>So the real question is lifespan strategy: LVP is lower-maintenance and more forgiving day to day; hardwood is renewable and can outlive LVP if you're willing to maintain and occasionally refinish it.</p>"),
   ("Looks and resale value",
    "<p>High-end LVP looks remarkably convincing now, but true hardwood still reads as more premium underfoot and in listings. In higher-end neighborhoods — think Lakewood Ranch's Lake Club or Sarasota's West of Trail homes — real engineered hardwood in living areas can support resale value. In rentals, second homes, and busy family spaces, quality LVP is the smarter spend.</p>"),
   ("What we'd actually install, room by room",
    "<p><strong>Living/dining/bedrooms (owner-occupied, higher-end):</strong> engineered hardwood for warmth and resale.<br><strong>Whole-home rentals &amp; second homes:</strong> rigid-core LVP for worry-free durability.<br><strong>Kitchens, laundry, near sliders &amp; bathrooms:</strong> LVP or tile — never solid hardwood.<br><strong>High-traffic family homes with pets/kids:</strong> LVP almost every time.</p><p>Most Florida homes end up with a smart mix, and a good installer helps you decide per room instead of pushing one product everywhere.</p>"),
  ],
  "faqs":[
   ("Will hardwood floors ruin in a Florida home?","Not if they're the right type and installed correctly. Engineered hardwood, properly acclimated and moisture-tested, performs well in Florida. Solid hardwood is riskier in wet areas and homes that aren't consistently climate-controlled."),
   ("Is vinyl plank 'cheaper looking' than hardwood?","Entry-level LVP can look flat, but premium rigid-core planks with realistic embossing and varied tones look excellent. The gap between good LVP and real wood is much smaller than it was five years ago."),
   ("Which is better for resale in Tampa Bay?","In higher-end homes, real engineered hardwood in main living areas tends to help resale. In mid-market homes and rentals, quality LVP is widely accepted and often preferred for being waterproof."),
   ("Can I mix hardwood and LVP in the same house?","Yes — and many Florida homes do. Hardwood in the dry living areas, LVP or tile in kitchens, baths, and laundry is a common, smart combination. We can match tones and use clean transitions between them."),
  ]},
 {"slug":"best-flooring-for-florida-homes","emoji":"🏠","cat":"Buyer's Guide","read":"10 min",
  "date":"2026-06-02","mod":"2026-06-07",
  "title":"The Best Flooring for Florida Homes: A Room-by-Room Guide (2026)",
  "h1":"The Best Flooring for Florida Homes: A Room-by-Room Guide (2026)",
  "dek":"Humidity, sand, sun, and the occasional storm — here's how to choose flooring that survives the Gulf Coast, one room at a time.",
  "links":[("All our services","/hardwood-flooring/"),("Tile Installation","/tile-installation/"),("Serving Bradenton","/bradenton/"),("Free estimate","/contact/")],
  "body":[
   ("Start with the Florida problem",
    "<p>Choosing flooring in Florida isn't like choosing it up north. Here, three forces work against your floor: <strong>humidity</strong> (constant, and brutal in summer), <strong>water</strong> (storms, leaks, and homes that sit closed up), and <strong>grit</strong> (sand tracked in from the Gulf acts like sandpaper). The best floor for any room is the one that handles those three for that room's specific use.</p>"),
   ("Living rooms & bedrooms",
    "<p>These dry, lower-moisture spaces give you the most freedom. <strong>Engineered hardwood</strong> brings warmth and resale value; <strong>luxury vinyl plank</strong> brings worry-free durability. For owner-occupied higher-end homes, hardwood shines. For rentals, second homes, and pet-heavy households, LVP wins. Laminate (AC4/AC5) is a solid budget alternative that looks great when the seams are done right.</p>"),
   ("Kitchens & laundry rooms",
    "<p>Water and spills rule here. Skip solid hardwood. <strong>Luxury vinyl plank</strong> and <strong>porcelain tile</strong> are the two right answers — both waterproof, both tough. LVP is warmer and quieter underfoot; tile is the most bulletproof against standing water and lasts decades if it's set flat and sealed properly.</p>"),
   ("Bathrooms",
    "<p>This is tile country. <strong>Porcelain tile</strong> with proper waterproofing under it is the gold standard for Florida bathrooms — especially showers, where a waterproof membrane and full mortar coverage are what prevent leaks behind the wall. LVP works in half-baths and powder rooms, but full bathrooms with showers should be tile, done by someone who waterproofs correctly.</p>"),
   ("Lanais, sunrooms & entryways",
    "<p>These transition zones see the most moisture and grit. <strong>Porcelain tile</strong> is ideal — it handles tracked-in sand, humidity, and the occasional blowing rain. Large-format tile with tight, even grout lines looks high-end and cleans easily.</p>"),
   ("Stairs",
    "<p>Carpet on Florida stairs traps humidity and wears fast. <strong>Solid wood treads</strong> — matched to your main floor — are the durable, premium upgrade. They're precision work, not plank-laying, so they're worth hiring out to someone who does them regularly.</p>"),
   ("The step that matters more than the product",
    "<p>Here's the secret most flooring ads won't tell you: in Florida, <em>installation matters more than the product</em>. The best plank in the world fails over an untested damp slab or an uneven subfloor. Whatever you choose, insist on documented moisture testing, real acclimation, and proper subfloor prep. That's the whole reason we built our 52-Point Floor-Ready Standard around those steps.</p>"),
  ],
  "faqs":[
   ("What is the most popular flooring in Florida right now?","Luxury vinyl plank, by a wide margin, because it's waterproof, durable, and affordable. Porcelain tile remains the top pick for wet areas, and engineered hardwood leads in higher-end living spaces."),
   ("What flooring should I avoid in Florida?","Solid hardwood in wet areas (kitchens, baths, near sliders) and carpet in high-humidity or high-traffic zones. Cheap thin laminate without proper underlayment also tends to fail in Florida moisture."),
   ("Is tile or vinyl plank better for Florida?","Both are waterproof. Tile is the most durable and best for bathrooms, lanais, and high-water areas; LVP is warmer, quieter, faster to install, and great everywhere else. Many homes use both."),
   ("Do I really need moisture testing if my floor is waterproof?","Yes. Even waterproof flooring sits on a subfloor that can hold or transmit moisture. Testing protects against mold, adhesive failure, and trapped moisture under the floor — it's about what's underneath, not the surface."),
  ]},
]
POSTS_BY_SLUG={p["slug"]:p for p in BLOG_POSTS}

# Merge auto-generated posts (automation/posts/*.json) so the build includes them.
import os as _os, glob as _glob, json as _json
_AUTO=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),"automation","posts")
for _f in sorted(_glob.glob(_os.path.join(_AUTO,"*.json"))):
    try:
        _p=_json.load(open(_f,encoding="utf-8"))
        _p.setdefault("emoji","📝"); _p.setdefault("read","8 min"); _p.setdefault("cat","Guide")
        _p.setdefault("mod",_p.get("date","2026-01-01")); _p.setdefault("h1",_p.get("title",""))
        if _p.get("slug") and _p["slug"] not in POSTS_BY_SLUG:
            BLOG_POSTS.append(_p); POSTS_BY_SLUG[_p["slug"]]=_p
    except Exception as _e:
        print("  ! skipped auto post",_f,_e)
BLOG_POSTS.sort(key=lambda x:x.get("date",""), reverse=True)  # newest first

def _fmt_date(iso):
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y,m,d=iso.split("-"); return f"{months[int(m)-1]} {int(d)}, {y}"

def page_blog_index():
    title=f"Flooring Blog | Cost Guides & Tips · {BRAND}"
    desc=("Florida flooring cost guides, hardwood vs vinyl comparisons, and room-by-room buying tips from BVA "
          "Flooring — Bradenton & Tampa Bay.")[:158]
    bc=[("Home","/"),("Blog",None)]
    cards="".join(
        f'<a class="svc-card" href="/blog/{p["slug"]}/"><div class="svc-ic">{p["emoji"]}</div>'
        f'<span class="more" style="color:var(--copper-dk)">{p["cat"]} · {p["read"]}</span>'
        f'<h3 style="margin:.4rem 0 .5rem">{p["title"]}</h3><p>{p["dek"]}</p>'
        f'<span class="more">Read guide →</span></a>' for p in BLOG_POSTS)
    schema=jsonld({"@context":"https://schema.org","@type":"Blog","@id":f"https://{DOMAIN}/blog/#blog",
                   "name":f"{BRAND} Blog","url":f"https://{DOMAIN}/blog/","publisher":{"@id":f"https://{DOMAIN}/#organization"},
                   "blogPost":[{"@type":"BlogPosting","headline":p["title"],"url":f"https://{DOMAIN}/blog/{p['slug']}/","datePublished":p["date"]} for p in BLOG_POSTS]},
                  sc_breadcrumb(bc))
    return (head(title,desc,"/blog/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap"><span class="eyebrow">BVA Flooring Blog</span>
<h1>Florida Flooring, <b>Explained</b></h1><p>Straight answers on cost, materials, and what actually lasts on the Gulf Coast — no fluff, no sales spin.</p></div></section>
<section><div class="wrap"><div class="svc-grid">{cards}</div></div></section>
{wa_banner()}
{final_cta()}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

def page_blog_post(p):
    title=(f"{p['title']} | {BRAND}")[:65] if len(f"{p['title']} | {BRAND}")<=65 else p['title'][:62]
    desc=p["dek"][:158]
    bc=[("Home","/"),("Blog","/blog/"),(p["cat"],None)]
    body="".join(f'<h2>{h}</h2>{html}' for h,html in p["body"])
    faq_html,faq_schema=faq_block(p["faqs"])
    links="".join(f'<a class="rel" href="{u}"><b>{l}</b><span>→</span></a>' for l,u in p["links"])
    words=len(re.sub(r'<[^>]+>',' ',body+ " ".join(q+a for q,a in p["faqs"])).split())
    article={"@context":"https://schema.org","@type":"Article","@id":f"https://{DOMAIN}/blog/{p['slug']}/#article",
        "headline":p["title"],"description":p["dek"],"image":[f"https://{DOMAIN}/images/og-default.jpg"],
        "datePublished":p["date"],"dateModified":p["mod"],
        "author":{"@type":"Organization","name":BRAND,"url":f"https://{DOMAIN}/about/"},
        "publisher":{"@type":"Organization","name":LEGAL,"logo":{"@type":"ImageObject","url":f"https://{DOMAIN}/images/logo.svg"}},
        "mainEntityOfPage":{"@type":"WebPage","@id":f"https://{DOMAIN}/blog/{p['slug']}/"},
        "articleSection":p["cat"],"wordCount":words,"inLanguage":"en-US"}
    schema=jsonld(article, faq_schema, sc_breadcrumb(bc))
    return (head(title,desc,f"/blog/{p['slug']}/") + header() + crumbs(bc) +
     f"""<section class="phero"><div class="wrap" style="max-width:840px"><span class="eyebrow">{p['cat']} · {p['read']} read</span>
<h1 style="font-size:clamp(1.9rem,4.4vw,2.9rem)">{p['h1']}</h1>
<p>{p['dek']}</p>
<p style="font-size:.86rem;color:rgba(255,255,255,.78);margin-top:.6rem">By {AUTHOR} · Updated {_fmt_date(p['mod'])}</p></div></section>
<section class="intro"><div class="wrap"><div class="prose">{body}
<div class="stat" style="margin-top:2rem"><span class="i">📋</span><div><p>Every BVA floor passes a 52-point Floor-Ready inspection before we call it done.</p>
<p class="s">{EXPERIENCE} of Gulf Coast experience · Licensed &amp; insured · Free 24-hr estimate</p></div></div>
</div></div></section>
<section style="background:var(--sand)"><div class="wrap"><div class="shead"><span class="eyebrow">Keep Reading</span><h2>Helpful Next Steps</h2></div>
<div class="rel-grid" style="max-width:820px;margin:0 auto">{links}</div></div></section>
<section class="faqs"><div class="wrap"><div class="shead"><span class="eyebrow">FAQ</span><h2>Quick Answers</h2></div>{faq_html}</div></section>
{wa_banner()}
{final_cta()}
{footer()}{wa_float()}{MENU_JS}{schema}</body></html>""")

# ── Support files ───────────────────────────────────────────────────────────
def robots_txt():
    return (f"User-agent: *\nAllow: /\n\n"
            f"# AI crawlers welcome\nUser-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\n"
            f"User-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
            f"Sitemap: https://{DOMAIN}/sitemap.xml\n")

def headers_file():
    return ("/*\n  X-Frame-Options: DENY\n  X-Content-Type-Options: nosniff\n"
            "  Referrer-Policy: strict-origin-when-cross-origin\n"
            "  Permissions-Policy: camera=(), microphone=(), geolocation=()\n"
            "  X-XSS-Protection: 1; mode=block\n\n"
            "/images/*\n  Cache-Control: public, max-age=31536000, immutable\n\n"
            "/*.svg\n  Cache-Control: public, max-age=31536000, immutable\n")

def redirects_file():
    return ("/home  /  301\n/index  /  301\n/services  /hardwood-flooring/  301\n"
            "/hardwood  /hardwood-flooring/  301\n/vinyl  /vinyl-plank-flooring/  301\n"
            "/lvp  /vinyl-plank-flooring/  301\n/tile  /tile-installation/  301\n"
            "/laminate  /laminate-flooring/  301\n/stairs  /stair-treads/  301\n"
            "/repair  /floor-repair/  301\n")

def sitemap_xml():
    urls=[("/","1.0","weekly")]
    for s in SERVICES: urls.append((f"/{s['slug']}/","0.9","monthly"))
    for slug,_ in AREAS:
        urls.append((f"/{slug}/","0.8","monthly"))
        for s in SERVICES: urls.append((f"/{s['slug']}/{slug}/","0.7","monthly"))
    urls.append(("/blog/","0.6","weekly"))
    for p in BLOG_POSTS: urls.append((f"/blog/{p['slug']}/","0.6","monthly"))
    urls += [("/about/","0.5","monthly"),("/contact/","0.7","monthly")]
    body="".join(f"  <url><loc>https://{DOMAIN}{p}</loc><changefreq>{cf}</changefreq><priority>{pr}</priority></url>\n"
                 for p,pr,cf in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+body+'</urlset>\n')
