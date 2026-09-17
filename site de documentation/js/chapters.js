(function () {
  const T = window.T;

  function sec(title, paragraphs, extra) {
    return Object.assign({ title: title, p: paragraphs }, extra || {});
  }

  window.CHAPTERS = [
    {
      id: "revision",
      num: 0,
      titles: T("Révision séance précédente", "Previous session review", "مراجعة الحصة السابقة"),
      lead: T(
        "On reprend le squelette HTML, le texte, la mise en forme, les commentaires, les éléments vides, l’onglet, les attributs, les liens et les images — avant d’attaquer listes, icônes et conteneurs.",
        "We recap the HTML skeleton, text, formatting, comments, empty elements, the tab, attributes, links and images — before lists, icons and containers.",
        "نراجع هيكل HTML والنص والتنسيق والتعليقات والعناصر الفارغة وعلامة التبويب والسمات والروابط والصور — قبل القوائم والأيقونات والحاويات."
      ),
      sections: [
        sec(
          T("Squelette d’une page", "Page skeleton", "هيكل الصفحة"),
          [
            T("head = configuration (invisible sauf l’onglet). body = ce que le visiteur voit.", "head = configuration (invisible except the tab). body = what the visitor sees.", "head = الإعدادات (غير ظاهرة إلا في التبويب). body = ما يراه الزائر.")
          ],
          {
            code: "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n  <meta charset=\"UTF-8\">\n  <title>Fiche Peugeot 208 | Alger</title>\n</head>\n<body>\n  <h1>Peugeot 208</h1>\n  <p>Année <b>2020</b> — Alger.</p>\n</body>\n</html>"
          }
        ),
        sec(
          T("Texte, forme, vides, liens", "Text, style, voids, links", "النص والتنسيق والفارغ والروابط"),
          [
            T("h1–h6 = titres. p = paragraphe. div = boîte bloc. span = bout de texte en ligne.", "h1–h6 = headings. p = paragraph. div = block box. span = inline bit of text.", "h1–h6 = عناوين. p = فقرة. div = صندوق كتلي. span = جزء نص داخل السطر."),
            T("b i u mark sub sup = mise en forme. <!-- commentaire -->. br / hr / img = éléments vides (pas de balise fermante).", "b i u mark sub sup = formatting. <!-- comment -->. br / hr / img = empty elements (no closing tag).", "b i u mark sub sup = تنسيق. <!-- تعليق -->. br / hr / img = عناصر فارغة (بدون وسم إغلاق)."),
            T("Attribut = nom=\"valeur\" dans la balise ouvrante. a + href = lien. target=\"_blank\" = nouvel onglet. img + src + alt = image.", "Attribute = name=\"value\" on the opening tag. a + href = link. target=\"_blank\" = new tab. img + src + alt = image.", "السمة = name=\"value\" داخل الوسم الافتتاحي. a + href = رابط. target=\"_blank\" = تبويب جديد. img + src + alt = صورة.")
          ]
        ),
        {
          title: T("Mini page complète", "Complete mini page", "صفحة مصغّرة كاملة"),
          p: [T("Exemple réel d’annonce, comme à la séance précédente.", "A real listing example, like in the previous session.", "مثال إعلان حقيقي كما في الحصة السابقة.")],
          code: "<h1>Peugeot 208</h1>\n<p>Année <b>2020</b> — <mark>65 000 km</mark> — Alger.</p>\n<p>Prix : 1 850 000 DA — 3<sup>e</sup> main.</p>\n<hr>\n<a href=\"https://www.google.com\" target=\"_blank\">Voir sur Google</a>",
          preview: true
        }
      ],
      remember: [
        T("Un seul h1 par page en général.", "Usually one h1 per page.", "غالبًا h1 واحد في الصفحة."),
        T("title (onglet) ≠ h1 (page).", "title (tab) ≠ h1 (page).", "title (التبويب) ≠ h1 (الصفحة)."),
        T("Les attributs se mettent toujours dans la balise ouvrante.", "Attributes always go on the opening tag.", "السمات دائمًا في الوسم الافتتاحي.")
      ]
    },
    {
      id: "chapitre-1",
      num: 1,
      titles: T("Les éléments de texte", "Text elements", "عناصر النص"),
      lead: T(
        "Afficher des titres, des paragraphes, et distinguer div (bloc) de span (en ligne).",
        "Display headings, paragraphs, and tell div (block) from span (inline).",
        "عرض العناوين والفقرات والتمييز بين div (كتلة) و span (ضمن السطر)."
      ),
      sections: [
        {
          title: T("Titres h1 à h6", "Headings h1 to h6", "العناوين h1 إلى h6"),
          p: [T("Plus le numéro est grand, plus le titre est petit. h1 = titre principal de la page.", "The bigger the number, the smaller the heading. h1 = main page title.", "كلما زاد الرقم صغر العنوان. h1 = العنوان الرئيسي.")],
          code: "<h1>Ouedkniss</h1>\n<h2>Téléphones à Alger</h2>\n<h3>iPhone 13 — 85 000 DA</h3>",
          preview: true
        },
        {
          title: T("p, div, span", "p, div, span", "p و div و span"),
          p: [T("p = paragraphe. div = cadre bloc (une carte). span = cadre dans la phrase (un prix, une ville).", "p = paragraph. div = block box (a card). span = box inside a sentence (a price, a city).", "p = فقرة. div = صندوق كتلي (بطاقة). span = صندوق داخل الجملة (سعر، مدينة).")],
          table: {
            headers: T(["Élément", "Type", "Usage"], ["Element", "Type", "Use"], ["العنصر", "النوع", "الاستخدام"]),
            rows: [
              [T("p", "p", "p"), T("bloc", "block", "كتلة"), T("texte", "text", "نص")],
              [T("div", "div", "div"), T("bloc", "block", "كتلة"), T("regrouper une carte", "group a card", "تجميع بطاقة")],
              [T("span", "span", "span"), T("en ligne", "inline", "ضمن السطر"), T("un mot, un prix", "a word, a price", "كلمة أو سعر")]
            ]
          },
          code: "<div>\n  <h2>Peugeot 208</h2>\n  <p>Ville : <span>Alger</span> — Prix : <span>1 850 000 DA</span></p>\n</div>",
          preview: true
        }
      ],
      remember: [
        T("h1 = titre de page, pas un outil pour “faire gros”.", "h1 = page title, not a way to “make it big”.", "h1 = عنوان الصفحة وليس أداة للتكبير.")
      ]
    },
    {
      id: "chapitre-2",
      num: 2,
      titles: T("Mise en forme du texte", "Text formatting", "تنسيق النص"),
      lead: T("Gras, italique, souligné, surligné, indice et exposant — sans CSS.", "Bold, italic, underline, highlight, subscript and superscript — no CSS.", "غامق ومائل وتسطير وتمييز ومنخفض ومرتفع — بدون CSS."),
      sections: [
        {
          title: T("Les balises de forme", "Formatting tags", "وسوم التنسيق"),
          table: {
            headers: T(["Balise", "Effet"], ["Tag", "Effect"], ["الوسم", "الأثر"]),
            rows: [
              [T("b / strong", "b / strong", "b / strong"), T("gras", "bold", "غامق")],
              [T("i / em", "i / em", "i / em"), T("italique", "italic", "مائل")],
              [T("u", "u", "u"), T("souligné", "underline", "تسطير")],
              [T("mark", "mark", "mark"), T("surligné", "highlight", "تمييز")],
              [T("sub", "sub", "sub"), T("indice (H2O)", "subscript (H2O)", "منخفض (H2O)")],
              [T("sup", "sup", "sup"), T("exposant (m²)", "superscript (m²)", "مرتفع (m²)")]
            ]
          },
          code: "<p>Appartement <b>F3</b> à <i>Bab Ezzouar</i>.</p>\n<p>Prix : <strong>1 850 000 DA</strong> — 85 m<sup>2</sup></p>\n<p>Eau : H<sub>2</sub>O — mot <mark>Alger</mark></p>",
          preview: true
        }
      ],
      remember: [
        T("Ces balises s’utilisent à l’intérieur d’un p, pas à la place.", "These tags go inside a p, they do not replace it.", "هذه الوسوم داخل p وليست بديلًا عنه.")
      ]
    },
    {
      id: "chapitre-3",
      num: 3,
      titles: T("Commentaires et éléments vides", "Comments and empty elements", "التعليقات والعناصر الفارغة"),
      lead: T("Notes invisibles dans le code, et balises sans fermeture (br, hr, img).", "Invisible notes in the code, and tags with no closing pair (br, hr, img).", "ملاحظات غير ظاهرة في الكود ووسوم بلا إغلاق (br و hr و img)."),
      sections: [
        {
          title: T("Commentaire", "Comment", "التعليق"),
          p: [T("Le visiteur ne voit pas le commentaire. Ça sert à expliquer ou désactiver du HTML.", "Visitors do not see comments. Use them to explain or disable HTML.", "الزائر لا يرى التعليق. يُستخدم للشرح أو تعطيل HTML.")],
          code: "<!-- Carte de l'annonce Peugeot 208 -->\n<h2>Peugeot 208</h2>"
        },
        {
          title: T("Éléments vides", "Empty elements", "العناصر الفارغة"),
          p: [T("Pas de contenu, pas de balise fermante : br (saut de ligne), hr (trait), img (image).", "No content, no closing tag: br (line break), hr (rule), img (image).", "بدون محتوى وبدون وسم إغلاق: br (سطر جديد) و hr (خط) و img (صورة).")],
          code: "<p>Karim B.<br>Hydra, Alger<br>0550 12 34 56</p>\n<hr>\n<p>Annonce n°20481</p>",
          preview: true
        }
      ],
      remember: [
        T("On n’écrit pas </br> ni </img>.", "Do not write </br> or </img>.", "لا نكتب </br> ولا </img>.")
      ]
    },
    {
      id: "chapitre-4",
      num: 4,
      titles: T("Titre de l’onglet et favicon", "Tab title and favicon", "عنوان التبويب والأيقونة"),
      lead: T("Ce qui se voit dans l’onglet se configure dans head : title + favicon (Flaticon).", "What you see in the tab is set in head: title + favicon (Flaticon).", "ما يظهر في التبويب يُضبط في head: title + أيقونة (Flaticon)."),
      sections: [
        {
          title: T("title vs h1", "title vs h1", "title مقابل h1"),
          p: [T("title = texte de l’onglet (et de Google). h1 = titre visible dans la page.", "title = tab text (and Google). h1 = visible heading in the page.", "title = نص التبويب (وجوجل). h1 = العنوان الظاهر في الصفحة.")],
          code: "<head>\n  <title>Ouedkniss — Annonces Alger</title>\n  <link rel=\"shortcut icon\" href=\"icones/html.png\" type=\"image/png\">\n</head>"
        },
        {
          title: T("Favicon — étapes Flaticon", "Favicon — Flaticon steps", "أيقونة التبويب — خطوات Flaticon"),
          p: [T("flaticon.com → connexion → recherche → personnaliser → télécharger → dossier icones/ → href dans link.", "flaticon.com → log in → search → customize → download → icones/ folder → href on link.", "flaticon.com → دخول → بحث → تخصيص → تنزيل → مجلد icones/ → href في link.")]
        }
      ],
      remember: [
        T("title et favicon vont dans head, jamais dans body.", "title and favicon go in head, never in body.", "title والأيقونة في head وليس في body.")
      ]
    },
    {
      id: "chapitre-5",
      num: 5,
      titles: T("Attributs, liens et images", "Attributes, links and images", "السمات والروابط والصور"),
      lead: T("Un attribut configure un élément. href pour les liens, src et alt pour les images.", "An attribute configures an element. href for links, src and alt for images.", "السمة تضبط العنصر. href للروابط و src و alt للصور."),
      sections: [
        {
          title: T("Forme d’un attribut", "Attribute shape", "شكل السمة"),
          p: [T("Toujours dans la balise ouvrante : nom=\"valeur\". title = infobulle au survol.", "Always on the opening tag: name=\"value\". title = hover tooltip.", "دائمًا في الوسم الافتتاحي: name=\"value\". title = تلميح عند المرور.")],
          code: "<p title=\"Fiche du vendeur\">Karim — Alger</p>\n<a href=\"https://www.google.com\" target=\"_blank\">Google (nouvel onglet)</a>",
          preview: true
        },
        {
          title: T("Image", "Image", "الصورة"),
          p: [T("img est vide. src = fichier. alt = texte de remplacement + accessibilité.", "img is empty. src = file. alt = fallback text + accessibility.", "img فارغ. src = الملف. alt = نص بديل وإتاحة.")],
          code: "<img src=\"images/voiture.png\" alt=\"Peugeot 208 à Alger\" width=\"400\" height=\"250\">"
        }
      ],
      remember: [
        T("Sans href, le lien ne mène nulle part. Sans alt, l’image est incomplète.", "Without href the link goes nowhere. Without alt the image is incomplete.", "بدون href الرابط لا يذهب لأي مكان. بدون alt الصورة ناقصة.")
      ]
    },
    {
      id: "chapitre-6",
      num: 6,
      titles: T("Les listes", "Lists", "القوائم"),
      lead: T(
        "Les listes HTML ne sont pas une base de données : c’est une présentation visuelle, comme les listes de Word (puces ou numéros).",
        "HTML lists are not a database: they are visual layout, like Word lists (bullets or numbers).",
        "قوائم HTML ليست قاعدة بيانات: إنها عرض بصري مثل قوائم وورد (نقاط أو أرقام)."
      ),
      sections: [
        {
          title: T("ul, ol, li", "ul, ol, li", "ul و ol و li"),
          p: [T("ul = unordered (puces) quand l’ordre n’importe pas. ol = ordered (1. 2. 3.) quand l’ordre compte. li = chaque ligne.", "ul = unordered (bullets) when order does not matter. ol = ordered (1. 2. 3.) when order matters. li = each row.", "ul = غير مرتبة (نقاط) عندما لا يهم الترتيب. ol = مرتبة (1. 2. 3.) عندما يهم الترتيب. li = كل سطر.")],
          code: "<ul>\n  <li>Alger</li>\n  <li>Oran</li>\n  <li>Constantine</li>\n</ul>\n<ol>\n  <li>Contacter le vendeur</li>\n  <li>Voir le téléphone</li>\n  <li>Payer</li>\n</ol>",
          preview: true
        },
        {
          title: T("dl — liste de descriptions", "dl — description list", "dl — قائمة وصف"),
          p: [T("Pas de li. dt = le mot. dd = la définition. Idéal pour un glossaire ou une fiche produit.", "No li. dt = the term. dd = the definition. Ideal for a glossary or a product sheet.", "بدون li. dt = المصطلح. dd = التعريف. مناسب للقاموس أو بطاقة المنتج.")],
          code: "<dl>\n  <dt>HTML</dt>\n  <dd>Langage qui structure une page web.</dd>\n  <dt>État 9/10</dt>\n  <dd>Très bon état, micro-rayures possibles.</dd>\n</dl>",
          preview: true
        }
      ],
      remember: [
        T("ul/ol contiennent des li. dl contient des paires dt + dd.", "ul/ol contain li. dl contains dt + dd pairs.", "ul/ol تحتوي li. dl تحتوي أزواج dt + dd.")
      ]
    },
    {
      id: "chapitre-7",
      num: 7,
      titles: T("Les icônes", "Icons", "الأيقونات"),
      lead: T("Deux familles : image PNG (img) ou police d’icônes (i + bibliothèque Akar).", "Two families: PNG image (img) or icon font (i + Akar library).", "عائلتان: صورة PNG (img) أو خط أيقونات (i + مكتبة Akar)."),
      sections: [
        {
          title: T("Méthode 1 — img + Flaticon", "Method 1 — img + Flaticon", "الطريقة 1 — img + Flaticon"),
          p: [T("Télécharger un PNG, le mettre dans icones/, l’afficher avec img. Taille = width et height.", "Download a PNG, put it in icones/, show it with img. Size = width and height.", "نزّل PNG وضعه في icones/ واعرضه بـ img. الحجم = width و height.")],
          code: "<img src=\"icones/html.png\" alt=\"Logo HTML\" width=\"48\" height=\"48\">\n<a href=\"https://www.w3schools.com\">\n  <img src=\"icones/html.png\" alt=\"W3Schools\" width=\"24\" height=\"24\">\n</a>"
        },
        {
          title: T("Méthode 2 — Akar Icons", "Method 2 — Akar Icons", "الطريقة 2 — Akar Icons"),
          p: [
            T("Copier le <script> dans head. Coller <i class=\"ai-...\"> dans body. C’est du texte : color + font-size (pas width/height).", "Copy the <script> into head. Paste <i class=\"ai-...\"> in body. It is text: color + font-size (not width/height).", "انسخ <script> إلى head. الصق <i class=\"ai-...\"> في body. إنه نص: color + font-size (وليس width/height).")
          ],
          code: "<i class=\"ai-facebook-fill\" style=\"color: blue; font-size: 46px;\"></i>",
          interactive: "icons"
        }
      ],
      remember: [
        T("Image → fichier + width/height. Akar → script + font-size/color.", "Image → file + width/height. Akar → script + font-size/color.", "الصورة → ملف + width/height. Akar → سكربت + font-size/color.")
      ]
    },
    {
      id: "chapitre-8",
      num: 8,
      titles: T("Conteneurs sémantiques et non sémantiques", "Semantic and non-semantic containers", "الحاويات الدلالية وغير الدلالية"),
      lead: T(
        "Un conteneur regroupe plusieurs éléments dans un même cadre — comme la carte d’une annonce Ouedkniss (image, titre, icônes, prix).",
        "A container groups several elements in one frame — like an Ouedkniss listing card (image, title, icons, price).",
        "الحاوية تجمع عدة عناصر في إطار واحد — مثل بطاقة إعلان (صورة، عنوان، أيقونات، سعر)."
      ),
      sections: [
        {
          title: T("Non sémantique : div et span", "Non-semantic: div and span", "غير دلالي: div و span"),
          p: [T("Aucun métier dans le nom. div = boîte bloc. span = boîte en ligne. Un div peut visuellement remplacer header ou footer, mais Google ne comprend pas le rôle.", "No job in the name. div = block box. span = inline box. A div can visually replace header or footer, but Google does not understand the role.", "لا مهنة في الاسم. div = صندوق كتلي. span = صندوق سطري. يمكن لـ div أن يعوّض header أو footer بصريًا لكن جوجل لا يفهم الدور.")],
          code: "<div>\n  <img src=\"voiture.jpg\" alt=\"Peugeot 208\">\n  <h2>Peugeot 208</h2>\n  <p>Prix : <span>1 850 000 DA</span></p>\n</div>"
        },
        {
          title: T("Sémantique HTML5", "HTML5 semantics", "دلالات HTML5"),
          p: [T("Le nom dit le métier. On mélange sémantique (quand on peut nommer la zone) et div (pour le CSS).", "The name states the job. Mix semantics (when you can name the area) and div (for CSS).", "الاسم يوضح المهمة. نمزج الدلالة (عندما نستطيع تسمية المنطقة) و div (من أجل CSS).")],
          table: {
            headers: T(["Élément", "Métier"], ["Element", "Job"], ["العنصر", "المهمة"]),
            rows: [
              [T("header", "header", "header"), T("en-tête", "header bar", "ترويسة")],
              [T("nav", "nav", "nav"), T("menu", "menu", "قائمة")],
              [T("main", "main", "main"), T("contenu principal (1 par page)", "main content (1 per page)", "المحتوى الرئيسي (واحد في الصفحة)")],
              [T("section", "section", "section"), T("partie thématique", "thematic part", "جزء موضوعي")],
              [T("article", "article", "article"), T("annonce / article indépendant", "independent listing / post", "إعلان / مقال مستقل")],
              [T("aside", "aside", "aside"), T("pub, à côté", "ad, aside", "إعلان جانبي")],
              [T("footer", "footer", "footer"), T("pied de page", "page footer", "تذييل")]
            ]
          },
          code: "<header><h1>Ouedkniss</h1><nav><a href=\"#\">Annonces</a></nav></header>\n<main>\n  <section>\n    <article>\n      <h2>iPhone 13</h2>\n      <p>Alger — 85 000 DA</p>\n    </article>\n  </section>\n  <aside>Publicité</aside>\n</main>\n<footer>© 2026</footer>",
          preview: true,
          interactive: "semantic"
        }
      ],
      remember: [
        T("Sémantique = le nom donne le job. Non sémantique = générique (div).", "Semantic = the name gives the job. Non-semantic = generic (div).", "دلالي = الاسم يعطي المهمة. غير دلالي = عام (div)."),
        T("Pourquoi pas que des div ? Le moteur de recherche aime la diversité et le sens.", "Why not only divs? Search engines like diversity and meaning.", "لماذا لا نستخدم div فقط؟ محرك البحث يحب التنوع والمعنى.")
      ]
    },
    {
      id: "chapitre-9",
      num: 9,
      titles: T("Vidéo", "Video", "الفيديو"),
      lead: T("Intégrer un fichier vidéo avec video + controls, ou plusieurs formats avec source.", "Embed a video file with video + controls, or several formats with source.", "دمج ملف فيديو بـ video + controls أو عدة صيغ بـ source."),
      sections: [
        {
          title: T("Un fichier", "One file", "ملف واحد"),
          p: [T("Sans controls, pas de boutons play/pause. width et height règlent la taille.", "Without controls there are no play/pause buttons. width and height set the size.", "بدون controls لا توجد أزرار تشغيل. width و height تضبطان الحجم.")],
          code: "<video src=\"videos/video.mp4\" controls width=\"500\" height=\"280\"></video>"
        },
        {
          title: T("Plusieurs formats", "Several formats", "عدة صيغ"),
          p: [T("Le navigateur prend le premier format qu’il sait lire, puis saute aux suivants. MP4 est le plus sûr. YouTube = iframe, pas video.", "The browser takes the first format it can play, then skips the rest. MP4 is safest. YouTube = iframe, not video.", "المتصفح يأخذ أول صيغة يعرف تشغيلها ثم ينتقل للتالية. MP4 الأكثر أمانًا. يوتيوب = iframe وليس video.")],
          code: "<video controls width=\"500\">\n  <source src=\"videos/video.mp4\" type=\"video/mp4\">\n  <source src=\"videos/video.webm\" type=\"video/webm\">\n  <source src=\"videos/video.ogg\" type=\"video/ogg\">\n  Navigateur non supporté.\n</video>"
        }
      ],
      remember: [
        T("controls est presque toujours obligatoire.", "controls is almost always required.", "controls شبه إلزامي دائمًا.")
      ]
    },
    {
      id: "chapitre-10",
      num: 10,
      titles: T("Audio", "Audio", "الصوت"),
      lead: T("Même logique que la vidéo, sans image : audio + controls, et source pour plusieurs formats.", "Same logic as video, without a picture: audio + controls, and source for several formats.", "نفس منطق الفيديو بلا صورة: audio + controls و source لعدة صيغ."),
      sections: [
        {
          title: T("Un fichier MP3", "One MP3 file", "ملف MP3 واحد"),
          p: [T("width/height ne s’appliquent pas vraiment à audio. Toujours controls pour que l’utilisateur lance le son.", "width/height do not really apply to audio. Always use controls so the user can start the sound.", "width/height لا تنطبق فعليًا على audio. استخدم controls دائمًا ليبدأ المستخدم الصوت.")],
          code: "<audio src=\"audio/audio.mp3\" controls></audio>"
        },
        {
          title: T("Plusieurs formats", "Several formats", "عدة صيغ"),
          p: [T("mp3 → audio/mpeg. ogg → audio/ogg. wav → audio/wav. Si un format n’est pas supporté, le navigateur saute vers l’autre.", "mp3 → audio/mpeg. ogg → audio/ogg. wav → audio/wav. If a format is unsupported, the browser jumps to the next.", "mp3 → audio/mpeg. ogg → audio/ogg. wav → audio/wav. إذا لم تُدعم صيغة ينتقل المتصفح للأخرى.")],
          code: "<audio controls>\n  <source src=\"audio/audio.mp3\" type=\"audio/mpeg\">\n  <source src=\"audio/audio.ogg\" type=\"audio/ogg\">\n  <source src=\"audio/audio.wav\" type=\"audio/wav\">\n</audio>"
        }
      ],
      remember: [
        T("video = image + son. audio = son seulement. Les deux utilisent source.", "video = picture + sound. audio = sound only. Both use source.", "video = صورة + صوت. audio = صوت فقط. كلاهما يستخدم source.")
      ]
    },
    {
      id: "chapitre-11",
      num: 11,
      titles: T("Iframe", "Iframe", "Iframe"),
      lead: T("Un cadre qui charge une autre page ou une vidéo YouTube, sans quitter ton site.", "A frame that loads another page or a YouTube video, without leaving your site.", "إطار يحمّل صفحة أخرى أو فيديو يوتيوب دون مغادرة موقعك."),
      sections: [
        {
          title: T("Fichier local", "Local file", "ملف محلي"),
          p: [T("src = chemin du fichier HTML à afficher dans le cadre.", "src = path of the HTML file to show inside the frame.", "src = مسار ملف HTML المعروض داخل الإطار.")],
          code: "<iframe src=\"../chapitre-10/index.html\" width=\"500\" height=\"280\" title=\"Audio chapitre 10\"></iframe>"
        },
        {
          title: T("YouTube", "YouTube", "يوتيوب"),
          p: [T("YouTube donne un iframe (Partager → Intégrer). L’URL est /embed/ID, pas watch?v=. Ce n’est pas l’élément video.", "YouTube gives an iframe (Share → Embed). The URL is /embed/ID, not watch?v=. This is not the video element.", "يوتيوب يعطي iframe (مشاركة → تضمين). الرابط /embed/ID وليس watch?v=. هذا ليس عنصر video.")],
          code: "<iframe width=\"560\" height=\"315\"\n  src=\"https://www.youtube.com/embed/U2-JPqrALsA\"\n  title=\"YouTube\"\n  allowfullscreen></iframe>"
        }
      ],
      remember: [
        T("video = ton fichier mp4. iframe = YouTube ou une autre page.", "video = your mp4 file. iframe = YouTube or another page.", "video = ملف mp4 الخاص بك. iframe = يوتيوب أو صفحة أخرى.")
      ]
    },
    {
      id: "chapitre-12",
      num: 12,
      titles: T("HTML Head", "HTML Head", "HTML Head"),
      lead: T("head = configuration : charset, viewport, title, favicon, CSS, JS, librairies d’icônes.", "head = configuration: charset, viewport, title, favicon, CSS, JS, icon libraries.", "head = الإعدادات: charset و viewport و title والأيقونة و CSS و JS ومكتبات الأيقونات."),
      sections: [
        {
          title: T("charset et viewport", "charset and viewport", "charset و viewport"),
          p: [
            T("charset UTF-8 = accents, €, emojis. Sans ça, é et 😀 cassent.", "charset UTF-8 = accents, €, emojis. Without it, é and 😀 break.", "charset UTF-8 = الحركات و € والإيموجي. بدونه ينكسر é و 😀."),
            T("viewport = le téléphone prend sa vraie largeur (pas une mini page PC).", "viewport = the phone uses its real width (not a tiny desktop page).", "viewport = الهاتف يستخدم عرضه الحقيقي (وليس صفحة حاسوب مصغّرة).")
          ],
          code: "<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>Annonces Alger | Aboni</title>\n  <link rel=\"shortcut icon\" href=\"icones/html.png\" type=\"image/png\">\n  <link rel=\"stylesheet\" href=\"style.css\">\n  <script src=\"https://unpkg.com/akar-icons-fonts\"></script>\n</head>"
        }
      ],
      remember: [
        T("Visible dans la page → body. Onglet / config → head.", "Visible on the page → body. Tab / config → head.", "الظاهر في الصفحة → body. التبويب / الإعداد → head.")
      ]
    },
    {
      id: "chapitre-13",
      num: 13,
      titles: T("Symboles HTML et emojis", "HTML symbols and emojis", "رموز HTML والإيموجي"),
      lead: T("UTF-8 pour coller les emojis. Entities (&copy; &lt; &nbsp;) pour les caractères réservés et les symboles.", "UTF-8 to paste emojis. Entities (&copy; &lt; &nbsp;) for reserved characters and symbols.", "UTF-8 للصق الإيموجي. الكيانات (&copy; &lt; &nbsp;) للمحارف المحجوزة والرموز."),
      sections: [
        {
          title: T("Emojis", "Emojis", "الإيموجي"),
          p: [T("Coller direct : 😀 ❤️ 🇩🇿. Ou code : &#128512; = 😀. Il faut meta charset UTF-8.", "Paste directly: 😀 ❤️ 🇩🇿. Or code: &#128512; = 😀. You need meta charset UTF-8.", "الصق مباشرة: 😀 ❤️ 🇩🇿. أو الرمز: &#128512; = 😀. تحتاج meta charset UTF-8.")],
          code: "<p>bonjour 😀 ❤️ 🇩🇿</p>\n<p>&#128512;</p>",
          preview: true
        },
        {
          title: T("Entities réservées", "Reserved entities", "الكيانات المحجوزة"),
          p: [T("< > & \" ' cassent le HTML si on les tape tels quels. On écrit &lt; &gt; &amp; &quot; &apos;. &nbsp; = espace forcé.", "< > & \" ' break HTML if typed raw. Write &lt; &gt; &amp; &quot; &apos;. &nbsp; = forced space.", "< > & \" ' تكسر HTML إذا كُتبت كما هي. نكتب &lt; &gt; &amp; &quot; &apos;. &nbsp; = مسافة إجبارية.")],
          code: "<p>L’élément p s’écrit &lt;p&gt;&lt;/p&gt;</p>\n<p>&copy; 2026 Aboni — 2500 &euro;</p>",
          preview: true,
          interactive: "entities"
        }
      ],
      remember: [
        T("Nom (&copy;) plus lisible. Numéro (&#169;) marche toujours.", "Name (&copy;) is easier to read. Number (&#169;) always works.", "الاسم (&copy;) أوضح. الرقم (&#169;) يعمل دائمًا.")
      ]
    }
  ];
})();
