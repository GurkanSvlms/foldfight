"""Builds the Foldfight site (English at the root, Turkish under /tr/).

    python3 build.py

Pages: index.html, privacy.html, support.html. Everything is static for GitHub Pages.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://gurkansvlms.github.io/foldfight"
APP_URL = "https://apps.apple.com/app/id6833807721"
EMAIL = "playauragames@gmail.com"
UPDATED = {"en": "13 November 2026", "tr": "13 Kasım 2026"}

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

T = {
    "en": {
        "lang": "en", "dir": "", "title": "Foldfight — two-player games for one phone",
        "desc": "Seven quick duels for two people and one phone. On iPhone Duo the hinge is your controller; on every other iPhone and iPad you play by touch.",
        "tag1": "FOLD", "tag2": "FIGHT", "lead": "Two players, one phone. Seven quick duels — and on iPhone Duo, the hinge is your controller.",
        "cta": "Download on the App Store", "ctanote": "Free to try. One purchase unlocks every game.",
        "games_h": "Seven games. <em>One phone.</em>", "games_sub": "Put the phone between you. Each half belongs to one player.",
        "free": "FREE", "hinge": "HINGE", "flat": "FLAT",
        "g": {
            "fuse": ("FUSE", "Close the phone a little every pass and hand it over. Shut it, stall or pass too soon and you lose."),
            "hunt": ("ANGLE HUNT", "A secret angle appears. Fold to it with no gauge and lock it in. Closest over three rounds wins."),
            "reflex": ("REFLEX", "Wait for “TAP!” and beat your rival to it. Tap early and the round is theirs."),
            "tug": ("TUG OF WAR", "Tap your half faster than your rival and drag the knot to your edge."),
            "math": ("QUICK MATH", "Same sum on both halves. First right answer scores; a wrong one benches you."),
            "trap": ("COLOR TRAP", "Tap only when the word matches its colour. Fall for a trap and lose a point."),
            "hockey": ("MINI HOCKEY", "Paddles on each half, puck across the middle. First to five goals."),
        },
        "shots_h": "See it <em>in play</em>",
        "how_h": "How it <em>works</em>",
        "how": [("Pick a game", "Fuse is free. One purchase unlocks the other six, now and later."),
                ("Put the phone between you", "Flat on the table, or half-folded on iPhone Duo for the hinge games."),
                ("Settle it", "Best of five, first to five, or the last one standing. Tonight’s score keeps count.")],
        "duo_h": "Made for <em>iPhone Duo</em>",
        "duo_p": "Fuse and Angle Hunt read the real hinge angle. Every other iPhone and iPad plays them by touch, so everyone can join in.",
        "privacy": "Privacy", "support": "Support", "other_lang": ("Türkçe", "/foldfight/tr/"),
        "rights": "© 2026 Aura Games. iPhone is a trademark of Apple Inc.",
        "privacy_title": "Privacy Policy",
        "privacy_body": f"""
