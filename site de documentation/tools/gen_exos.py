# -*- coding: utf-8 -*-
"""Generate exos/*.md and js/exercises.js (FR / EN / AR)."""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXOS = os.path.join(ROOT, "exos")
JS = os.path.join(ROOT, "site de documentation", "js", "exercises.js")
os.makedirs(EXOS, exist_ok=True)


def T(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


def Q(fr, en, ar, opts, a, why_fr, why_en, why_ar):
    return {
        "q": T(fr, en, ar),
        "options": [T(*o) if isinstance(o, tuple) else o for o in opts],
        "a": a,
        "why": T(why_fr, why_en, why_ar),
    }


def P(task, starter, solution, hint):
    return {
        "task": T(*task),
        "starter": starter,
        "solution": solution,
        "hint": T(*hint),
    }


def o(fr, en, ar):
    return T(fr, en, ar)


DATA = {}

# ---------------------------------------------------------------------------
# REVISION
# ---------------------------------------------------------------------------
DATA["revision"] = {
    "file": "00-revision.md",
    "title": T("Révision séance précédente", "Previous session review", "مراجعة الحصة السابقة"),
    "theoretical": [
        Q("Où place-t-on le titre de l’onglet ?", "Where do you put the tab title?", "أين نضع عنوان التبويب؟",
          [o("Dans body, avec h1", "In body, with h1", "في body مع h1"),
           o("Dans head, avec title", "In head, with title", "في head مع title"),
           o("Dans un attribut alt", "In an alt attribute", "في سمة alt"),
           o("Dans un commentaire", "In a comment", "في تعليق")],
          1, "title va dans head. h1 est le titre visible dans la page.", "title goes in head. h1 is the visible page heading.", "title في head. h1 عنوان الصفحة الظاهر."),
        Q("Quelle est la forme d’un attribut ?", "What is the shape of an attribute?", "ما شكل السمة؟",
          [o("valeur=nom", "value=name", "value=name"),
           o("nom='valeur' dans la balise ouvrante", "name='value' on the opening tag", "name='value' في الوسم الافتتاحي"),
           o("nom dans la balise fermante", "name on the closing tag", "الاسم في وسم الإغلاق"),
           o("un commentaire", "a comment", "تعليق")],
          1, "Toujours nom=\"valeur\" dans la balise ouvrante.", "Always name=\"value\" on the opening tag.", "دائمًا name=\"value\" في الوسم الافتتاحي."),
        Q("Quel élément crée un lien ?", "Which element creates a link?", "أي عنصر ينشئ رابطًا؟",
          [o("img", "img", "img"), o("a", "a", "a"), o("p", "p", "p"), o("div", "div", "div")],
          1, "a (anchor) + href.", "a (anchor) + href.", "a (مرساة) + href."),
        Q("Quel attribut ouvre le lien dans un nouvel onglet ?", "Which attribute opens the link in a new tab?", "أي سمة تفتح الرابط في تبويب جديد؟",
          [o("src", "src", "src"), o("alt", "alt", "alt"), o("target=\"_blank\"", "target=\"_blank\"", "target=\"_blank\""), o("href", "href", "href")],
          2, "target=\"_blank\".", "target=\"_blank\".", "target=\"_blank\"."),
        Q("img est un élément :", "img is:", "img هو:",
          [o("avec balise fermante obligatoire", "with a required closing tag", "بوسم إغلاق إلزامي"),
           o("vide (pas de </img>)", "empty (no </img>)", "فارغ (بدون </img>)"),
           o("un titre", "a heading", "عنوان"),
           o("un lien", "a link", "رابط")],
          1, "img, br, hr, meta sont vides.", "img, br, hr, meta are empty.", "img و br و hr و meta فارغة."),
        Q("À quoi sert alt sur une image ?", "What is alt for on an image?", "ما فائدة alt على الصورة؟",
          [o("Changer la couleur", "Change the color", "تغيير اللون"),
           o("Texte si l’image ne charge pas + accessibilité", "Text if the image fails + accessibility", "نص إن فشلت الصورة + إتاحة"),
           o("Ouvrir un onglet", "Open a tab", "فتح تبويب"),
           o("Mettre en gras", "Make bold", "تغليظ")],
          1, "alt décrit l’image.", "alt describes the image.", "alt يصف الصورة."),
        Q("Quelle balise fait un saut de ligne ?", "Which tag makes a line break?", "أي وسم يكسر السطر؟",
          [o("hr", "hr", "hr"), o("br", "br", "br"), o("p", "p", "p"), o("span", "span", "span")],
          1, "br = line break. hr = trait horizontal.", "br = line break. hr = horizontal rule.", "br = سطر جديد. hr = خط أفقي."),
        Q("Un commentaire HTML s’écrit :", "An HTML comment is written:", "يُكتب تعليق HTML:",
          [o("// texte", "// text", "// نص"),
           o("<!-- texte -->", "<!-- text -->", "<!-- نص -->"),
           o("# texte", "# text", "# نص"),
           o("/* texte */", "/* text */", "/* نص */")],
          1, "<!-- commentaire -->", "<!-- comment -->", "<!-- تعليق -->"),
        Q("div est :", "div is:", "div هو:",
          [o("en ligne", "inline", "ضمن السطر"), o("un bloc (boîte)", "a block (box)", "كتلة (صندوق)"), o("un lien", "a link", "رابط"), o("vide", "empty", "فارغ")],
          1, "div = conteneur bloc. span = en ligne.", "div = block container. span = inline.", "div = حاوية كتلية. span = ضمن السطر."),
        Q("Combien de h1 recommande-t-on par page ?", "How many h1 per page are recommended?", "كم h1 يُنصح به في الصفحة؟",
          [o("Autant que possible", "As many as possible", "أكبر عدد ممكن"), o("Un en général", "Usually one", "واحد عادة"), o("Zéro", "Zero", "صفر"), o("Exactement 6", "Exactly 6", "ستة تمامًا")],
          1, "Un h1 principal.", "One main h1.", "h1 رئيسي واحد."),
        Q("mark sert à :", "mark is for:", "mark لـ:",
          [o("un lien", "a link", "رابط"), o("surligner", "highlight", "تمييز"), o("une image", "an image", "صورة"), o("un titre", "a heading", "عنوان")],
          1, "mark = surlignage.", "mark = highlight.", "mark = تمييز."),
        Q("sup affiche le texte :", "sup displays text:", "sup يعرض النص:",
          [o("en bas (indice)", "lower (subscript)", "أسفل"), o("en haut (exposant)", "higher (superscript)", "أعلى (أس)"), o("en gras", "bold", "غامق"), o("caché", "hidden", "مخفي")],
          1, "sup = exposant (m²). sub = indice (H2O).", "sup = superscript (m²). sub = subscript (H2O).", "sup = أس. sub = منخفض."),
        Q("href est essentiel pour :", "href is essential for:", "href أساسي لـ:",
          [o("img", "img", "img"), o("a", "a", "a"), o("br", "br", "br"), o("hr", "hr", "hr")],
          1, "Sans href, a ne mène nulle part.", "Without href, a goes nowhere.", "بدون href لا يذهب a لأي مكان."),
        Q("title (attribut) affiche :", "The title attribute shows:", "سمة title تعرض:",
          [o("l’onglet", "the tab", "التبويب"), o("une infobulle au survol", "a hover tooltip", "تلميحًا عند المرور"), o("une vidéo", "a video", "فيديو"), o("un favicon", "a favicon", "أيقونة تبويب")],
          1, "title attribut = tooltip. title élément = onglet.", "title attribute = tooltip. title element = tab.", "سمة title = تلميح. عنصر title = التبويب."),
        Q("Le favicon se met avec :", "The favicon is set with:", "تُضبط أيقونة التبويب بـ:",
          [o("img dans body", "img in body", "img في body"),
           o("link rel=\"shortcut icon\" dans head", "link rel=\"shortcut icon\" in head", "link rel=\"shortcut icon\" في head"),
           o("a href", "a href", "a href"),
           o("p", "p", "p")],
          1, "link dans head, href vers le PNG.", "link in head, href to the PNG.", "link في head و href نحو PNG."),
        Q("span sert surtout à :", "span is mainly used to:", "span يُستخدم أساسًا لـ:",
          [o("créer une page", "create a page", "إنشاء صفحة"),
           o("entourer un mot dans une phrase", "wrap a word inside a sentence", "لف كلمة داخل جملة"),
           o("une liste", "a list", "قائمة"),
           o("une vidéo", "a video", "فيديو")],
          1, "span = en ligne.", "span = inline.", "span = ضمن السطر."),
        Q("hr affiche :", "hr displays:", "hr يعرض:",
          [o("un lien", "a link", "رابط"), o("une ligne horizontale", "a horizontal line", "خطًا أفقيًا"), o("un titre", "a heading", "عنوان"), o("un emoji", "an emoji", "إيموجي")],
          1, "hr = séparateur.", "hr = separator.", "hr = فاصل."),
        Q("UTF-8 se met dans :", "UTF-8 is set in:", "UTF-8 يُضبط في:",
          [o("un p", "a p", "p"), o("meta charset dans head", "meta charset in head", "meta charset في head"), o("footer", "footer", "footer"), o("ul", "ul", "ul")],
          1, "meta charset=\"UTF-8\".", "meta charset=\"UTF-8\".", "meta charset=\"UTF-8\"."),
        Q("Quelle balise met en gras “simple” ?", "Which tag makes simple bold?", "أي وسم يجعل النص غامقًا ببساطة؟",
          [o("b", "b", "b"), o("a", "a", "a"), o("img", "img", "img"), o("hr", "hr", "hr")],
          0, "b (ou strong).", "b (or strong).", "b (أو strong)."),
        Q("Le chemin d’une image locale se met dans :", "A local image path goes in:", "مسار صورة محلية يوضع في:",
          [o("href", "href", "href"), o("src", "src", "src"), o("alt", "alt", "alt"), o("target", "target", "target")],
          1, "src = source du fichier. href = destination d’un lien.", "src = file source. href = link destination.", "src = مصدر الملف. href = وجهة الرابط."),
    ],
    "practical": [],
}

def add_prac(key, items):
    DATA[key]["practical"] = items

add_prac("revision", [
    P(("Écris un h1 « Annonces Alger » et un paragraphe.", "Write an h1 “Annonces Alger” and a paragraph.", "اكتب h1 «إعلانات الجزائر» وفقرة."),
      "<body>\n\n</body>", "<body>\n  <h1>Annonces Alger</h1>\n  <p>Bienvenue sur le site d'annonces.</p>\n</body>",
      ("h1 puis p dans body.", "h1 then p in body.", "h1 ثم p في body.")),
    P(("Mets le mot F3 en gras dans un paragraphe.", "Make the word F3 bold in a paragraph.", "اجعل الكلمة F3 غامقة في فقرة."),
      "<p>Appartement F3 à Hydra.</p>", "<p>Appartement <b>F3</b> à Hydra.</p>",
      ("Entoure F3 avec b.", "Wrap F3 with b.", "لف F3 بـ b.")),
    P(("Ajoute un commentaire HTML au-dessus du h1.", "Add an HTML comment above the h1.", "أضف تعليق HTML فوق h1."),
      "<h1>Contact</h1>", "<!-- Fiche vendeur -->\n<h1>Contact</h1>",
      ("<!-- texte -->", "<!-- text -->", "<!-- نص -->")),
    P(("Sépare deux phrases avec un saut de ligne br.", "Split two sentences with a br line break.", "افصل جملتين بـ br."),
      "<p>Karim Hydra</p>", "<p>Karim<br>Hydra</p>",
      ("br au milieu du p.", "br inside the p.", "br داخل p.")),
    P(("Ajoute un trait hr entre le titre et le texte.", "Add an hr rule between the title and the text.", "أضف hr بين العنوان والنص."),
      "<h1>Annonce</h1>\n<p>Peugeot 208</p>", "<h1>Annonce</h1>\n<hr>\n<p>Peugeot 208</p>",
      ("hr est vide.", "hr is empty.", "hr فارغ.")),
    P(("Crée un lien vers Google.", "Create a link to Google.", "أنشئ رابطًا إلى جوجل."),
      "", "<a href=\"https://www.google.com\">Google</a>",
      ("a + href.", "a + href.", "a + href.")),
    P(("Le lien doit s’ouvrir dans un nouvel onglet.", "The link must open in a new tab.", "يجب أن يُفتح الرابط في تبويب جديد."),
      "<a href=\"https://www.google.com\">Google</a>",
      "<a href=\"https://www.google.com\" target=\"_blank\">Google</a>",
      ("target=\"_blank\"", "target=\"_blank\"", "target=\"_blank\"")),
    P(("Ajoute une image avec alt.", "Add an image with alt.", "أضف صورة مع alt."),
      "", "<img src=\"images/voiture.png\" alt=\"Peugeot 208 à Alger\">",
      ("img src alt, pas de balise fermante.", "img src alt, no closing tag.", "img src alt بدون إغلاق.")),
    P(("Ajoute un attribut title (infobulle) au paragraphe.", "Add a title tooltip attribute on the paragraph.", "أضف سمة title (تلميح) للفقرة."),
      "<p>Karim — Alger</p>", "<p title=\"Fiche du vendeur\">Karim — Alger</p>",
      ("title dans la balise ouvrante.", "title on the opening tag.", "title في الوسم الافتتاحي.")),
    P(("Mets 85 m² avec un exposant.", "Write 85 m² using superscript.", "اكتب 85 م² بأس."),
      "<p>85 m2</p>", "<p>85 m<sup>2</sup></p>",
      ("sup autour de 2.", "sup around 2.", "sup حول 2.")),
    P(("Surligna le mot Alger.", "Highlight the word Alger.", "ميّز كلمة Alger."),
      "<p>Ville : Alger</p>", "<p>Ville : <mark>Alger</mark></p>",
      ("mark", "mark", "mark")),
    P(("Entoure le prix avec span.", "Wrap the price with span.", "لف السعر بـ span."),
      "<p>Prix : 85000 DA</p>", "<p>Prix : <span>85000 DA</span></p>",
      ("span en ligne.", "span is inline.", "span ضمن السطر.")),
    P(("Crée un div qui contient un h2 et un p.", "Create a div that contains an h2 and a p.", "أنشئ div يحتوي h2 و p."),
      "", "<div>\n  <h2>iPhone 13</h2>\n  <p>Alger</p>\n</div>",
      ("div = boîte.", "div = box.", "div = صندوق.")),
    P(("Écris H2O avec un indice.", "Write H2O with subscript.", "اكتب H2O بمنخفض."),
      "<p>H2O</p>", "<p>H<sub>2</sub>O</p>",
      ("sub autour de 2.", "sub around 2.", "sub حول 2.")),
    P(("Mets un titre d’onglet « Mini Ouedkniss ».", "Set the tab title to “Mini Ouedkniss”.", "اجعل عنوان التبويب «Mini Ouedkniss»."),
      "<head>\n</head>", "<head>\n  <title>Mini Ouedkniss</title>\n</head>",
      ("élément title dans head.", "title element in head.", "عنصر title في head.")),
    P(("Ajoute charset UTF-8.", "Add charset UTF-8.", "أضف charset UTF-8."),
      "<head>\n  <title>Test</title>\n</head>",
      "<head>\n  <meta charset=\"UTF-8\">\n  <title>Test</title>\n</head>",
      ("meta charset.", "meta charset.", "meta charset.")),
    P(("Italique sur Bab Ezzouar.", "Italic on Bab Ezzouar.", "مائل على Bab Ezzouar."),
      "<p>Appartement à Bab Ezzouar</p>", "<p>Appartement à <i>Bab Ezzouar</i></p>",
      ("i", "i", "i")),
    P(("Souligne « Visite samedi ».", "Underline “Visite samedi”.", "سطّر «Visite samedi»."),
      "<p>Visite samedi</p>", "<p><u>Visite samedi</u></p>",
      ("u", "u", "u")),
    P(("Image 100x100 avec title.", "100x100 image with title.", "صورة 100×100 مع title."),
      "", "<img src=\"photo.png\" alt=\"Annonce\" title=\"Galaxy A54\" width=\"100\" height=\"100\">",
      ("width height title.", "width height title.", "width height title.")),
    P(("Page mini complète : title, h1, lien nouvel onglet.", "Mini full page: title, h1, new-tab link.", "صفحة مصغّرة: title و h1 ورابط تبويب جديد."),
      "<!DOCTYPE html>\n<html>\n<head></head>\n<body></body>\n</html>",
      "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n  <meta charset=\"UTF-8\">\n  <title>Annonce</title>\n</head>\n<body>\n  <h1>Peugeot 208</h1>\n  <a href=\"https://www.google.com\" target=\"_blank\">Google</a>\n</body>\n</html>",
      ("head + body.", "head + body.", "head + body.")),
])

# Continue in same file - chapters 1-13
# I'll build remaining chapters similarly but keep unique questions.

def make_ch(id_, file_, title, theoretical, practical):
    DATA[id_] = {"file": file_, "title": title, "theoretical": theoretical, "practical": practical}


make_ch("chapitre-1", "chapitre-1.md", T("Chapitre 1 — Éléments de texte", "Chapter 1 — Text elements", "الفصل 1 — عناصر النص"),
[
    Q("Quel élément est le titre le plus important ?", "Which element is the most important heading?", "أي عنصر هو أهم عنوان؟",
      [o("h6", "h6", "h6"), o("h1", "h1", "h1"), o("p", "p", "p"), o("span", "span", "span")], 1, "h1 = titre principal.", "h1 = main heading.", "h1 = العنوان الرئيسي."),
    Q("h6 est :", "h6 is:", "h6 هو:",
      [o("plus grand que h1", "bigger than h1", "أكبر من h1"), o("plus petit que h1", "smaller than h1", "أصغر من h1"), o("un lien", "a link", "رابط"), o("vide", "empty", "فارغ")], 1, "Plus le numéro grandit, plus le titre rétrécit.", "As the number grows, the heading shrinks.", "كلما زاد الرقم صغر العنوان."),
    Q("p signifie :", "p means:", "p تعني:",
      [o("picture", "picture", "صورة"), o("paragraph", "paragraph", "فقرة"), o("page", "page", "صفحة"), o("padding", "padding", "حشوة")], 1, "paragraph.", "paragraph.", "فقرة."),
    Q("div est plutôt :", "div is rather:", "div أقرب إلى:",
      [o("en ligne", "inline", "ضمن السطر"), o("un bloc", "a block", "كتلة"), o("un audio", "audio", "صوت"), o("un commentaire", "a comment", "تعليق")], 1, "div = block container.", "div = block container.", "div = حاوية كتلية."),
    Q("span est plutôt :", "span is rather:", "span أقرب إلى:",
      [o("un bloc pleine largeur", "a full-width block", "كتلة بعرض كامل"), o("en ligne dans le texte", "inline in the text", "ضمن النص"), o("un titre", "a heading", "عنوان"), o("une liste", "a list", "قائمة")], 1, "span reste dans la phrase.", "span stays in the sentence.", "span يبقى في الجملة."),
    Q("Combien de niveaux de titres HTML ?", "How many HTML heading levels?", "كم مستوى عناوين في HTML؟",
      [o("3", "3", "3"), o("4", "4", "4"), o("6", "6", "6"), o("10", "10", "10")], 2, "h1 à h6.", "h1 to h6.", "h1 إلى h6."),
    Q("On met plusieurs phrases longues surtout dans :", "Long sentences go mainly in:", "الجمل الطويلة توضع أساسًا في:",
      [o("h1", "h1", "h1"), o("p", "p", "p"), o("title", "title", "title"), o("br", "br", "br")], 1, "p = paragraphe de texte.", "p = text paragraph.", "p = فقرة نص."),
    Q("Pour grouper image + titre + prix d’une carte on utilise souvent :", "To group image + title + price of a card we often use:", "لتجميع صورة + عنوان + سعر البطاقة نستخدم غالبًا:",
      [o("span", "span", "span"), o("div", "div", "div"), o("br", "br", "br"), o("title", "title", "title")], 1, "div = boîte.", "div = box.", "div = صندوق."),
    Q("Pour colorer seulement le mot « Alger » plus tard en CSS on entoure avec :", "To later style only the word “Alger” in CSS we wrap it with:", "لتنسيق كلمة «Alger» لاحقًا في CSS نلفها بـ:",
      [o("div", "div", "div"), o("span", "span", "span"), o("hr", "hr", "hr"), o("html", "html", "html")], 1, "span pour un bout de texte.", "span for a bit of text.", "span لجزء من النص."),
    Q("Le contenu visible va dans :", "Visible content goes in:", "المحتوى الظاهر يذهب إلى:",
      [o("head", "head", "head"), o("body", "body", "body"), o("DOCTYPE", "DOCTYPE", "DOCTYPE"), o("charset", "charset", "charset")], 1, "body = page visible.", "body = visible page.", "body = الصفحة الظاهرة."),
    Q("h3 est :", "h3 is:", "h3 هو:",
      [o("plus important que h1", "more important than h1", "أهم من h1"), o("un sous-titre plus petit que h2", "a smaller subtitle than h2", "عنوان فرعي أصغر من h2"), o("une image", "an image", "صورة"), o("un lien", "a link", "رابط")], 1, "h1 > h2 > h3 …", "h1 > h2 > h3 …", "h1 > h2 > h3 …"),
    Q("On peut mettre un span :", "You can put a span:", "يمكن وضع span:",
      [o("seulement dans head", "only in head", "في head فقط"), o("dans un p", "inside a p", "داخل p"), o("à la place de html", "instead of html", "بدل html"), o("sans balise ouvrante", "without an opening tag", "بدون وسم افتتاحي")], 1, "span vit dans le texte.", "span lives in the text.", "span يعيش داخل النص."),
    Q("div sans CSS :", "A div without CSS:", "div بدون CSS:",
      [o("est forcément vert", "is necessarily green", "أخضر حتمًا"), o("prend en général toute la largeur (bloc)", "usually takes full width (block)", "يأخذ العرض كاملًا عادة (كتلة)"), o("est invisible", "is invisible", "غير ظاهر"), o("crée un onglet", "creates a tab", "ينشئ تبويبًا")], 1, "Comportement bloc par défaut.", "Default block behaviour.", "سلوك كتلي افتراضي."),
    Q("Le titre de l’onglet n’est PAS :", "The tab title is NOT:", "عنوان التبويب ليس:",
      [o("title", "title", "title"), o("h1", "h1", "h1"), o("dans head", "in head", "في head"), o("un élément HTML", "an HTML element", "عنصر HTML")], 1, "h1 est dans la page, pas dans l’onglet.", "h1 is on the page, not in the tab.", "h1 في الصفحة لا في التبويب."),
    Q("Quel élément n’est PAS un titre ?", "Which is NOT a heading?", "أي عنصر ليس عنوانًا؟",
      [o("h4", "h4", "h4"), o("p", "p", "p"), o("h2", "h2", "h2"), o("h5", "h5", "h5")], 1, "p = paragraphe.", "p = paragraph.", "p = فقرة."),
    Q("On écrit un titre de section “Voitures” plutôt avec :", "A section title “Voitures” is rather:", "عنوان قسم «سيارات» يكون عادة:",
      [o("h1 si la page s’appelle déjà Ouedkniss", "h2 if the page is already titled Ouedkniss", "h2 إذا كانت الصفحة بعنوان Ouedkniss"),
       o("six h1", "six h1", "ستة h1"),
       o("span seulement", "span only", "span فقط"),
       o("hr seulement", "hr only", "hr فقط")], 0, "h1 = site/page, h2 = section.", "h1 = site/page, h2 = section.", "h1 = الموقع/الصفحة، h2 = القسم."),
    Q("HTML sert d’abord à :", "HTML is first used to:", "HTML يُستخدم أولًا لـ:",
      [o("donner un rôle / une structure au contenu", "give content a role / structure", "إعطاء دور/هيكل للمحتوى"),
       o("dessiner des ombres 3D", "draw 3D shadows", "رسم ظلال ثلاثية"),
       o("remplacer JavaScript", "replace JavaScript", "تعويض جافاسكربت"),
       o("héberger des vidéos YouTube uniquement", "only host YouTube videos", "استضافة يوتيوب فقط")], 0, "HTML = structure.", "HTML = structure.", "HTML = هيكل."),
    Q("On ferme un p avec :", "You close a p with:", "يُغلق p بـ:",
      [o("</p>", "</p>", "</p>"), o("<p>", "<p>", "<p>"), o("</br>", "</br>", "</br>"), o("</img>", "</img>", "</img>")], 0, "Balise fermante </p>.", "Closing tag </p>.", "وسم إغلاق </p>."),
    Q("Un div peut contenir :", "A div can contain:", "يمكن لـ div أن يحتوي:",
      [o("seulement du texte brut sans balises", "only raw text with no tags", "نصًا خامًا بلا وسوم"),
       o("plusieurs éléments (h2, p, img…)", "several elements (h2, p, img…)", "عدة عناصر (h2 و p و img…)"),
       o("uniquement un head", "only a head", "head فقط"),
       o("un DOCTYPE", "a DOCTYPE", "DOCTYPE")], 1, "div est un conteneur.", "div is a container.", "div حاوية."),
    Q("span autour d’un prix sert à :", "span around a price is for:", "span حول السعر لـ:",
      [o("créer un fichier MP3", "create an MP3 file", "إنشاء ملف MP3"),
       o("cibler ce mot plus tard (couleur, gras…)", "target that word later (color, bold…)", "استهداف تلك الكلمة لاحقًا"),
       o("ouvrir YouTube", "open YouTube", "فتح يوتيوب"),
       o("remplacer charset", "replace charset", "تعويض charset")], 1, "span = crochet sémantique/visuel dans le texte.", "span = hook in the text.", "span = خطاف داخل النص."),
],
[
    P(("Ajoute un h1 « Ouedkniss ».", "Add an h1 “Ouedkniss”.", "أضف h1 «Ouedkniss»."), "", "<h1>Ouedkniss</h1>", ("Balise h1.", "h1 tag.", "وسم h1.")),
    P(("Ajoute un h2 « Téléphones ».", "Add an h2 “Téléphones”.", "أضف h2 «هواتف»."), "<h1>Ouedkniss</h1>", "<h1>Ouedkniss</h1>\n<h2>Téléphones</h2>", ("h2 sous h1.", "h2 under h1.", "h2 تحت h1.")),
    P(("Écris un paragraphe de description.", "Write a description paragraph.", "اكتب فقرة وصف."), "", "<p>iPhone 13 128 Go, état 9/10, Alger Centre.</p>", ("p", "p", "p")),
    P(("Crée un span autour de « Alger ».", "Wrap “Alger” in a span.", "لف «Alger» بـ span."),
      "<p>Ville : Alger</p>", "<p>Ville : <span>Alger</span></p>", ("span", "span", "span")),
    P(("Regroupe h3 et p dans un div.", "Group h3 and p in a div.", "جمّع h3 و p في div."),
      "<h3>Peugeot 208</h3>\n<p>Hydra</p>", "<div>\n  <h3>Peugeot 208</h3>\n  <p>Hydra</p>\n</div>", ("div enveloppe.", "div wraps.", "div يلف.")),
    P(("Ajoute h4, h5 et h6 pour un contact.", "Add h4, h5 and h6 for a contact.", "أضف h4 و h5 و h6 لاتصال."),
      "", "<h4>Détails</h4>\n<h5>Contact</h5>\n<h6>Annonce n°20481</h6>", ("niveaux 4 à 6.", "levels 4 to 6.", "المستويات 4 إلى 6.")),
    P(("Prix dans un span à l’intérieur du p.", "Price in a span inside the p.", "السعر في span داخل p."),
      "<p>Prix : 85000 DA</p>", "<p>Prix : <span>85000 DA</span></p>", ("span", "span", "span")),
    P(("Deux cartes (deux div) l’une sous l’autre.", "Two cards (two divs) stacked.", "بطاقتان (divان) تحت بعض."),
      "", "<div><h3>iPhone 13</h3></div>\n<div><h3>Galaxy A54</h3></div>", ("deux div.", "two divs.", "divان.")),
    P(("Un h3 « Galaxy A54 » et un p « Oran ».", "An h3 “Galaxy A54” and a p “Oran”.", "h3 «Galaxy A54» و p «وهران»."),
      "", "<h3>Galaxy A54</h3>\n<p>Oran</p>", ("h3 + p.", "h3 + p.", "h3 + p.")),
    P(("span autour de « 9/10 ».", "span around “9/10”.", "span حول «9/10»."),
      "<p>État 9/10</p>", "<p>État <span>9/10</span></p>", ("span", "span", "span")),
    P(("Page avec h1, h2, p.", "Page with h1, h2, p.", "صفحة بـ h1 و h2 و p."),
      "<body></body>", "<body>\n  <h1>Annonces</h1>\n  <h2>Voitures</h2>\n  <p>Peugeot 208 à Alger.</p>\n</body>", ("ordre titres puis texte.", "headings then text.", "العناوين ثم النص.")),
    P(("div + h2 + deux p.", "div + h2 + two p.", "div + h2 + فقرتان."),
      "", "<div>\n  <h2>F3 Hydra</h2>\n  <p>85 m2</p>\n  <p>3e étage</p>\n</div>", ("un seul div parent.", "one parent div.", "div أب واحد.")),
    P(("N’utilise pas h1 deux fois : un h1 et un h2.", "Do not use h1 twice: one h1 and one h2.", "لا تستخدم h1 مرتين: h1 و h2."),
      "<h1>Site</h1>\n<h1>Section</h1>", "<h1>Site</h1>\n<h2>Section</h2>", ("section = h2.", "section = h2.", "القسم = h2.")),
    P(("Texte « Bienvenue » dans un p, pas dans un h1.", "“Bienvenue” in a p, not in an h1.", "«مرحبًا» في p لا في h1."),
      "<h1>Bienvenue sur la fiche.</h1>", "<p>Bienvenue sur la fiche.</p>", ("p pour le texte courant.", "p for running text.", "p للنص العادي.")),
    P(("Entoure seulement le prénom avec span.", "Wrap only the first name with span.", "لف الاسم الأول فقط بـ span."),
      "<p>Karim B. — Alger</p>", "<p><span>Karim</span> B. — Alger</p>", ("span autour de Karim.", "span around Karim.", "span حول Karim.")),
    P(("Ajoute un h2 vide de contenu « À propos ».", "Add an h2 with content “À propos”.", "أضف h2 بمحتوى «حول»."),
      "", "<h2>À propos</h2>", ("h2", "h2", "h2")),
    P(("Trois niveaux : h1 site, h2 catégorie, h3 produit.", "Three levels: h1 site, h2 category, h3 product.", "ثلاثة مستويات: h1 موقع، h2 فئة، h3 منتج."),
      "", "<h1>Ouedkniss</h1>\n<h2>Voitures</h2>\n<h3>Peugeot 208</h3>", ("hiérarchie.", "hierarchy.", "تسلسل.")),
    P(("Un div avec un span de ville.", "A div with a city span.", "div مع span للمدينة."),
      "", "<div>\n  <p>Ville : <span>Oran</span></p>\n</div>", ("div > p > span.", "div > p > span.", "div > p > span.")),
    P(("Paragraphe de 2 phrases sur un téléphone.", "A 2-sentence paragraph about a phone.", "فقرة من جملتين عن هاتف."),
      "", "<p>Samsung Galaxy A54 128 Go. Boîte et facture disponibles à Oran.</p>", ("un seul p.", "one p.", "p واحد.")),
    P(("Carte complète : div, h3, p, span prix.", "Full card: div, h3, p, price span.", "بطاقة كاملة: div و h3 و p و span للسعر."),
      "", "<div>\n  <h3>iPhone 13</h3>\n  <p>Alger</p>\n  <p>Prix : <span>85000 DA</span></p>\n</div>", ("comme une annonce.", "like a listing.", "مثل إعلان.")),
])

print("ch1 ok", len(DATA["chapitre-1"]["theoretical"]), len(DATA["chapitre-1"]["practical"]))

# Write remaining chapters to a second generation by importing more below
# Save partial then continue...

def dump_md(key, info):
    lines = [f"# {info['title']['fr']}", "", f"## Exercices théoriques (20)", ""]
    for i, q in enumerate(info["theoretical"], 1):
        lines.append(f"### {i}.")
        lines.append(q["q"]["fr"])
        letters = "abcd"
        for j, opt in enumerate(q["options"]):
            lines.append(f"- {letters[j]}) {opt['fr']}")
        lines.append(f"**Réponse :** {letters[q['a']]}")
        lines.append(f"**Explication :** {q['why']['fr']}")
        lines.append("")
    lines += ["## Exercices pratiques (20)", ""]
    for i, p in enumerate(info["practical"], 1):
        lines.append(f"### {i}.")
        lines.append(f"**Consigne :** {p['task']['fr']}")
        lines.append("")
        lines.append("**Code de départ :**")
        lines.append("```html")
        lines.append(p["starter"] or "<!-- vide -->")
        lines.append("```")
        lines.append("")
        lines.append("**Correction :**")
        lines.append("```html")
        lines.append(p["solution"])
        lines.append("```")
        lines.append("")
        lines.append(f"**Indice :** {p['hint']['fr']}")
        lines.append("")
    path = os.path.join(EXOS, info["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# We'll extend DATA in gen_exos_rest and merge — keep this file importing rest
if __name__ == "__main__":
    print("base keys", list(DATA.keys()))
