"""Builds the Foldfight site in 12 languages (English at the root, others under /<code>/).

    python3 build.py

Pages: index.html, privacy.html, support.html. Everything is static for GitHub Pages.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://gurkansvlms.github.io/foldfight"
APP_URL = "https://apps.apple.com/app/id6833807721"
EMAIL = "playauragames@gmail.com"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

GAMES = [  # key, ground, glow, free
    ("fuse", "#3B0D0A", "rgba(255,90,31,.9)", True),
    ("hunt", "#0A1F5C", "rgba(47,123,255,.9)", False),
    ("reflex", "#0B3B24", "rgba(43,214,123,.85)", False),
    ("tug", "#2A0E4A", "rgba(180,76,255,.85)", False),
    ("math", "#06343A", "rgba(19,181,166,.85)", False),
    ("trap", "#1C1340", "rgba(106,76,255,.85)", False),
    ("hockey", "#0E2233", "rgba(30,144,255,.85)", False),
]
SHOTS = ["01-reflex", "02-fuse", "03-hockey", "04-tug", "05-hunt", "06-math", "07-trap", "08-result"]

from locales import LANGS, T


def url(code, path):
    seg = LANGS[code][0]
    return f"{BASE}/{seg + '/' if seg else ''}{path}"


def rel(code, path):
    seg = LANGS[code][0]
    return f"/foldfight/{seg + '/' if seg else ''}{path}"


def page(code, path, title, desc, body, prefix):
    t = T[code]
    seg, lang, direction, _ = LANGS[code]
    alternates = "\n".join(f'<link rel="alternate" hreflang="{LANGS[c][1]}" href="{url(c, path)}">' for c in LANGS)
    current = ' aria-current="page"'
    switch = "".join(f'<a href="{rel(c, path)}" hreflang="{LANGS[c][1]}" lang="{LANGS[c][1]}"{current if c == code else ""}>{LANGS[c][3]}</a>' for c in LANGS)
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "MobileApplication", "name": "Foldfight",
        "operatingSystem": "iOS 27.0 or later", "applicationCategory": "GameApplication",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "downloadUrl": APP_URL, "inLanguage": lang, "description": t["desc"],
    }, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{lang}" dir="{direction}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(code, path)}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{url('en', path)}">
<meta name="apple-itunes-app" content="app-id=6833807721">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/assets/og.jpg">
<meta property="og:type" content="website">
<meta property="og:locale" content="{lang.replace('-', '_')}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0B12">
<link rel="icon" href="{prefix}assets/favicon.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{prefix}assets/site.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="wrap top">
  <a class="brand" href="{rel(code, '')}"><img src="{prefix}assets/icon-256.png" alt="">Foldfight</a>
  <details class="langs"><summary class="chip">{LANGS[code][3]}</summary><nav aria-label="{t['languages']}">{switch}</nav></details>
</header>
<main>
{body}
</main>
<footer><div class="wrap">
  <span>{t['rights']}</span>
  <nav><a href="{rel(code, 'privacy.html')}">{t['privacy_word']}</a><a href="{rel(code, 'support.html')}">{t['support_word']}</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""


def home(code, prefix):
    t = T[code]
    g = t["g"]
    cards = "\n".join(
        f'<article class="game" style="background:{ground};--glow:{glow}"><span class="tag{" free" if free else ""}">'
        f'{t["free"] + " · " if free else ""}{t["hinge"] if k in ("fuse", "hunt") else t["flat"]}</span>'
        f'<h3>{g[k][0]}</h3><p>{g[k][1]}</p></article>'
        for k, ground, glow, free in GAMES)
    shots = "\n".join(f'<img src="{prefix}assets/shots/{code}-{s}.jpg" alt="" loading="lazy" width="414" height="900">' for s in SHOTS)
    steps = "\n".join(f'<div class="card"><span class="num">{i + 1}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(t["how"]))
    return f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <img class="mascot" src="{prefix}assets/mascot.png" alt="Foldfight mascot" width="150" height="125">
    <h1>FOLD<span>FIGHT</span></h1>
    <p class="lead">{t['lead']}</p>
    <div class="cta"><a class="pill" href="{APP_URL}">{t['cta']}</a><span class="note">{t['ctanote']}</span></div>
  </div>
  <img class="hero-shot" src="{prefix}assets/shots/{code}-01-reflex.jpg" alt="" width="414" height="900">
</div></section>
<section><div class="wrap">
  <h2>{t['games_h']}</h2><p class="sub">{t['games_sub']}</p>
  <div class="games">{cards}</div>
</div></section>
<section><div class="wrap">
  <h2>{t['shots_h']}</h2>
  <div class="strip">{shots}</div>
</div></section>
<section><div class="wrap">
  <h2>{t['how_h']}</h2>
  <div class="steps">{steps}</div>
</div></section>
<section><div class="wrap">
  <h2>{t['duo_h']}</h2><p class="sub">{t['duo_p']}</p>
  <a class="pill" href="{APP_URL}">{t['cta']}</a>
</div></section>"""


def main():
    for code in LANGS:
        t = T[code]
        seg = LANGS[code][0]
        out = os.path.join(HERE, seg) if seg else HERE
        prefix = "../" if seg else ""
        os.makedirs(out, exist_ok=True)
        privacy = "".join((f"<h2>{h}</h2>" if h else "") + f"<p>{p.format(email=MAIL)}</p>" for h, p in t["privacy"])
        pages = {
            "index.html": (t["title"], t["desc"], home(code, prefix)),
            "privacy.html": (f"{t['privacy_title']} — Foldfight", t["privacy_title"],
                             f'<div class="wrap doc"><h1>{t["privacy_title"]}</h1><p>{t["updated"]}</p>{privacy}</div>'),
            "support.html": (f"{t['support_title']} — Foldfight", t["support_title"],
                             f'<div class="wrap doc"><h1>{t["support_title"]}</h1><p>{t["support_intro"].format(email=MAIL)}</p><h2>{t["faq_h"]}</h2>'
                             + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"]) + "</div>"),
        }
        for name, (title, desc, body) in pages.items():
            with open(os.path.join(out, name), "w") as f:
                f.write(page(code, "" if name == "index.html" else name, title, desc, body, prefix))
    with open(os.path.join(HERE, "404.html"), "w") as f:
        f.write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/foldfight/"><title>Foldfight</title>')
    with open(os.path.join(HERE, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    urls = [url(c, p) for c in LANGS for p in ("", "privacy.html", "support.html")]
    with open(os.path.join(HERE, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print("built")


if __name__ == "__main__":
    main()
