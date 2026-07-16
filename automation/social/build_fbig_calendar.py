#!/usr/bin/env python3
"""Fila de posts Facebook + Instagram da BVA Flooring (igual Triangle).

- 4 templates de imagem rotativos (nenhuma foto repete visualmente por semanas).
- Legendas ricas em keyword servico+cidade, deep link pra pagina servico x cidade,
  hashtags locais + de servico. FB/IG permitem telefone/promocao (ao contrario do GBP).
- 3x/semana (seg/qua/sex). Saida: calendar-fbig-<data>.json + preview-fbig-<data>.html
  (o Make le a fila e publica no FB + IG).

Uso: py automation/social/build_fbig_calendar.py [semanas] [data-inicio YYYY-MM-DD]
"""
import json, sys
from datetime import datetime, timedelta
from pathlib import Path

SITE="https://bvaflooring.com"; IMG="https://bvaflooring.com/images/social-fbig"
PHONE="(941) 807-0339"; STANDARD="52-Point Floor-Ready Standard"

SVC={"hardwood":{"name":"Hardwood Flooring","kw":"hardwood flooring installation","slug":"hardwood-flooring"},
     "vinyl":{"name":"Luxury Vinyl Plank","kw":"luxury vinyl plank (LVP) installation","slug":"vinyl-plank-flooring"},
     "stairs":{"name":"Vinyl Stair Treads","kw":"vinyl stair tread installation","slug":"stair-treads"}}
CITY_SLUG={"Bradenton":"bradenton","Sarasota":"sarasota","Lakewood Ranch":"lakewood-ranch","Palmetto":"palmetto",
           "Parrish":"parrish","Venice":"venice","Tampa":"tampa","St. Petersburg":"st-petersburg"}

# base = nome do arquivo sem extensao (existe -t1..-t4 em images/social-fbig)
BANK=[
 ("hardwood","Bradenton","hardwood-flooring-installation-bradenton-fl","a solid hardwood floor in a Bradenton living room"),
 ("hardwood","Lakewood Ranch","engineered-hardwood-flooring-lakewood-ranch-fl","engineered hardwood in a Lakewood Ranch home"),
 ("hardwood","Sarasota","hardwood-floor-installation-sarasota-fl","a hardwood floor installation in a Sarasota home"),
 ("vinyl","Sarasota","luxury-vinyl-plank-flooring-sarasota-fl","100% waterproof luxury vinyl plank in a Sarasota home"),
 ("vinyl","Tampa","waterproof-vinyl-plank-installation-tampa-fl","a waterproof vinyl plank installation in Tampa"),
 ("vinyl","Venice","luxury-vinyl-plank-flooring-venice-fl","luxury vinyl plank (LVP) flooring in a Venice home"),
 ("vinyl","St. Petersburg","wood-look-vinyl-plank-flooring-st-petersburg-fl","wood-look vinyl plank in a St. Petersburg room"),
 ("vinyl","Palmetto","glue-down-vinyl-plank-flooring-palmetto-fl","glue-down luxury vinyl plank in Palmetto"),
 ("vinyl","Parrish","glue-down-luxury-vinyl-flooring-parrish-fl","glue-down luxury vinyl flooring in a Parrish home"),
 ("stairs","Bradenton","vinyl-stair-tread-installation-bradenton-fl","a vinyl stair tread installation in Bradenton"),
 ("stairs","Tampa","waterproof-vinyl-stair-treads-tampa-fl","waterproof vinyl stair treads in Tampa"),
 ("stairs","Lakewood Ranch","vinyl-stair-tread-installation-lakewood-ranch-fl","a vinyl stair tread and riser install in Lakewood Ranch"),
]