<p><strong>Foldfight collects no personal data.</strong> There are no accounts, no ads, no analytics and no tracking.</p>
<h2>What stays on your device</h2>
<ul><li>The two player names you type, so you don't have to enter them again. They never leave the device and you can change or clear them any time.</li>
<li>Tonight's score, which is kept only while the app is open.</li></ul>
<h2>Purchases</h2>
<p>The one-time “Unlock All Games” purchase is handled entirely by Apple through the App Store. We never see your payment details. The app asks StoreKit on your device whether the purchase exists.</p>
<h2>The hinge</h2>
<p>On iPhone Duo the app reads the hinge angle on the device to run Fuse and Angle Hunt. The angle is used only while you play and is not stored or sent anywhere.</p>
<h2>Children</h2>
<p>Foldfight does not collect data from anyone, including children.</p>
<h2>Changes and contact</h2>
<p>If this policy changes, the new version will appear on this page with a new date. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>""",
        "support_title": "Support",
        "support_intro": f"Something not working, or an idea for a new game? Write to <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. We usually answer within two days.",
        "faq": [
            ("How do I restore my purchase?", "Tap any locked game, then “Restore purchase” under the unlock button. Use the same Apple Account you bought with."),
            ("Do I need an iPhone Duo?", "No. Every game works on every iPhone and iPad with iOS 27 or later. On iPhone Duo, Fuse and Angle Hunt use the real hinge instead of the on-screen arc."),
            ("How do two people play on one phone?", "Lay the phone flat between you. Each half of the screen belongs to one player and the text on it faces that player."),
            ("Is there a subscription or ads?", "No. Fuse is free. One purchase unlocks all games, including the ones we add later."),
            ("Can I change the player names?", "Yes. Tap “Edit names” on the home screen."),
            ("Does the app work offline?", "Yes. Everything runs on the phone; only the purchase talks to the App Store."),
        ],
        "faq_h": "Questions",
    },
    "tr": {
        "lang": "tr", "dir": "", "title": "Foldfight — tek telefonda iki kişilik oyunlar",
        "desc": "İki kişi ve tek telefon için yedi hızlı düello. iPhone Duo'da menteşe kumandan olur; diğer tüm iPhone ve iPad'lerde dokunarak oynarsın.",
        "tag1": "FOLD", "tag2": "FIGHT", "lead": "İki oyuncu, tek telefon. Yedi hızlı düello — iPhone Duo'da ise menteşe senin kumandan.",
        "cta": "App Store'dan indir", "ctanote": "Ücretsiz dene. Tek satın alma tüm oyunları açar.",
        "games_h": "Yedi oyun. <em>Tek telefon.</em>", "games_sub": "Telefonu aranıza koyun. Ekranın her yarısı bir oyuncunun.",
        "free": "ÜCRETSİZ", "hinge": "MENTEŞE", "flat": "DÜZ",
        "g": {
            "fuse": ("FUSE", "Her turda telefonu biraz daha kapat ve karşıya ver. Kapatan, oyalanan ya da erken devreden kaybeder."),
            "hunt": ("ANGLE HUNT", "Gizli bir açı çıkar. Gösterge olmadan o açıya katla ve kilitle. Üç turda en yakın olan kazanır."),
            "reflex": ("REFLEX", "“DOKUN!” yazısını bekle ve rakibinden önce dokun. Erken dokunursan tur onun."),
            "tug": ("HALAT ÇEKME", "Kendi yarına rakibinden hızlı dokun, düğümü kendi kenarına çek."),
            "math": ("HIZLI HESAP", "İki yarıda aynı işlem. İlk doğru cevap puan alır; yanlış cevap seni bir tur dışarıda bırakır."),
            "trap": ("RENK TUZAĞI", "Yalnızca kelime kendi rengindeyken dokun. Tuzağa düşersen puan kaybedersin."),
            "hockey": ("MİNİ HOKEY", "Her yarıda bir raket, ortadan geçen bir pak. Beş gol atan kazanır."),
        },
        "shots_h": "Oyundan <em>kareler</em>",
        "how_h": "Nasıl <em>oynanır</em>",
        "how": [("Bir oyun seç", "Fuse ücretsiz. Tek satın alma diğer altı oyunu ve gelecek oyunları açar."),
                ("Telefonu aranıza koyun", "Masaya düz koyun; menteşe oyunlarında iPhone Duo'yu yarıya katlayın."),
                ("Kazananı belirleyin", "Beş turun en iyisi, beşe ilk ulaşan ya da son kalan. Bu geceki skor tutulur.")],
        "duo_h": "<em>iPhone Duo</em> için yapıldı",
        "duo_p": "Fuse ve Angle Hunt gerçek menteşe açısını okur. Diğer tüm iPhone ve iPad'lerde dokunarak oynanır, böylece herkes katılabilir.",
        "privacy": "Gizlilik", "support": "Destek", "other_lang": ("English", "/foldfight/"),
        "rights": "© 2026 Aura Games. iPhone, Apple Inc.'in ticari markasıdır.",
        "privacy_title": "Gizlilik Politikası",
        "privacy_body": f"""
