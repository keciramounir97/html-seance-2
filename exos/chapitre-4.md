# Chapitre 4 — Titre et favicon

## Exercices théoriques (20)

### 1.
L’élément title se place dans :
- a) body
- b) head
- c) footer
- d) ul
**Réponse :** b
**Explication :** head = configuration.

### 2.
title affiche le texte :
- a) dans l’onglet
- b) en h1 obligatoire
- c) en bas de page seulement
- d) dans une video
**Réponse :** a
**Explication :** Onglet + Google.

### 3.
Le favicon est :
- a) la petite icône de l’onglet
- b) une balise p
- c) un iframe
- d) un audio
**Réponse :** a
**Explication :** link rel=shortcut icon.

### 4.
L’attribut href du favicon contient :
- a) le chemin du fichier image
- b) un paragraphe
- c) un h1
- d) target blank
**Réponse :** a
**Explication :** Chemin vers PNG/ICO.

### 5.
Flaticon sert ici à :
- a) télécharger une icône
- b) lire une video
- c) créer un ul
- d) remplacer UTF-8
**Réponse :** a
**Explication :** Puis dossier icones/.

### 6.
h1 et title :
- a) sont exactement la même chose
- b) title = onglet, h1 = page
- c) h1 va dans head
- d) title va dans body
**Réponse :** b
**Explication :** Deux endroits différents.

### 7.
rel="shortcut icon" signifie :
- a) que ce link est l’icône du site
- b) un lien Google
- c) une video
- d) une liste
**Réponse :** a
**Explication :** rel décrit le rôle du link.

### 8.
Sans title, l’onglet montre souvent :
- a) Document / nom du fichier
- b) une video autoplay
- c) un ul
- d) un footer sémantique
**Réponse :** a
**Explication :** D’où l’intérêt de title.

### 9.
type="image/png" :
- a) indique le type MIME du fichier icône
- b) crée un paragraphe
- c) est un h6
- d) remplace src d’une video
**Réponse :** a
**Explication :** type du link.

### 10.
On met le favicon :
- a) dans head
- b) après </html>
- c) dans un li seulement
- d) dans audio
**Réponse :** a
**Explication :** Toujours head.

### 11.
VS Code snippet link:favicon donne :
- a) une ligne link rel=shortcut icon
- b) un iframe YouTube
- c) une ol
- d) un mark
**Réponse :** a
**Explication :** Puis on remplit href.

### 12.
Un bon title d’annonce :
- a) Peugeot 208 Alger | Aboni
- b) 
- c) <script>
- d) aaaa
**Réponse :** a
**Explication :** Clair et unique.

### 13.
Le fichier icône se range souvent dans :
- a) icones/
- b) head/body/head
- c) un commentaire
- d) un dl
**Réponse :** a
**Explication :** Dossier d’images.

### 14.
link est un élément :
- a) vide
- b) avec </link> obligatoire
- c) un titre
- d) un span
**Réponse :** a
**Explication :** Void.

### 15.
On peut avoir title ET h1 différents :
- a) Oui
- b) Non, interdit
- c) Seulement en arabe
- d) Seulement sans charset
**Réponse :** a
**Explication :** Souvent le title est plus long (SEO).

### 16.
href vide dans le favicon :
- a) n’affiche pas l’icône
- b) crée une video
- c) est le meilleur cas
- d) remplace UTF-8
**Réponse :** a
**Explication :** Il faut le chemin du fichier.

### 17.
L’icône PNG 32×32 :
- a) convient bien à un favicon simple
- b) doit être une video mp4
- c) va dans ol seulement
- d) casse br
**Réponse :** a
**Explication :** Petit fichier.

### 18.
title trop long :
- a) sera coupé dans l’onglet
- b) crée 10 h1
- c) est obligatoire
- d) remplace nav
**Réponse :** a
**Explication :** Reste concis.

### 19.
On télécharge l’icône PUIS :
- a) on écrit le chemin dans href
- b) on supprime head
- c) on ajoute </img> au link
- d) on met title dans body
**Réponse :** a
**Explication :** Fichier d’abord, chemin ensuite.

### 20.
Le couple visible de l’onglet :
- a) favicon + title
- b) ul + ol
- c) video + audio
- d) iframe + source
**Réponse :** a
**Explication :** Les deux se voient dans l’onglet.

## Exercices pratiques (20)

### 1.
**Consigne :** Ajoute un title « Annonces Alger ».

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
  <title>Annonces Alger</title>