TEMPLATES=[
 "{kw_title} in {city}, FL done right. {desc}. Built for Florida humidity and backed by our {standard} — licensed & insured.\n\n\U0001F4DE Free estimate in 24h: {phone}\n\U0001F517 {link}\n\n{tags}",
 "Looking for {kw} in {city}, Florida? This is our work. {desc}. One accountable local crew, moisture-tested installs, written workmanship warranty.\n\n\U0001F4DE {phone} — free in-home estimate\n\U0001F517 {link}\n\n{tags}",
 "Another {svc_name} project in {city}, FL ✅ {desc}. From Bradenton to Tampa Bay, we install floors that actually last in Florida.\n\n\U0001F4DE Call {phone} for a free estimate\n\U0001F517 {link}\n\n{tags}",
 "Thinking about {kw} in {city}, FL? {desc}. New name, old-school standard — one crew, measurable quality on every floor.\n\n\U0001F4DE {phone}\n\U0001F517 {link}\n\n{tags}",
]
SVC_TAGS={"hardwood":["#HardwoodFloors","#HardwoodFlooring","#EngineeredHardwood","#WoodFloors"],
          "vinyl":["#LuxuryVinylPlank","#LVP","#VinylPlankFlooring","#WaterproofFlooring"],
          "stairs":["#StairTreads","#StairRemodel","#VinylStairs","#StaircaseUpgrade"]}
GEN=["#FloridaFlooring","#TampaBay","#FlooringContractor","#HomeRenovation","#FloridaHomes","#FlooringInstallation","#GulfCoast"]

def ctags(city):
    c=city.replace(" ","").replace(".","")
    return [f"#{c}",f"#{c}FL",f"#{c}Flooring"]

def build(weeks,start):
    posts=[]; days=[0,2,4]  # seg/qua/sex
    i=0
    for w in range(weeks):
        for slot in range(3):
            svc_k,city,base,desc=BANK[i%len(BANK)]
            tmpl=((i%4)+(i//len(BANK)))%4  # roda template e evita repetir template na volta da foto
            s=SVC[svc_k]
            link=f"{SITE}/{s['slug']}/{CITY_SLUG[city]}/"
            tags=" ".join(ctags(city)+SVC_TAGS[svc_k]+GEN)
            cap=TEMPLATES[tmpl].format(kw=s["kw"],kw_title=s["kw"].capitalize(),svc_name=s["name"],
                                       city=city,desc=desc,phone=PHONE,link=link,standard=STANDARD,tags=tags)
            d=start+timedelta(days=w*7+days[slot])
            posts.append({"date":d.strftime("%Y-%m-%dT")+("11:30:00" if slot%2==0 else "18:00:00"),
                          "channel":"fbig_bva","service":svc_k,"city":city,
                          "image_url":f"{IMG}/{base}-t{tmpl+1}.jpg","caption":cap,"link":link})
            i+=1
    return posts

def preview(posts):
    cards="".join(f'<div class="c"><img src="{p["image_url"].replace(IMG,"../../images/social-fbig")}" loading="lazy"><div class="b"><span class="dt">{p["date"][:16].replace("T"," ")}</span><pre>{p["caption"]}</pre></div></div>' for p in posts)
    return ('<!DOCTYPE html><meta charset="UTF-8"><title>Preview FB+IG BVA</title>'
      '<style>body{font-family:Segoe UI,sans-serif;background:#fbfaf8;padding:24px;color:#1b2330}h1{color:#0E2547}'
      '.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:16px}.c{background:#fff;border:1px solid #E3DDD3;border-radius:12px;overflow:hidden}'
      '.c img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block}.b{padding:12px}.dt{font-size:.78rem;color:#5d6675}'
      'pre{white-space:pre-wrap;font-family:inherit;font-size:.82rem;margin:8px 0 0;line-height:1.45}</style>'
      f'<h1>Fila FB + Instagram — {len(posts)} posts (4 templates rotativos)</h1><div class="g">{cards}</div>')

def main():
    weeks=int(sys.argv[1]) if len(sys.argv)>1 else 8
    start=datetime.strptime(sys.argv[2],"%Y-%m-%d") if len(sys.argv)>2 else datetime.now()+timedelta(days=(7-datetime.now().weekday())%7 or 7)
    posts=build(weeks,start); stamp=start.strftime("%Y-%m-%d"); here=Path(__file__).parent
    (here/f"calendar-fbig-{stamp}.json").write_text(json.dumps(posts,indent=2,ensure_ascii=False),encoding="utf-8")
    (here/f"preview-fbig-{stamp}.html").write_text(preview(posts),encoding="utf-8")
    print(f"{len(posts)} FB+IG posts -> calendar-fbig-{stamp}.json + preview-fbig-{stamp}.html")

if __name__=="__main__": main()
