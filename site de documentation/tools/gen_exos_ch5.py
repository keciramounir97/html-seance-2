# -*- coding: utf-8 -*-
"""Compact banks for chapters 5–13."""
from gen_exos import T, Q, P, o, make_ch

def B(id_, file_, title, trows, prows):
    make_ch(id_, file_, T(*title), [Q(*r) for r in trows], [P(*r) for r in prows])

def R(qf, qe, qa, cf, ce, ca, w, af, ae, aa, whyf, whye, whya, ai=0):
    opts = [o(cf, ce, ca)] + [o(*x) for x in w]
    # rotate so answer index = ai
    if ai:
        opts = opts[1:ai] + [opts[0]] + opts[ai:] if False else opts
    return (qf, qe, qa, opts if ai == 0 else None)


# Simpler: keep answer index explicit

def tq(qf, qe, qa, options, a, wf, we, wa):
    return (qf, qe, qa, options, a, wf, we, wa)

def pr(task, starter, solution, hint):
    return (task, starter, solution, hint)

# ========== 5 ==========
make_ch("chapitre-5", "chapitre-5.md", T("Chapitre 5 — Attributs, liens, images", "Chapter 5 — Attributes, links, images", "الفصل 5 — السمات والروابط والصور"),
[
    Q("Un attribut s’écrit :", "An attribute is written:", "تُكتب السمة:",
      [o("dans la balise fermante", "on the closing tag", "في وسم الإغلاق"), o("nom=\"valeur\" dans la balise ouvrante", "name=\"value\" on the opening tag", "name=\"value\" في الوسم الافتتاحي"), o("après </html>", "after </html>", "بعد </html>"), o("dans un commentaire seulement", "in a comment only", "في تعليق فقط")], 1, "Toujours la balise ouvrante.", "Always the opening tag.", "دائمًا الوسم الافتتاحي."),
    Q("href sert à :", "href is for:", "href لـ:",
      [o("l’adresse du lien", "the link address", "عنوان الرابط"), o("une image locale seulement", "a local image only", "صورة محلية فقط"), o("un saut de ligne", "a line break", "سطر جديد"), o("un titre d’onglet", "a tab title", "عنوان تبويب")], 0, "hypertext reference.", "hypertext reference.", "مرجع النص التشعبي."),
    Q("target=\"_blank\" :", "target=\"_blank\":", "target=\"_blank\":",
      [o("ouvre un nouvel onglet", "opens a new tab", "يفتح تبويبًا جديدًا"), o("met en gras", "makes bold", "يجعل غامقًا"), o("ajoute UTF-8", "adds UTF-8", "يضيف UTF-8"), o("crée un ul", "creates a ul", "ينشئ ul")], 0, "Garde la page actuelle ouverte.", "Keeps the current page open.", "يبقي الصفحة الحالية مفتوحة."),
    Q("src sur img :", "src on img:", "src على img:",
      [o("chemin ou URL de l’image", "image path or URL", "مسار أو رابط الصورة"), o("texte alternatif", "alternative text", "النص البديل"), o("infobulle", "tooltip", "تلميح"), o("lien hypertexte", "hyperlink", "رابط")], 0, "source du fichier.", "file source.", "مصدر الملف."),
    Q("alt sert à :", "alt is for:", "alt لـ:",
      [o("décrire l’image (accessibilité + image cassée)", "describe the image (a11y + broken image)", "وصف الصورة (إتاحة + صورة مكسورة)"), o("ouvrir YouTube", "open YouTube", "فتح يوتيوب"), o("numéroter une liste", "number a list", "ترقيم قائمة"), o("remplacer head", "replace head", "تعويض head")], 0, "Obligatoire pour une image correcte.", "Required for a proper image.", "ضروري لصورة صحيحة."),
    Q("title (attribut) :", "title (attribute):", "title (سمة):",
      [o("infobulle au survol", "hover tooltip", "تلميح عند المرور"), o("texte de l’onglet", "tab text", "نص التبويب"), o("un iframe", "an iframe", "iframe"), o("un dl", "a dl", "dl")], 0, "Ne pas confondre avec l’élément title.", "Do not confuse with the title element.", "لا تخلطه مع عنصر title."),
    Q("Sans href, a :", "Without href, a:", "بدون href، a:",
      [o("ne mène nulle part", "goes nowhere", "لا يذهب لأي مكان"), o("devient une video", "becomes a video", "يصبح فيديو"), o("est un h1", "is an h1", "h1"), o("est vide comme br", "is empty like br", "فارغ مثل br")], 0, "href est essentiel.", "href is essential.", "href أساسي."),
    Q("width et height sur img :", "width and height on img:", "width و height على img:",
      [o("tailles d’affichage", "display sizes", "أحجام العرض"), o("couleur", "color", "لون"), o("UTF-8", "UTF-8", "UTF-8"), o("target", "target", "target")], 0, "Pixels souvent.", "Often pixels.", "بكسل غالبًا."),
    Q("class et id :", "class and id:", "class و id:",
      [o("identifient / groupent pour le CSS plus tard", "identify / group for later CSS", "تعرّف / تجمّع لـ CSS لاحقًا"), o("lisent le MP3", "play MP3", "تشغّل MP3"), o("sont des listes", "are lists", "قوائم"), o("vont dans DOCTYPE", "go in DOCTYPE", "في DOCTYPE")], 0, "Attributs globaux.", "Global attributes.", "سمات عامة."),
    Q("Un lien interne vers index.html :", "An internal link to index.html:", "رابط داخلي إلى index.html:",
      [o("<a href=\"index.html\">Accueil</a>", "<a href=\"index.html\">Home</a>", "<a href=\"index.html\">الرئيسية</a>"), o("<img href=\"index.html\">", "<img href=\"index.html\">", "<img href=\"index.html\">"), o("<p src=\"index.html\">", "<p src=\"index.html\">", "<p src=\"index.html\">"), o("<br href=\"index.html\">", "<br href=\"index.html\">", "<br href=\"index.html\">")], 0, "a + href fichier local.", "a + href local file.", "a + href ملف محلي."),
    Q("img est :", "img is:", "img هو:",
      [o("vide", "empty", "فارغ"), o("un titre", "a heading", "عنوان"), o("un ol", "an ol", "ol"), o("un head", "a head", "head")], 0, "Pas de </img>.", "No </img>.", "لا </img>."),
    Q("On peut mettre une image dans un lien :", "We can put an image inside a link:", "يمكن وضع صورة داخل رابط:",
      [o("oui : a enveloppe img", "yes: a wraps img", "نعم: a يلف img"), o("jamais", "never", "أبدًا"), o("seulement dans head", "only in head", "في head فقط"), o("seulement avec audio", "only with audio", "مع audio فقط")], 0, "Image cliquable.", "Clickable image.", "صورة قابلة للنقر."),
    Q("https:// est :", "https:// is:", "https:// هو:",
      [o("une URL absolue (site externe)", "an absolute URL (external site)", "رابط مطلق (موقع خارجي)"), o("un commentaire", "a comment", "تعليق"), o("un favicon obligatoire", "a required favicon", "أيقونة إلزامية"), o("un h6", "an h6", "h6")], 0, "Vers un autre site.", "To another site.", "إلى موقع آخر."),
    Q("alt vide alt=\"\" :", "Empty alt=\"\":", "alt فارغ alt=\"\":",
      [o("image décorative (acceptable parfois)", "decorative image (sometimes ok)", "صورة زخرفية (أحيانًا مقبول)"), o("crée une video", "creates a video", "ينشئ فيديو"), o("est href", "is href", "هو href"), o("ouvre un onglet", "opens a tab", "يفتح تبويبًا")], 0, "Sinon décrire vraiment.", "Otherwise really describe it.", "وإلا صفها حقًا."),
    Q("L’ordre des attributs :", "Attribute order:", "ترتيب السمات:",
      [o("libre, tous dans la balise ouvrante", "free, all on the opening tag", "حر، كلها في الوسم الافتتاحي"), o("href après la balise fermante", "href after the closing tag", "href بعد الإغلاق"), o("alt dans head", "alt in head", "alt في head"), o("src dans title onglet", "src in the tab title", "src في عنوان التبويب")], 0, "src, alt, title, width…", "src, alt, title, width…", "src و alt و title و width…"),
    Q("Un lien sans texte visible :", "A link without visible text:", "رابط بلا نص ظاهر:",
      [o("est peu accessible (mettre un texte ou un alt d’image)", "is poorly accessible (add text or image alt)", "ضعيف الإتاحة (أضف نصًا أو alt)"), o("est obligatoire", "is required", "إلزامي"), o("remplace charset", "replaces charset", "يعوّض charset"), o("crée dl", "creates dl", "ينشئ dl")], 0, "Toujours un contenu cliquable clair.", "Always a clear clickable content.", "محتوى قابل للنقر واضح دائمًا."),
    Q("target par défaut :", "Default target:", "target الافتراضي:",
      [o("même onglet", "same tab", "نفس التبويب"), o("_blank", "_blank", "_blank"), o("une video", "a video", "فيديو"), o("head", "head", "head")], 0, "Sans target = même page.", "No target = same page.", "بدون target = نفس الصفحة."),
    Q("photo.png dans images/ :", "photo.png in images/:", "photo.png في images/:",
      [o("src=\"images/photo.png\"", "src=\"images/photo.png\"", "src=\"images/photo.png\""), o("href=\"images/photo.png\" sur img", "href=\"images/photo.png\" on img", "href=\"images/photo.png\" على img"), o("alt=\"images/photo.png\" seulement", "alt=\"images/photo.png\" only", "alt=\"images/photo.png\" فقط"), o("src dans a", "src on a", "src على a")], 0, "src pour img, href pour a.", "src for img, href for a.", "src لـ img و href لـ a."),
    Q("title sur img :", "title on img:", "title على img:",
      [o("infobulle, en plus de alt", "tooltip, in addition to alt", "تلميح إضافة إلى alt"), o("remplace src", "replaces src", "يعوّض src"), o("est un h1", "is an h1", "h1"), o("ouvre YouTube", "opens YouTube", "يفتح يوتيوب")], 0, "alt ≠ title.", "alt ≠ title.", "alt ≠ title."),
    Q("a est l’abréviation de :", "a is short for:", "a اختصار لـ:",
      [o("anchor", "anchor", "مرساة"), o("audio", "audio", "صوت"), o("article", "article", "مقال"), o("aside", "aside", "جانب")], 0, "Ancre / hyperlien.", "Anchor / hyperlink.", "مرساة / رابط."),
],
[
    P(("Lien Google.", "Google link.", "رابط جوجل."), "", "<a href=\"https://www.google.com\">Google</a>", ("a href", "a href", "a href")),
    P(("Nouvel onglet.", "New tab.", "تبويب جديد."), "<a href=\"https://www.google.com\">Google</a>", "<a href=\"https://www.google.com\" target=\"_blank\">Google</a>", ("target", "target", "target")),
    P(("Infobulle sur p.", "Tooltip on p.", "تلميح على p."), "<p>Karim</p>", "<p title=\"Vendeur\">Karim</p>", ("title", "title", "title")),
    P(("Image avec alt.", "Image with alt.", "صورة مع alt."), "", "<img src=\"images/image.png\" alt=\"Téléphone à Oran\">", ("img", "img", "img")),
    P(("Image 200×120.", "Image 200×120.", "صورة 200×120."), "<img src=\"a.png\" alt=\"a\">", "<img src=\"a.png\" alt=\"a\" width=\"200\" height=\"120\">", ("width height", "width height", "width height")),
    P(("Image dans un lien.", "Image inside a link.", "صورة داخل رابط."), "<img src=\"html.png\" alt=\"HTML\">", "<a href=\"https://www.w3schools.com\"><img src=\"html.png\" alt=\"HTML\"></a>", ("a autour.", "a around.", "a حولها.")),
    P(("Lien interne about.html.", "Internal link about.html.", "رابط داخلي about.html."), "", "<a href=\"about.html\">À propos</a>", ("href local.", "local href.", "href محلي.")),
    P(("alt + title sur img.", "alt + title on img.", "alt + title على img."), "<img src=\"v.png\">", "<img src=\"v.png\" alt=\"Peugeot 208\" title=\"1 850 000 DA\">", ("deux attributs.", "two attributes.", "سمتان.")),
    P(("class sur img.", "class on img.", "class على img."), "<img src=\"v.png\" alt=\"v\">", "<img src=\"v.png\" alt=\"v\" class=\"annonce\">", ("class", "class", "class")),
    P(("id unique.", "Unique id.", "id فريد."), "<img src=\"v.png\" alt=\"v\">", "<img src=\"v.png\" alt=\"v\" id=\"photo-principale\">", ("id", "id", "id")),
    P(("Corrige href sur img.", "Fix href on img.", "صحّح href على img."), "<img href=\"a.png\" alt=\"a\">", "<img src=\"a.png\" alt=\"a\">", ("src pas href.", "src not href.", "src لا href.")),
    P(("Corrige src sur a.", "Fix src on a.", "صحّح src على a."), "<a src=\"https://www.google.com\">Google</a>", "<a href=\"https://www.google.com\">Google</a>", ("href", "href", "href")),
    P(("Menu de 2 liens.", "Menu of 2 links.", "قائمة من رابطين."), "", "<p><a href=\"index.html\">Accueil</a> | <a href=\"contact.html\">Contact</a></p>", ("deux a.", "two a.", "a اثنان.")),
    P(("Image + paragraphe title.", "Image + paragraph title.", "صورة + title للفقرة."), "", "<p title=\"Fiche\">Galaxy A54</p>\n<img src=\"images/image.png\" alt=\"Galaxy A54\">", ("p + img.", "p + img.", "p + img.")),
    P(("Lien Facebook nouvel onglet.", "Facebook link new tab.", "رابط فيسبوك تبويب جديد."), "", "<a href=\"https://www.facebook.com\" target=\"_blank\">Facebook</a>", ("_blank", "_blank", "_blank")),
    P(("width 280 height 160.", "width 280 height 160.", "width 280 height 160."), "<img src=\"p.png\" alt=\"p\">", "<img src=\"p.png\" alt=\"p\" width=\"280\" height=\"160\">", ("nombres.", "numbers.", "أرقام.")),
    P(("Trois attributs img.", "Three img attributes.", "ثلاث سمات img."), "<img>", "<img src=\"p.png\" alt=\"Annonce\" title=\"A54\">", ("src alt title", "src alt title", "src alt title")),
    P(("Texte du lien clair.", "Clear link text.", "نص رابط واضح."), "<a href=\"https://www.google.com\">clique ici</a>", "<a href=\"https://www.google.com\">Rechercher sur Google</a>", ("éviter « clique ici ».", "avoid “click here”.", "تجنّب «انقر هنا».")),
    P(("Chemin images/image2.png.", "Path images/image2.png.", "مسار images/image2.png."), "<img alt=\"2\">", "<img src=\"images/image2.png\" alt=\"Annonce 2\">", ("src", "src", "src")),
    P(("Mini fiche : p title, lien blank, img.", "Mini card: p title, blank link, img.", "بطاقة: p title ورابط blank و img."), "", "<p title=\"Vendeur\">Karim — Alger</p>\n<a href=\"https://www.google.com\" target=\"_blank\">Google</a>\n<img src=\"images/image.png\" alt=\"Annonce Alger\">", ("les 3 idées du chapitre.", "the 3 chapter ideas.", "أفكار الفصل الثلاث.")),
])

print("ch5", len.__name__)
