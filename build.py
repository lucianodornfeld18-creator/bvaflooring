#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BVA Flooring — MVP site generator.
Distinct design system + original copy (NOT a Triangle/Napa clone).
Run: python build.py
Generates logo, MVP pages, support files into this folder.
"""
import os, json, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Business constants (real NAP) ───────────────────────────────────────────
BRAND      = "BVA Flooring"
LEGAL      = "BVA Services Corp"
TAGLINE    = "Pro Flooring Installation"
DOMAIN     = "bvaflooring.com"
PHONE_E164 = "+19418070339"
PHONE_DISP = "(941) 807-0339"
WA         = "19418070339"
EMAIL      = "bvaservicecorporation@gmail.com"
BASE_CITY  = "Bradenton"
STATE      = "FL"
ZIP        = "34208"          # NAP shows city+ZIP only (street hidden per owner)
FOUNDED    = "2020"           # founded ~6 years ago
EXPERIENCE = "6+ years"
STANDARD   = "BVA 52-Point Floor-Ready Standard"   # proprietary, named & numbered
WA_MSG     = "Hi%20BVA%20Flooring%2C%20I%27d%20like%20a%20free%20flooring%20estimate."
WEB3FORMS_KEY = "ec8d14c8-69fd-4433-b7ed-23a54218333d"   # web3forms.com -> emails leads to bvaservicecorporation@gmail.com

# ── Services ────────────────────────────────────────────────────────────────
SERVICES = [
    {"slug":"hardwood-flooring","name":"Hardwood Flooring","short":"Hardwood","icon":"🪵",
     "blurb":"Engineered & solid hardwood installed for Gulf-Coast humidity — acclimated, moisture-tested, and finished to last."},
    {"slug":"vinyl-plank-flooring","name":"Luxury Vinyl Plank","short":"Vinyl Plank","icon":"🧱",
     "blurb":"100% waterproof LVP/SPC over a flat, prepped subfloor — the smart pick for Florida living, rentals, and pets."},
    {"slug":"tile-installation","name":"Tile Installation","short":"Tile","icon":"◧",
     "blurb":"Porcelain, ceramic, and large-format tile set dead-flat with proper waterproofing for showers, floors, and lanais."},
    {"slug":"laminate-flooring","name":"Laminate Flooring","short":"Laminate","icon":"▤",
     "blurb":"High-AC-rating laminate with tight, level seams — budget-friendly looks without the budget-floor finish."},
    {"slug":"stair-treads","name":"Stair Treads","short":"Stair Treads","icon":"▦",
     "blurb":"Carpet-to-wood stair conversions and retreads — solid, quiet, code-minded steps that match your floors."},
    {"slug":"floor-repair","name":"Floor Repair & Replacement","short":"Floor Repair","icon":"🛠",
     "blurb":"Water-damaged boards, hollow tile, squeaks, and failed seams — diagnosed and fixed without ripping out the whole room."},
    {"slug":"hardwood-refinishing","name":"Hardwood Refinishing","short":"Refinishing","icon":"✨",
     "blurb":"Sand, repair, recolor, and reseal tired hardwood back to new — gaps, scratches, and worn finish gone without a full replacement."},
]
SVC = {s["slug"]: s for s in SERVICES}

# ── Service areas (full target structure; MVP builds Bradenton only) ─────────
AREAS = [
    ("bradenton","Bradenton"),("sarasota","Sarasota"),("lakewood-ranch","Lakewood Ranch"),
    ("palmetto","Palmetto"),("parrish","Parrish"),("venice","Venice"),
    ("tampa","Tampa"),("st-petersburg","St. Petersburg"),
]

# ── City data (Bradenton = real neighborhoods/ZIPs) ─────────────────────────
CITIES = {
 "bradenton":{
   "name":"Bradenton","county":"Manatee County","lat":27.4989,"lng":-82.5748,
   "zips":["34201","34202","34203","34205","34207","34208","34209","34210","34211","34212"],
   "hoods":["West Bradenton","Bayshore Gardens","Cortez","Palma Sola","Ballantyne","River Run",
            "Braden River","Tara","Riverview Boulevard","Whitfield Estates","Cordova Lakes",
            "Wares Creek","Perico Island","Pointe West","San Remo Shores","Village Green",
            "Coral Shores","Bayshore on the Lake","Riverdale","Greenbrook"],
   "landmarks":"the Riverwalk, Robinson Preserve, the historic Village of the Arts, and the Manatee River waterfront",
   "intro":("Bradenton homes run the gamut — 1950s block ranches near Palma Sola, waterfront builds along the "
            "Manatee River, and new construction out toward Lakewood Ranch. What ties them together is humidity. "
            "Sitting between the Gulf and the river, Bradenton air swings far wetter than the 45–55% your AC holds "
            "indoors, and flooring that isn't installed for that swing will cup, gap, or peel within a season or two. "),
 },
 "sarasota":{
   "name":"Sarasota","county":"Sarasota County","lat":27.3364,"lng":-82.5307,
   "zips":["34231","34232","34233","34234","34235","34236","34237","34238","34239","34240","34241","34242"],
   "hoods":["Southside Village","Gulf Gate","Arlington Park","Laurel Park","Bird Key","Lido Key",
            "Siesta Key","Palmer Ranch","Fruitville","Bee Ridge","Rosemary District","The Meadows",
            "McClellan Park","Cherokee Park","Hudson Bayou","Sapphire Shores","Indian Beach","Osprey"],
   "landmarks":"St. Armands Circle, Siesta Key Beach, the Bayfront, and the Ringling Museum district",
   "intro":("From historic bungalows in Laurel Park to barrier-island condos on Siesta and Lido Key, Sarasota "
            "flooring has to fight salt air and constant humidity. Coastal homes especially punish floors installed "
            "without moisture control — which is exactly the step we never skip."),
 },
 "lakewood-ranch":{
   "name":"Lakewood Ranch","county":"Manatee &amp; Sarasota Counties","lat":27.4178,"lng":-82.3445,
   "zips":["34202","34211","34212","34240"],
   "hoods":["Country Club East","Lakewood National","Greenbrook","Summerfield","Del Webb","Esplanade",
            "Polo Run","Waterside","Mallory Park","Central Park","Bridgewater","Lorraine Lakes",
            "Indigo","Azario","The Lake Club","Riverwalk"],
   "landmarks":"Lakewood Ranch Main Street, Waterside Place, and the UTC shopping district",
   "intro":("Lakewood Ranch is one of the fastest-growing communities in the country, which means a lot of "
            "newer slab-on-grade homes. Fresh concrete holds construction moisture for months — install over it "
            "without testing and a beautiful floor fails fast. We test every slab before a single plank goes down."),
 },
 "palmetto":{
   "name":"Palmetto","county":"Manatee County","lat":27.5214,"lng":-82.5723,
   "zips":["34221"],
   "hoods":["Riviera Dunes","Northwood","Artisan Lakes","Esplanade at Artisan Lakes","Sanctuary Cove",
            "Trevesta","Willow Walk","Fresh Meadows","Old Palmetto","Heron Creek","Silverstone",
            "Eave's Bend","Lincoln Park","Palmetto Point"],
   "landmarks":"Emerson Point Preserve, the Manatee River, and Palmetto's historic downtown",
   "intro":("Palmetto blends old riverfront cottages with new gated communities like Riviera Dunes and Artisan "
            "Lakes. Whether your floor sits over a 1940s slab or new construction, the Manatee River keeps the "
            "ground damp — so moisture testing and the right vapor barrier are non-negotiable."),
 },
 "parrish":{
   "name":"Parrish","county":"Manatee County","lat":27.5872,"lng":-82.4254,
   "zips":["34219"],
   "hoods":["North River Ranch","Silverleaf","Crosscreek","Kingsfield","Forest Creek","Rye Ranch",
            "Aviary at Rutland Ranch","Canoe Creek","Twin Rivers","River Wilderness","Harrison Ranch",
            "Chelsea Oaks","Copperstone","Isles at Bayview"],
   "landmarks":"Fort Hamer Park, the Manatee River, and the Florida Railroad Museum",
   "intro":("Parrish is booming with master-planned communities like North River Ranch and Silverleaf — almost "
            "all new-build, slab-on-grade homes. That makes construction-moisture in fresh concrete the single "
            "biggest flooring risk here, and the reason every Parrish job starts with a documented slab test."),
 },
 "venice":{
   "name":"Venice","county":"Sarasota County","lat":27.0998,"lng":-82.4543,
   "zips":["34285","34292","34293"],
   "hoods":["Venice Island","Venezia Park","Gulf View","Golden Beach","Pelican Pointe","Venetian Golf &amp; River Club",
            "Gran Paradiso","IslandWalk","Caribbean Village","Bird Bay","South Venice","Jacaranda",
            "Sorrento","Chestnut Creek","Auburn Cove"],
   "landmarks":"Venice Beach, the Venetian Waterway, historic downtown Venice, and Caspersen Beach",
   "intro":("Venice mixes mid-century island homes with newer 55+ communities like IslandWalk and Gran Paradiso. "
            "Island and near-Gulf homes battle salt air and high humidity; many are also second homes that sit "
            "closed up — a combination that destroys floors installed without proper moisture control."),
 },
 "tampa":{
   "name":"Tampa","county":"Hillsborough County","lat":27.9506,"lng":-82.4572,
   "zips":["33602","33603","33604","33606","33609","33611","33616","33629","33647"],
   "hoods":["Hyde Park","South Tampa","Davis Islands","Palma Ceia","Bayshore Beautiful","Westchase",
            "New Tampa","Carrollwood","Seminole Heights","Ybor City","Channelside","Tampa Palms",
            "SoHo","Beach Park","Sunset Park","Virginia Park"],
   "landmarks":"Bayshore Boulevard, the Tampa Riverwalk, Hyde Park Village, and Davis Islands",
   "intro":("Tampa runs from 1920s Hyde Park bungalows to high-rise condos on the water. Older South Tampa homes "
            "hide uneven, moisture-prone subfloors; new builds carry slab moisture. Both need the prep work most "
            "crews rush — which is where floors quietly fail two years later."),
 },
 "st-petersburg":{
   "name":"St. Petersburg","county":"Pinellas County","lat":27.7676,"lng":-82.6403,
   "zips":["33701","33702","33703","33704","33705","33707","33710","33711","33712","33713"],
   "hoods":["Old Northeast","Historic Kenwood","Snell Isle","Crescent Lake","Shore Acres","Downtown",
            "Allendale","Euclid-St. Paul","Greater Pinellas Point","Jungle Terrace","Tyrone","Disston Heights",
            "Coquina Key","Bahama Shores"],
   "landmarks":"the St. Pete Pier, Beach Drive, the waterfront museums, and Central Avenue",
   "intro":("St. Pete is full of character homes — 1920s Kenwood bungalows, Old Northeast Craftsmans, mid-century "
            "blocks near the water. Older wood subfloors and a peninsula surrounded by water mean moisture and "
            "leveling are the make-or-break steps for any St. Petersburg floor."),
 },
}

# ── Design system (distinct: Sora + Source Sans 3, navy + copper, warm sand) ─
CSS = """
:root{
--ink:#16335E;--ink-2:#0E2547;--ink-soft:#EAF0F8;
--copper:#C0843C;--copper-dk:#A66E2C;--copper-soft:#FBF1E3;
--slate:#9EAAB8;--text:#22262B;--muted:#5C6571;
--sand:#F4EFE8;--paper:#FBFAF8;--line:#E7E1D8;--white:#fff;
--wa:#25D366;--ok:#2F855A;
--radius:14px;--radius-lg:20px;
--sh-sm:0 1px 2px rgba(14,37,71,.06),0 1px 3px rgba(14,37,71,.10);
--sh:0 6px 18px rgba(14,37,71,.10);--sh-lg:0 22px 48px rgba(14,37,71,.16);
--fhead:'Sora',system-ui,sans-serif;--fbody:'Source Sans 3',system-ui,-apple-system,sans-serif;
--wrap:1300px;--ease:.25s cubic-bezier(.4,0,.2,1)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:88px;-webkit-text-size-adjust:100%}
body{font-family:var(--fbody);font-size:16.5px;line-height:1.65;color:var(--text);background:var(--paper);overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--ink);text-decoration:none;transition:color var(--ease)}
a:hover{color:var(--copper-dk)}
h1,h2,h3,h4{font-family:var(--fhead);font-weight:700;line-height:1.14;letter-spacing:-.02em;color:var(--ink-2)}
h1{font-size:clamp(2.05rem,5vw,3.25rem)}
h2{font-size:clamp(1.55rem,3.3vw,2.2rem)}
h3{font-size:clamp(1.12rem,1.9vw,1.34rem)}
p{margin:0 0 1rem}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 22px}
.eyebrow{display:inline-block;font-family:var(--fhead);font-size:.74rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--copper-dk);margin-bottom:.7rem}
.eyebrow::before{content:"";display:inline-block;width:26px;height:2px;background:var(--copper);vertical-align:middle;margin-right:10px;margin-bottom:4px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:14px 26px;font-family:var(--fhead);font-weight:600;font-size:.97rem;border-radius:10px;cursor:pointer;border:none;transition:all var(--ease);white-space:nowrap;letter-spacing:.01em}
.btn-primary{background:var(--copper);color:#fff;box-shadow:0 6px 18px rgba(192,132,60,.34)}
.btn-primary:hover{background:var(--copper-dk);color:#fff;transform:translateY(-2px)}
.btn-ink{background:var(--ink);color:#fff}
.btn-ink:hover{background:var(--ink-2);color:#fff;transform:translateY(-2px)}
.btn-outline{background:transparent;color:var(--ink);border:1.5px solid var(--ink)}
.btn-outline:hover{background:var(--ink);color:#fff}
.btn-ghost{background:rgba(255,255,255,.08);color:#fff;border:1.5px solid rgba(255,255,255,.45)}
.btn-ghost:hover{background:#fff;color:var(--ink)}
/* header */
.hdr{position:sticky;top:0;z-index:100;background:rgba(251,250,248,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;gap:1rem;max-width:var(--wrap);margin:0 auto;padding:12px 22px}
.brand{display:flex;align-items:center;gap:11px;flex-shrink:0}
.brand img{height:44px;width:44px}
.brand-tx{display:flex;flex-direction:column;line-height:1.04}
.brand-nm{font-family:var(--fhead);font-weight:800;font-size:1.2rem;color:var(--ink-2);letter-spacing:-.02em}
.brand-sb{font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--copper-dk);margin-top:3px;font-weight:600}
.menu{display:flex;align-items:center;gap:1.15rem;list-style:none}
.menu>li{position:relative}
.menu>li>a{font-family:var(--fhead);font-weight:500;color:var(--ink-2);font-size:.95rem;padding:9px 3px;display:inline-block}
.menu>li>a:hover{color:var(--copper-dk)}
.drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-8px);background:#fff;min-width:248px;border-radius:12px;box-shadow:var(--sh-lg);padding:.5rem 0;opacity:0;visibility:hidden;transition:all var(--ease);border:1px solid var(--line)}
.menu>li:hover .drop{opacity:1;visibility:visible;transform:translateX(-50%) translateY(0)}
.drop a{display:block;padding:9px 18px;font-size:.92rem;color:var(--text)}
.drop a:hover{background:var(--ink-soft);color:var(--ink)}
.nav-cta{display:flex;align-items:center;gap:.8rem;flex-shrink:0}
.nav-ph{display:flex;align-items:center;gap:6px;color:var(--ink);font-family:var(--fhead);font-weight:700;font-size:.95rem;white-space:nowrap}
.nav-ph svg{width:16px;height:16px}
.burger{display:none;background:none;border:none;cursor:pointer;padding:7px;color:var(--ink)}
.burger svg{width:26px;height:26px}
/* hero (split, left-aligned + estimate card) */
.hero{position:relative;background:linear-gradient(160deg,#0E2547 0%,#16335E 60%,#1d4274 100%);color:#fff;overflow:hidden;padding:0}
.hero::after{content:"";position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Cpath d='M0 0h30v30H0zM30 30h30v30H30z' fill='%23ffffff' fill-opacity='0.03'/%3E%3C/svg%3E");opacity:.6}
.hero-grid{position:relative;z-index:1;max-width:var(--wrap);margin:0 auto;padding:3.6rem 22px 3.4rem;display:grid;grid-template-columns:1.25fr .9fr;gap:2.6rem;align-items:center}
.hero h1{color:#fff;margin-bottom:1rem}
.hero h1 b{color:var(--copper);font-weight:700}
.hero-lead{font-size:1.1rem;color:rgba(255,255,255,.9);max-width:560px;margin-bottom:1.5rem}
.hero-cta{display:flex;gap:.8rem;flex-wrap:wrap;margin-bottom:1.5rem}
.hero-trust{display:flex;flex-wrap:wrap;gap:.55rem 1.4rem;font-size:.9rem;color:rgba(255,255,255,.92);font-family:var(--fhead);font-weight:500}
.hero-trust span{display:inline-flex;align-items:center;gap:7px}
.hero-trust span::before{content:"✓";color:var(--copper);font-weight:800}
.stars{color:#F4C04E;letter-spacing:2px;font-size:1.05rem}
.ecard{background:#fff;border-radius:18px;box-shadow:var(--sh-lg);padding:1.7rem;color:var(--text)}
.ecard h3{color:var(--ink-2);font-size:1.18rem;margin-bottom:.3rem}
.ecard .sub{font-size:.9rem;color:var(--muted);margin-bottom:1.1rem}
.ecard label{display:block;font-size:.78rem;font-weight:700;font-family:var(--fhead);color:var(--ink-2);margin:.6rem 0 .25rem;text-transform:uppercase;letter-spacing:.05em}
.ecard input,.ecard select{width:100%;padding:11px 13px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--fbody);font-size:.95rem;background:var(--paper);color:var(--text)}
.ecard textarea{width:100%;padding:11px 13px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--fbody);font-size:.95rem;background:var(--paper);color:var(--text);min-height:88px;resize:vertical}
.ecard input:focus,.ecard select:focus,.ecard textarea:focus{outline:none;border-color:var(--copper)}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}
@media(max-width:560px){.frow{grid-template-columns:1fr}}
.ecard .btn{width:100%;margin-top:1rem}
.ecard .fine{font-size:.76rem;color:var(--muted);text-align:center;margin:.7rem 0 0}
/* proof strip */
.proof{background:var(--ink-2);color:#fff;padding:1.1rem 0}
.proof-row{display:flex;flex-wrap:wrap;justify-content:center;gap:1rem 2.6rem;text-align:center}
.proof-row div{font-size:.92rem;color:rgba(255,255,255,.86)}
.proof-row b{display:block;font-family:var(--fhead);font-size:1.35rem;color:#fff;font-weight:800}
.proof-row b.cu{color:var(--copper)}
section{padding:4.2rem 0}
.shead{max-width:760px;margin:0 auto 2.6rem;text-align:center}
.shead p{color:var(--muted);font-size:1.06rem;margin-top:.55rem}
.intro{background:#fff}
.prose{max-width:780px;margin:0 auto;font-size:1.07rem;line-height:1.78}
.prose p{margin-bottom:1.15rem}.prose strong{color:var(--ink-2)}
/* service cards */
.svc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.3rem}
.svc-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:1.6rem;transition:all var(--ease);display:block;color:inherit;position:relative;overflow:hidden}
.svc-card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--copper);transform:scaleY(0);transform-origin:top;transition:transform var(--ease)}
.svc-card:hover{transform:translateY(-4px);box-shadow:var(--sh-lg);border-color:transparent;color:inherit}
.svc-card:hover::before{transform:scaleY(1)}
.svc-ic{font-size:1.9rem;display:grid;place-items:center;width:54px;height:54px;background:var(--ink-soft);border-radius:13px;margin-bottom:1rem}
.svc-card h3{color:var(--ink-2);margin-bottom:.5rem}
.svc-card p{color:var(--muted);font-size:.96rem;margin-bottom:1rem}
.svc-card .more{font-family:var(--fhead);font-weight:600;font-size:.9rem;color:var(--copper-dk)}
/* project gallery */
.projsec{padding:4.4rem 0}
.projgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(248px,1fr));gap:1.2rem}
.proj{margin:0;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--sh-sm);transition:transform var(--ease),box-shadow var(--ease)}
.proj:hover{transform:translateY(-4px);box-shadow:var(--sh-lg)}
.proj img{display:block;width:100%;height:230px;object-fit:cover;background:var(--ink-soft)}
.proj figcaption{padding:.85rem 1rem;display:flex;flex-direction:column;gap:2px}
.proj figcaption b{font-family:var(--fhead);font-weight:600;color:var(--ink-2);font-size:.98rem}
.proj figcaption span{color:var(--muted);font-size:.85rem}
/* why / features */
.feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem}
.feat{background:var(--sand);border-radius:16px;padding:1.6rem}
.feat .n{font-family:var(--fhead);font-weight:800;font-size:1.5rem;color:var(--copper);margin-bottom:.4rem}
.feat h3{font-size:1.1rem;color:var(--ink-2);margin-bottom:.45rem}
.feat p{color:var(--muted);font-size:.95rem;margin:0}
/* stat badge */
.stat{background:linear-gradient(135deg,var(--copper-soft),#F6E4C8);border:1.5px solid #E6BE80;border-radius:14px;padding:1.1rem 1.4rem;margin:1.7rem 0;display:flex;align-items:center;gap:15px;flex-wrap:wrap}
.stat .i{font-size:2rem}
.stat p{margin:0;color:#7A4E16;font-weight:700;font-size:.97rem;font-family:var(--fhead)}
.stat p.s{color:#946018;font-weight:500;font-size:.84rem;font-family:var(--fbody)}
/* pricing */
.pricing{background:var(--sand)}
.ptab{background:#fff;border-radius:16px;overflow:hidden;box-shadow:var(--sh);border:1px solid var(--line);max-width:940px;margin:0 auto}
.ptab table{width:100%;border-collapse:collapse;font-size:.96rem}
.ptab thead{background:linear-gradient(135deg,var(--ink-2),var(--ink))}
.ptab th{padding:14px 18px;text-align:left;color:#fff;font-family:var(--fhead);font-weight:600;font-size:.82rem;letter-spacing:.05em;text-transform:uppercase}
.ptab tbody tr{border-bottom:1px solid var(--line)}
.ptab tbody tr:last-child{border-bottom:none}
.ptab tbody tr:nth-child(even){background:var(--paper)}
.ptab td{padding:13px 18px;vertical-align:top}
.ptab td:first-child{font-weight:700;color:var(--ink-2)}
.ptab td.pr{font-weight:800;color:var(--copper-dk);white-space:nowrap;font-family:var(--fhead)}
.pnote{text-align:center;font-size:.85rem;color:var(--muted);margin-top:1rem}
.pnote a{color:var(--copper-dk);font-weight:700}
/* checklist */
.chk-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.3rem;margin-top:2rem}
.chk{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--sh-sm)}
.chk-h{background:linear-gradient(135deg,var(--ink),#234b82);padding:.9rem 1.15rem;color:#fff;display:flex;align-items:center;gap:.7rem}
.chk-h .e{font-size:1.4rem}
.chk-h b{font-family:var(--fhead);font-size:.99rem;display:block}
.chk-h span{font-size:.72rem;opacity:.82;text-transform:uppercase;letter-spacing:.05em}
.chk ol{list-style:none;counter-reset:c;padding:.85rem 1.15rem;font-size:.92rem}
.chk li{counter-increment:c;padding:5px 0 5px 26px;position:relative;color:var(--text);line-height:1.45}
.chk li::before{content:counter(c);position:absolute;left:0;top:5px;width:19px;height:19px;background:var(--copper-soft);color:var(--copper-dk);border-radius:50%;font-size:.68rem;font-weight:800;display:grid;place-items:center;font-family:var(--fhead)}
/* neighborhoods */
.nbhd{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:.65rem;max-width:940px;margin:1.8rem auto 0}
.nbhd span{background:#fff;border:1px solid var(--line);color:var(--ink-2);padding:11px 15px;border-radius:10px;text-align:center;font-weight:600;font-size:.91rem;font-family:var(--fhead)}
.zips{display:flex;flex-wrap:wrap;gap:.55rem;justify-content:center;max-width:760px;margin:1.4rem auto 0}
.zips span{background:var(--ink-soft);color:var(--ink);padding:7px 15px;border-radius:50px;font-family:var(--fhead);font-weight:700;font-size:.86rem}
/* faq */
.faqs{background:#fff}
.faq-l{max-width:830px;margin:0 auto}
.faq{border:1px solid var(--line);border-radius:12px;margin-bottom:.9rem;overflow:hidden;background:var(--paper)}
.faq[open]{border-color:var(--copper);box-shadow:var(--sh)}
.faq summary{padding:1.1rem 1.3rem;font-family:var(--fhead);font-weight:600;font-size:1.01rem;color:var(--ink-2);cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:1rem;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:1.5rem;color:var(--copper);font-weight:300;flex-shrink:0;line-height:1}
.faq[open] summary::after{content:"−"}
.faq-c{padding:0 1.3rem 1.15rem;color:var(--muted);line-height:1.7;font-size:.97rem}
/* related / internal links */
.rel-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.1rem;margin-top:1.8rem}
.rel{background:var(--sand);border:1px solid var(--line);border-radius:14px;padding:1.3rem;display:block;color:inherit;transition:all var(--ease)}
.rel:hover{transform:translateY(-3px);box-shadow:var(--sh);background:#fff;color:inherit}
.rel b{font-family:var(--fhead);color:var(--ink-2);display:block;margin-bottom:.25rem}
.rel span{font-size:.88rem;color:var(--muted)}
/* whatsapp banner */
.wab{background:linear-gradient(135deg,#128C7E,#25D366);border-radius:18px;padding:1.6rem 2rem;margin:2.6rem auto;max-width:var(--wrap);display:flex;align-items:center;justify-content:space-between;gap:1.4rem;flex-wrap:wrap;box-shadow:0 16px 34px rgba(37,211,102,.26)}
.wab b{font-family:var(--fhead);color:#fff;font-size:1.14rem;display:block}
.wab span{color:rgba(255,255,255,.92);font-size:.9rem}
.wab a{background:#fff;color:#128C7E;padding:13px 24px;border-radius:10px;font-family:var(--fhead);font-weight:700;display:inline-flex;align-items:center;gap:8px}
/* final cta */
.fcta{background:linear-gradient(160deg,#0E2547,#16335E);color:#fff;text-align:center;padding:4.6rem 0}
.fcta h2{color:#fff;margin-bottom:.8rem}
.fcta p{color:rgba(255,255,255,.9);max-width:620px;margin:0 auto 1.5rem;font-size:1.05rem}
.fcta .ph{font-family:var(--fhead);font-size:1.65rem;font-weight:800;color:#fff;display:inline-block;margin:.6rem 0}
.fcta .ph:hover{color:var(--copper)}
.fcta-btns{display:flex;justify-content:center;gap:.9rem;flex-wrap:wrap}
/* breadcrumbs */
.crumbs{background:var(--sand);padding:13px 0;font-size:.85rem;border-bottom:1px solid var(--line)}
.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:8px;color:var(--muted)}
.crumbs li{display:flex;gap:8px;align-items:center}
.crumbs li::after{content:"›";color:var(--slate)}
.crumbs li:last-child::after{display:none}
.crumbs a{color:var(--copper-dk);font-weight:600}
.crumbs li:last-child{color:var(--ink-2);font-weight:700}
/* page hero (interior) */
.phero{background:linear-gradient(160deg,#0E2547,#16335E 70%,#1d4274);color:#fff;padding:3.2rem 0 2.8rem;text-align:center}
.phero h1{color:#fff;margin-bottom:.8rem}
.phero h1 b{color:var(--copper)}
.phero p{color:rgba(255,255,255,.9);max-width:720px;margin:0 auto 1.2rem;font-size:1.06rem}
.phero .eyebrow{color:#E8C79A}
.phero-trust{display:flex;justify-content:center;flex-wrap:wrap;gap:.5rem 1.4rem;font-size:.88rem;color:rgba(255,255,255,.92);font-family:var(--fhead);font-weight:500;margin-top:1rem}
.phero-trust span::before{content:"✓";color:var(--copper);font-weight:800;margin-right:6px}
/* footer */
footer{background:#0A1D38;color:rgba(255,255,255,.8);padding:3.6rem 0 0;font-size:.93rem}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1.1fr;gap:2.4rem;margin-bottom:2.4rem}
.fcol h4{color:#fff;font-size:.82rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;margin-bottom:1rem;font-family:var(--fhead)}
.fbrand{display:flex;align-items:center;gap:11px;margin-bottom:1rem}
.fbrand img{height:42px;width:42px;filter:brightness(0) invert(1)}
.fbrand b{font-family:var(--fhead);font-size:1.2rem;color:#fff}
.fcol p{color:rgba(255,255,255,.66);line-height:1.62;font-size:.9rem}
.fcol ul{list-style:none}
.fcol li{margin-bottom:.55rem}
.fcol a{color:rgba(255,255,255,.72);font-size:.9rem}
.fcol a:hover{color:var(--copper)}
.fc-item{display:flex;gap:9px;margin-bottom:.7rem;font-size:.9rem;color:rgba(255,255,255,.74);align-items:flex-start}
.fc-item svg{width:15px;height:15px;color:var(--copper);flex-shrink:0;margin-top:3px}
.fbot{border-top:1px solid rgba(255,255,255,.1);padding:1.4rem 0;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.8rem;font-size:.83rem;color:rgba(255,255,255,.55)}
.fbot a{color:rgba(255,255,255,.6)}
/* whatsapp float */
.wafloat{position:fixed;bottom:22px;right:22px;z-index:9999;background:var(--wa);color:#fff;padding:13px 19px;border-radius:50px;font-family:var(--fhead);font-weight:600;font-size:.9rem;display:inline-flex;align-items:center;gap:8px;box-shadow:0 8px 24px rgba(37,211,102,.45)}
.wafloat:hover{transform:translateY(-3px) scale(1.04);color:#fff}
.wafloat svg{width:20px;height:20px}
@media(max-width:1080px){.hero-grid{grid-template-columns:1fr;gap:2rem}.ecard{max-width:440px}.fgrid{grid-template-columns:1fr 1fr}}
@media(max-width:920px){
.menu{display:none;position:absolute;top:100%;left:0;right:0;flex-direction:column;background:#fff;padding:.4rem 0;box-shadow:var(--sh-lg);border-top:1px solid var(--line);max-height:calc(100vh - 76px);overflow-y:auto}
.menu.open{display:flex}
.menu>li{width:100%;border-bottom:1px solid var(--line)}
.menu>li>a{padding:13px 22px;display:flex;justify-content:space-between;align-items:center}
.menu>li>a[data-t]::after{content:"+";font-size:1.3rem;color:var(--copper);font-weight:300}
.menu>li.exp>a[data-t]::after{content:"−"}
.drop{position:static;transform:none;opacity:1;visibility:visible;box-shadow:none;background:var(--sand);border:none;border-radius:0;padding:0;display:none;min-width:0}
.menu>li.exp .drop{display:block}
.drop a{padding:11px 22px 11px 38px}
.nav-ph span{display:none}.burger{display:block}.nav-cta .btn{display:none}
.wafloat span{display:none}.wafloat{padding:12px}
}
@media(max-width:680px){.fgrid{grid-template-columns:1fr}.proof-row{gap:.8rem 1.6rem}.ptab{overflow-x:auto}.ptab table{min-width:520px}}
"""

# ── SVG snippets ────────────────────────────────────────────────────────────
SVG_PHONE='<svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'
SVG_WA='<svg fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.71.306 1.263.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'
SVG_PIN='<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_MAIL='<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'
SVG_CLOCK='<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
SVG_PHONE2='<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>'

def wa_link(extra=""):
    return f"https://wa.me/{WA}?text={WA_MSG}"

# ── Head ────────────────────────────────────────────────────────────────────
def head(title, desc, path, og="og-default.jpg"):
    canon=f"https://{DOMAIN}{path}"
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="geo.region" content="US-FL"><meta name="geo.placename" content="Bradenton, Florida">
<meta name="geo.position" content="27.4989;-82.5748"><meta name="ICBM" content="27.4989, -82.5748">
<meta property="og:type" content="website"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="https://{DOMAIN}/images/{og}">
<meta property="og:locale" content="en_US"><meta property="og:site_name" content="{BRAND}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="https://{DOMAIN}/images/{og}">
<link rel="icon" type="image/svg+xml" href="/images/logo.svg">
<link rel="apple-touch-icon" href="/images/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>"""

# ── Header / footer / CTAs ──────────────────────────────────────────────────
def header():
    svc_links="".join(f'<a href="/{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    area_links="".join(f'<a href="/{slug}/">📍 {nm}, FL</a>' for slug,nm in AREAS)
    return f"""<header class="hdr"><nav class="nav" aria-label="Main">
<a href="/" class="brand" aria-label="{BRAND} home">
<img src="/images/logo.svg" alt="{BRAND} logo" width="44" height="44">
<span class="brand-tx"><span class="brand-nm">{BRAND}</span><span class="brand-sb">{TAGLINE}</span></span></a>
<ul class="menu" id="menu">
<li><a href="/">Home</a></li>
<li><a href="/hardwood-flooring/" data-t>Services</a><div class="drop">{svc_links}</div></li>
<li><a href="/bradenton/" data-t>Service Areas</a><div class="drop">{area_links}</div></li>
<li><a href="/blog/">Blog</a></li>
<li><a href="/faq/">FAQ</a></li>
<li><a href="/about/">About</a></li>
<li><a href="/contact/">Contact</a></li></ul>
<div class="nav-cta">
<a href="tel:{PHONE_E164}" class="nav-ph">{SVG_PHONE}<span>{PHONE_DISP}</span></a>
<a href="/contact/#quote" class="btn btn-primary">Free Quote</a>
<button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
</div></nav></header>"""

def footer():
    svc="".join(f'<li><a href="/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    area="".join(f'<li><a href="/{slug}/">{nm}, FL</a></li>' for slug,nm in AREAS)
    return f"""<footer><div class="wrap">
<div class="fgrid">
<div class="fcol">
<div class="fbrand"><img src="/images/logo.svg" alt="{BRAND}"><b>{BRAND}</b></div>
<p>Professional flooring installation across Bradenton, Sarasota, Lakewood Ranch &amp; the Tampa Bay Gulf Coast. Hardwood, luxury vinyl plank, tile, laminate, stair treads, and repair — installed for Florida humidity and backed in writing.</p>
</div>
<div class="fcol"><h4>Services</h4><ul>{svc}</ul></div>
<div class="fcol"><h4>Service Areas</h4><ul>{area}</ul></div>
<div class="fcol"><h4>Contact</h4>
<div class="fc-item">{SVG_PHONE2}<a href="tel:{PHONE_E164}">{PHONE_DISP}</a></div>
<div class="fc-item">{SVG_MAIL}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div class="fc-item">{SVG_PIN}<span>Bradenton, FL {ZIP} · serving all Tampa Bay</span></div>
<div class="fc-item">{SVG_CLOCK}<span>Mon–Sat · 7 AM – 7 PM</span></div>
</div></div>
<div class="fbot">
<div>© 2026 {LEGAL} ({BRAND}). All rights reserved. · Licensed &amp; insured · Locally owned.</div>
<div><a href="/about/">About</a> · <a href="/faq/">FAQ</a> · <a href="/financing/">Financing</a> · <a href="/warranty/">Warranty</a> · <a href="/contact/">Contact</a></div>
</div></div></footer>"""

def wa_float():
    return f'<a href="{wa_link()}" target="_blank" rel="noopener" class="wafloat" aria-label="Chat on WhatsApp">{SVG_WA}<span>Free Quote</span></a>'

def wa_banner():
    return f"""<div class="wab"><div><b>Free estimate within 24 hours.</b><span>Call, text, or WhatsApp — we answer 7 days a week.</span></div>
<a href="{wa_link()}" target="_blank" rel="noopener">{SVG_WA} WhatsApp Us</a></div>"""

def final_cta(line=None):
    line=line or f"From first measurement to final baseboard, {BRAND} delivers Florida-tough installations across Tampa Bay. Free measurement. Locked-in pricing. Written workmanship warranty."
    return f"""<section class="fcta"><div class="wrap">
<span class="eyebrow" style="color:#E8C79A">Ready when you are</span>
<h2>Get Your Free Flooring Estimate</h2><p>{line}</p>
<a href="tel:{PHONE_E164}" class="ph">📞 {PHONE_DISP}</a>
<div class="fcta-btns"><a href="/contact/#quote" class="btn btn-primary">Get My Free Quote</a>
<a href="{wa_link()}" target="_blank" rel="noopener" class="btn btn-ghost">{SVG_WA} WhatsApp Us</a></div>
</div></section>"""

MENU_JS="""<script>
(function(){var b=document.getElementById('burger'),m=document.getElementById('menu');if(!b||!m)return;
b.addEventListener('click',function(){var o=m.classList.toggle('open');b.setAttribute('aria-expanded',o);if(!o)m.querySelectorAll('li.exp').forEach(function(l){l.classList.remove('exp')})});
m.querySelectorAll('a[data-t]').forEach(function(a){a.addEventListener('click',function(e){if(window.innerWidth>920)return;e.preventDefault();var l=a.parentElement,w=l.classList.contains('exp');m.querySelectorAll('li.exp').forEach(function(x){x.classList.remove('exp')});if(!w)l.classList.add('exp')})});
window.addEventListener('resize',function(){if(window.innerWidth>920){m.classList.remove('open');m.querySelectorAll('li.exp').forEach(function(l){l.classList.remove('exp')})}});
})();</script>"""

def jsonld(*objs):
    return "".join(f'<script type="application/ld+json">{json.dumps(o,ensure_ascii=False)}</script>' for o in objs)

# ── Schema helpers ──────────────────────────────────────────────────────────
def sc_org():
    return {"@context":"https://schema.org","@type":"Organization","@id":f"https://{DOMAIN}/#organization",
        "name":LEGAL,"alternateName":BRAND,"url":f"https://{DOMAIN}/","logo":{"@type":"ImageObject","url":f"https://{DOMAIN}/images/logo.svg"},
        "telephone":PHONE_E164,"email":EMAIL,"areaServed":[{"@type":"City","name":nm} for _,nm in AREAS],
        "address":{"@type":"PostalAddress","addressLocality":BASE_CITY,"addressRegion":STATE,"postalCode":ZIP,"addressCountry":"US"},
        "foundingDate":FOUNDED,"slogan":TAGLINE}

def sc_localbiz(path,desc,city=None,suffix=""):
    o={"@context":"https://schema.org","@type":["LocalBusiness","HomeAndConstructionBusiness"],
        "@id":f"https://{DOMAIN}{path}#business","name":f"{BRAND}{' — '+suffix if suffix else ''}",
        "description":desc,"url":f"https://{DOMAIN}{path}","telephone":PHONE_E164,"email":EMAIL,
        "image":f"https://{DOMAIN}/images/og-default.jpg","priceRange":"$$",
        "address":{"@type":"PostalAddress","addressLocality":city or BASE_CITY,"addressRegion":STATE,"postalCode":ZIP if not city or city==BASE_CITY else "","addressCountry":"US"},
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"07:00","closes":"19:00"}],
        "parentOrganization":{"@id":f"https://{DOMAIN}/#organization"}}
    if city:
        o["areaServed"]={"@type":"City","name":city,"containedInPlace":{"@type":"State","name":"Florida"}}
    else:
        o["areaServed"]=[{"@type":"City","name":nm} for _,nm in AREAS]
    return o

def sc_breadcrumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i,"name":nm,**({"item":f"https://{DOMAIN}{u}"} if u else {})}
        for i,(nm,u) in enumerate(items,1)]}

def sc_website():
    return {"@context":"https://schema.org","@type":"WebSite","@id":f"https://{DOMAIN}/#website",
        "url":f"https://{DOMAIN}/","name":BRAND,"publisher":{"@id":f"https://{DOMAIN}/#organization"}}

def crumbs(items):
    lis="".join((f'<li><a href="{u}">{nm}</a></li>' if u else f'<li>{nm}</li>') for nm,u in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{lis}</ol></div></nav>'

def faq_block(faqs):
    html="".join(f'<details class="faq"><summary>{q}</summary><div class="faq-c">{a}</div></details>' for q,a in faqs)
    schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub(r'<[^>]+>','',a).strip()}} for q,a in faqs]}
    return f'<div class="faq-l">{html}</div>', schema

# ── Writer ──────────────────────────────────────────────────────────────────
def write(path, html):
    full=os.path.join(ROOT,path.lstrip("/"))
    os.makedirs(os.path.dirname(full),exist_ok=True)
    with open(full,"w",encoding="utf-8") as f:
        f.write(html)
    print("  +",path)

def write_raw(relpath, content):
    full=os.path.join(ROOT,relpath)
    d=os.path.dirname(full)
    if d: os.makedirs(d,exist_ok=True)
    with open(full,"w",encoding="utf-8") as f:
        f.write(content)
    print("  +",relpath)

# Content module (page bodies) is imported after constants/helpers are defined.
import content as C

def main():
    print("Building BVA Flooring (full site) ->", ROOT)
    write_raw("images/logo.svg", C.LOGO_SVG)
    write_raw("robots.txt", C.robots_txt())
    write_raw("_headers", C.headers_file())
    write_raw("_redirects", C.redirects_file())
    write_raw("sitemap.xml", C.sitemap_xml())
    write_raw("llms.txt", C.llms_txt())
    write("/index.html", C.page_home())
    write("/about/index.html", C.page_about())
    write("/contact/index.html", C.page_contact())
    write("/thanks/index.html", C.page_thanks())
    write("/faq/index.html", C.page_faq())
    write("/financing/index.html", C.page_financing())
    write("/warranty/index.html", C.page_warranty())
    write("/404.html", C.page_404())
    for s in SERVICES:
        write(f"/{s['slug']}/index.html", C.page_service_index(s))
    for slug,_ in AREAS:
        write(f"/{slug}/index.html", C.page_city_hub(slug))
        for s in SERVICES:
            write(f"/{s['slug']}/{slug}/index.html", C.page_service_city(s,slug))
    write("/blog/index.html", C.page_blog_index())
    for post in C.BLOG_POSTS:
        write(f"/blog/{post['slug']}/index.html", C.page_blog_post(post))
    print("Done.")

if __name__=="__main__":
    main()