<p><strong>Foldfight hiçbir kişisel veri toplamaz.</strong> Hesap, reklam, analiz ya da takip yoktur.</p>
<h2>Cihazında kalanlar</h2>
<ul><li>Yazdığın iki oyuncu adı, tekrar girmemen için. Cihazdan hiç çıkmaz; istediğin zaman değiştirebilir ya da silebilirsin.</li>
<li>Bu geceki skor; yalnızca uygulama açıkken tutulur.</li></ul>
<h2>Satın almalar</h2>
<p>Tek seferlik “Tüm Oyunları Aç” satın alması tamamen Apple tarafından App Store üzerinden yapılır. Ödeme bilgilerini hiçbir zaman görmeyiz. Uygulama satın almanın olup olmadığını cihazdaki StoreKit'e sorar.</p>
<h2>Menteşe</h2>
<p>iPhone Duo'da uygulama, Fuse ve Angle Hunt için cihazdaki menteşe açısını okur. Açı yalnızca oyun sırasında kullanılır; saklanmaz ve hiçbir yere gönderilmez.</p>
<h2>Çocuklar</h2>
<p>Foldfight, çocuklar dahil kimseden veri toplamaz.</p>
<h2>Değişiklikler ve iletişim</h2>
<p>Bu politika değişirse yeni hâli bu sayfada yeni tarihle yayımlanır. Sorular için: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>""",
        "support_title": "Destek",
        "support_intro": f"Bir şey çalışmıyor mu, yeni bir oyun fikrin mi var? <a href=\"mailto:{EMAIL}\">{EMAIL}</a> adresine yaz. Genellikle iki gün içinde yanıtlıyoruz.",
        "faq": [
            ("Satın alımımı nasıl geri yüklerim?", "Kilitli bir oyuna dokun, ardından açma düğmesinin altındaki “Satın alımı geri yükle”ye dokun. Satın aldığın Apple Hesabı ile giriş yapmış olmalısın."),
            ("iPhone Duo şart mı?", "Hayır. Tüm oyunlar iOS 27 ve sonrası olan her iPhone ve iPad'de çalışır. iPhone Duo'da Fuse ve Angle Hunt, ekrandaki yay yerine gerçek menteşeyi kullanır."),
            ("İki kişi tek telefonda nasıl oynar?", "Telefonu aranıza düz koyun. Ekranın her yarısı bir oyuncunun ve yazılar o oyuncuya dönük."),
            ("Abonelik ya da reklam var mı?", "Hayır. Fuse ücretsiz. Tek satın alma, sonradan eklenecekler dahil tüm oyunları açar."),
            ("Oyuncu adlarını değiştirebilir miyim?", "Evet. Ana ekranda “Adları düzenle”ye dokun."),
            ("İnternetsiz çalışır mı?", "Evet. Her şey telefonda çalışır; yalnızca satın alma App Store ile konuşur."),
        ],
        "faq_h": "Sık sorulanlar",
    },
}


def page(t, path, title, desc, body, prefix):
    canon = f"{BASE}/{'' if t['lang'] == 'en' else 'tr/'}{path}"
    other = f"{BASE}/{'tr/' if t['lang'] == 'en' else ''}{path}"
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "MobileApplication", "name": "Foldfight",
        "operatingSystem": "iOS 27.0 or later", "applicationCategory": "GameApplication",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "downloadUrl": APP_URL, "inLanguage": t["lang"], "description": t["desc"],
    }, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="{t['lang']}" href="{canon}">
<link rel="alternate" hreflang="{'tr' if t['lang'] == 'en' else 'en'}" href="{other}">
<link rel="alternate" hreflang="x-default" href="{BASE}/{path}">
<meta name="apple-itunes-app" content="app-id=6833807721">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/assets/og.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0B12">
<link rel="icon" href="{prefix}assets/favicon.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{prefix}assets/site.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="wrap top">
  <a class="brand" href="{prefix}{'' if t['lang'] == 'en' else 'tr/'}"><img src="{prefix}assets/icon-256.png" alt="">Foldfight</a>
  <nav class="nav"><a class="chip" href="{t['other_lang'][1]}{path}" hreflang="{'tr' if t['lang'] == 'en' else 'en'}">{t['other_lang'][0]}</a></nav>
</header>
<main>
{body}
</main>
<footer><div class="wrap">
  <span>{t['rights']}</span>
  <nav><a href="{prefix}{'' if t['lang'] == 'en' else 'tr/'}privacy.html">{t['privacy']}</a><a href="{prefix}{'' if t['lang'] == 'en' else 'tr/'}support.html">{t['support']}</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""


def home(t, prefix):
    g = t["g"]
    cards = "\n".join(
        f'<article class="game" style="background:{ground};--glow:{glow}"><span class="tag{" free" if free else ""}">'
        f'{t["free"] + " · " if free else ""}{t["hinge"] if k in ("fuse", "hunt") else t["flat"]}</span>'
        f'<h3>{g[k][0]}</h3><p>{g[k][1]}</p></article>'
        for k, ground, glow, free in GAMES)
    shots = "\n".join(f'<img src="{prefix}assets/shots/{t["lang"]}-{s}.jpg" alt="" loading="lazy" width="414" height="900">' for s in SHOTS)
    steps = "\n".join(f'<div class="card"><span class="num">{i + 1}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(t["how"]))
    return f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <img class="mascot" src="{prefix}assets/mascot.png" alt="Foldfight mascot" width="150" height="125">
    <h1>{t['tag1']}<span>{t['tag2']}</span></h1>
    <p class="lead">{t['lead']}</p>
    <div class="cta"><a class="pill" href="{APP_URL}">{t['cta']}</a><span class="note">{t['ctanote']}</span></div>
  </div>
  <img class="hero-shot" src="{prefix}assets/shots/{t['lang']}-01-reflex.jpg" alt="" width="414" height="900">
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
    for lang, t in T.items():
        out = HERE if lang == "en" else os.path.join(HERE, "tr")
        prefix = "" if lang == "en" else "../"
        os.makedirs(out, exist_ok=True)
        pages = {
            "index.html": (t["title"], t["desc"], home(t, prefix)),
            "privacy.html": (f"{t['privacy_title']} — Foldfight", t["privacy_title"],
                             f'<div class="wrap doc"><h1>{t["privacy_title"]}</h1><p>{UPDATED[lang]}</p>{t["privacy_body"]}</div>'),
            "support.html": (f"{t['support_title']} — Foldfight", t["support_title"],
                             f'<div class="wrap doc"><h1>{t["support_title"]}</h1><p>{t["support_intro"]}</p><h2>{t["faq_h"]}</h2>'
                             + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"]) + "</div>"),
        }
        for name, (title, desc, body) in pages.items():
            with open(os.path.join(out, name), "w") as f:
                f.write(page(t, "" if name == "index.html" else name, title, desc, body, prefix))
    with open(os.path.join(HERE, "404.html"), "w") as f:
        f.write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/foldfight/"><title>Foldfight</title>')
    with open(os.path.join(HERE, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    urls = [f"{BASE}/{p}" for p in ("", "privacy.html", "support.html", "tr/", "tr/privacy.html", "tr/support.html")]
    with open(os.path.join(HERE, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print("built")


if __name__ == "__main__":
    main()