</head>
```

**Indice :** title dans head.

### 2.
**Consigne :** Ajoute un favicon PNG.

**Code de départ :**
```html
<head>
<title>X</title>
</head>
```

**Correction :**
```html
<head>
<title>X</title>
<link rel="shortcut icon" href="icones/html.png" type="image/png">
</head>
```

**Indice :** link

### 3.
**Consigne :** Change le title pour Peugeot 208.

**Code de départ :**
```html
<title>Document</title>
```

**Correction :**
```html
<title>Peugeot 208 | Alger</title>
```

**Indice :** texte entre les balises.

### 4.
**Consigne :** href vers icones/logo.png.

**Code de départ :**
```html
<link rel="shortcut icon" href="" type="image/png">
```

**Correction :**
```html
<link rel="shortcut icon" href="icones/logo.png" type="image/png">
```

**Indice :** remplir href.

### 5.
**Consigne :** title + h1 différents.

**Code de départ :**
```html
<head></head>
<body></body>
```

**Correction :**
```html
<head><title>Ouedkniss Alger</title></head>
<body><h1>Annonces</h1></body>
```

**Indice :** onglet ≠ page.

### 6.
**Consigne :** type image/x-icon.

**Code de départ :**
```html
<link rel="shortcut icon" href="f.ico">
```

**Correction :**
```html
<link rel="shortcut icon" href="f.ico" type="image/x-icon">
```

**Indice :** type

### 7.
**Consigne :** Deux lignes : charset et title.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
<title>Aboni</title>
</head>
```

**Indice :** meta puis title.

### 8.
**Consigne :** Favicon + title mini site.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<title>Mini Ouedkniss</title>
<link rel="shortcut icon" href="icones/html.png">
</head>
```

**Indice :** les deux.

### 9.
**Consigne :** Corrige title mis dans body.

**Code de départ :**
```html
<body><title>X</title><h1>X</h1></body>
```

**Correction :**
```html
<head><title>X</title></head>
<body><h1>X</h1></body>
```

**Indice :** title → head.

### 10.
**Consigne :** Title SEO : produit + ville.

**Code de départ :**
```html
<title>Document</title>
```

**Correction :**
```html
<title>iPhone 13 Alger | Aboni</title>
```

**Indice :** mots clés.

### 11.
**Consigne :** rel shortcut icon manquant.

**Code de départ :**
```html
<link href="i.png">
```

**Correction :**
```html
<link rel="shortcut icon" href="i.png">
```

**Indice :** rel

### 12.
**Consigne :** Chemin relatif icones/html-5.png.

**Code de départ :**
```html
<link rel="shortcut icon" href="html-5.png">
```

**Correction :**
```html
<link rel="shortcut icon" href="icones/html-5.png">
```

**Indice :** dossier icones.

### 13.
**Consigne :** Ajoute lang=fr sur html et un title.

**Code de départ :**
```html
<html>
<head></head>
</html>
```

**Correction :**
```html
<html lang="fr">
<head><title>Cours HTML</title></head>
</html>
```

**Indice :** lang + title.

### 14.
**Consigne :** title avec emoji (UTF-8 déjà là).

**Code de départ :**
```html
<title>Annonces</title>
```

**Correction :**
```html
<title>Annonces 🇩🇿</title>
```

**Indice :** coller l’emoji.

### 15.
**Consigne :** Commentaire puis favicon.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<!-- icone onglet -->
<link rel="shortcut icon" href="icones/html.png">
</head>
```

**Indice :** commentaire.

### 16.
**Consigne :** Remplace Document.

**Code de départ :**
```html
<title>Document</title>
```

**Correction :**
```html
<title>Chapitre 4 | Aboni</title>
```

**Indice :** nouveau texte.

### 17.
**Consigne :** Favicon type png et href.

**Code de départ :**
```html
<link rel="shortcut icon">
```

**Correction :**
```html
<link rel="shortcut icon" href="icones/html.png" type="image/png">
```

**Indice :** href + type.

### 18.
**Consigne :** Head complet chapitre 4.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
<title>Séance HTML</title>
<link rel="shortcut icon" href="icones/html.png" type="image/png">
</head>
```

**Indice :** 3 lignes.

### 19.
**Consigne :** Ne pas mettre le favicon en img dans body : utilise link.

**Code de départ :**
```html
<body><img src="icones/html.png" alt="icon"></body>
```

**Correction :**
```html
<head>
<link rel="shortcut icon" href="icones/html.png">
</head>
<body></body>
```

**Indice :** link head.

### 20.
**Consigne :** Title h1 cohérents mais pas identiques.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<head><title>Ouedkniss — Téléphones Alger</title></head>
<body><h1>Téléphones à Alger</h1></body>
```

**Indice :** complémentaires.
