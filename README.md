# BVA Flooring — bvaflooring.com

Static, SEO/GEO-optimized website for **BVA Services Corp** (BVA Flooring), a flooring
installer serving Bradenton, Sarasota, Lakewood Ranch & the Tampa Bay Gulf Coast.

Built to be deployed on **Cloudflare Pages**.

## Structure

- `build.py` — site constants (NAP, services, cities) + shared components & schema helpers
- `content.py` — page bodies, original copy, pricing, FAQs, blog posts
- `previews.py` — design mockups only (NOT deployed; ignored by git)
- Generated output (committed): `index.html`, `/about/`, `/contact/`, `/thanks/`, `404.html`,
  6 service indexes, 8 city hubs, 48 service×city pages, `/blog/` + posts,
  `sitemap.xml`, `robots.txt`, `_headers`, `_redirects`, `images/logo.svg`

## Build

```bash
py build.py          # regenerates all HTML from build.py + content.py
```
On Windows, prefix with `PYTHONIOENCODING=utf-8` so console output renders.

## Business facts (single source of truth: build.py)

- Brand: **BVA Flooring** · Legal: **BVA Services Corp** · Founded **2020**
- Phone **(941) 807-0339** · Email **bvaservicecorporation@gmail.com**
- NAP address shown as **Bradenton, FL 34208** (street hidden by owner request)
- No license number on file · 5★ shown visually only (kept out of JSON-LD until real reviews exist)
- Proprietary process: **BVA 52-Point Floor-Ready Standard**

## Services × Cities

Services: hardwood-flooring, vinyl-plank-flooring, tile-installation, laminate-flooring,
stair-treads, floor-repair.
Cities: bradenton, sarasota, lakewood-ranch, palmetto, parrish, venice, tampa, st-petersburg.

## Deploy (Cloudflare Pages)

1. Create a GitHub repo and push this folder (`previews/` is git-ignored).
2. Cloudflare Pages → Create project → connect the repo.
3. Build command: *(none — static)*. Build output directory: `/` (root).
4. Add custom domain **bvaflooring.com** (already on Cloudflare).
5. Submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools.

## To do (next)

- AI / project photos for hero + service cards (replace icon placeholders)
- Automated blog pipeline (adapted from the Triangle Flooring automation; needs Anthropic API key + cadence)
