# Chapitre 12 — HTML Head

## Exercices théoriques (20)

### 1.
head contient :
- a) la configuration (peu visible)
- b) tout le texte h1 de la page seulement
- c) uniquement des li
- d) uniquement des video
**Réponse :** a
**Explication :** body = visible.

### 2.
charset UTF-8 :
- a) accents, €, emojis
- b) une liste ol
- c) un iframe
- d) un footer
**Réponse :** a
**Explication :** Première meta souvent.

### 3.
viewport :
- a) largeur écran (téléphone vs PC)
- b) un type mp3
- c) un dt
- d) un mark
**Réponse :** a
**Explication :** width=device-width.

### 4.
Sans viewport le téléphone :
- a) affiche souvent une mini page PC
- b) lit un mp4 tout seul
- c) crée un ul
- d) ajoute un favicon
**Réponse :** a
**Explication :** Zoom pénible.

### 5.
title va dans :
- a) head
- b) body seulement
- c) footer
- d) source
**Réponse :** a
**Explication :** Onglet.

### 6.
favicon :
- a) link dans head
- b) ol dans body
- c) audio
- d) iframe YT
**Réponse :** a
**Explication :** Chapitre 4 + 12.

### 7.
CSS externe :
- a) link rel="stylesheet" href="style.css"
- b) img src style.css
- c) audio src style.css
- d) ul href style.css
**Réponse :** a
**Explication :** Dans head souvent.

### 8.
JS librairie icônes :
- a) script src dans head (Akar)
- b) un dt
- c) un hr
- d) un sub
**Réponse :** a
**Explication :** Chapitre 7.

### 9.
meta description :
- a) texte pour Google sous le titre
- b) un h1 visible grand
- c) un ol
- d) un source mp4
**Réponse :** a
**Explication :** SEO.

### 10.
style interne :
- a) <style> dans head
- b) <ul> dans charset
- c) <br> CSS
- d) <video> CSS
**Réponse :** a
**Explication :** CSS dans la page.

### 11.
JS peut aussi aller :
- a) avant </body> (souvent mieux)
- b) dans alt d’img seulement
- c) dans un li obligatoire
- d) dans DOCTYPE
**Réponse :** a
**Explication :** Vitesse.

### 12.
lang="fr" se met sur :
- a) html
- b) source
- c) hr
- d) br
**Réponse :** a
**Explication :** Langue du document.

### 13.
meta author :
- a) nom de l’auteur
- b) un iframe
- c) un ol
- d) un emoji obligatoire
**Réponse :** a
**Explication :** Optionnel.

### 14.
Sans UTF-8 :
- a) é et 😀 peuvent casser
- b) ol disparaît
- c) video devient audio
- d) nav devient footer
**Réponse :** a
**Explication :** Chapitre 13 aussi.

### 15.
viewport initial-scale=1.0 :
- a) pas de zoom bizarre au départ
- b) crée 1.0 listes
- c) est un mp3
- d) est un article
**Réponse :** a
**Explication :** Échelle 1.

### 16.
On voit le title :
- a) dans l’onglet, pas comme h1
- b) en grand dans body automatiquement
- c) dans un ul
- d) dans audio
**Réponse :** a
**Explication :** Rappel ch.4.

### 17.
link est vide :
- a) oui (favicon, CSS)
- b) non, </link> obligatoire
- c) c’est un p
- d) c’est un h2
**Réponse :** a
**Explication :** Void.

### 18.
meta est vide :
- a) oui
- b) non
- c) c’est un iframe
- d) c’est un dl
**Réponse :** a
**Explication :** Pas de </meta>.

### 19.
Ordre conseillé :
- a) charset, viewport, title, favicon, css, scripts
- b) body puis head
- c) footer puis doctype
- d) ul puis html
**Réponse :** a
**Explication :** Lisibilité.

### 20.
head n’affiche pas :
- a) le h1, les p, les images du site (ça c’est body)
- b) jamais le title d’onglet
- c) jamais le favicon
- d) la config
**Réponse :** a
**Explication :** Visible vs config.

## Exercices pratiques (20)

### 1.
**Consigne :** meta charset.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
</head>
```

**Indice :** UTF-8

### 2.
**Consigne :** viewport.

**Code de départ :**
```html
<head>
<meta charset="UTF-8">
</head>
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

**Indice :** viewport

### 3.
**Consigne :** title.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<title>Annonces Alger | Aboni</title>
</head>
```

**Indice :** title

### 4.
**Consigne :** favicon.

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

### 5.
**Consigne :** CSS externe.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<link rel="stylesheet" href="style.css">
</head>
```

**Indice :** stylesheet

### 6.
**Consigne :** script Akar.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<script src="https://unpkg.com/akar-icons-fonts"></script>
</head>
```

**Indice :** script

### 7.
**Consigne :** meta description.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<meta name="description" content="Mini site d'annonces à Alger.">
</head>
```

**Indice :** description

### 8.
**Consigne :** style interne body font.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<style>body { font-family: sans-serif; }</style>
</head>
```

**Indice :** style

### 9.
**Consigne :** lang fr sur html.

**Code de départ :**
```html
<html>
<head></head>
</html>
```

**Correction :**
```html
<html lang="fr">
<head></head>
</html>
```

**Indice :** lang

### 10.
**Consigne :** author Aboni.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<meta name="author" content="Aboni">
</head>
```

**Indice :** author

### 11.
**Consigne :** Head complet du cours.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Cours HTML">
<title>Chapitre 12 | Aboni</title>
<link rel="shortcut icon" href="icones/html.png" type="image/png">
</head>
```

**Indice :** toutes les lignes.

### 12.
**Consigne :** Corrige title dans body.

**Code de départ :**
```html
<body><title>X</title><h1>X</h1></body>
```

**Correction :**
```html
<head><title>X</title></head>
<body><h1>X</h1></body>
```

**Indice :** head

### 13.
**Consigne :** Test UTF-8 dans body.

**Code de départ :**
```html
<head><meta charset="UTF-8"></head>
<body></body>
```

**Correction :**
```html
<head><meta charset="UTF-8"></head>
<body><p>café 85 € 😀 🇩🇿</p></body>
```

**Indice :** accents emoji

### 14.
**Consigne :** CSS + title.

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<title>Site</title>
<link rel="stylesheet" href="style.css">
</head>
```

**Indice :** 2 liens config.

### 15.
**Consigne :** script avant fin body.

**Code de départ :**
```html
<body>
<h1>Hi</h1>
</body>
```

**Correction :**
```html
<body>
<h1>Hi</h1>
<script src="app.js"></script>
</body>
```

**Indice :** fin body

### 16.
**Consigne :** viewport content exact.

**Code de départ :**
```html
<meta name="viewport">
```

**Correction :**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Indice :** content

### 17.
**Consigne :** Deux meta + title.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aboni</title>
</head>
```

**Indice :** base

### 18.
**Consigne :** Commentaires dans head.

**Code de départ :**
```html
<head>
<title>X</title>
</head>
```

**Correction :**
```html
<head>
<!-- configuration -->
<title>X</title>
</head>
```

**Indice :** <!-- -->

### 19.
**Consigne :** Ne pas mettre h1 dans head.

**Code de départ :**
```html
<head><h1>Annonces</h1></head>
```

**Correction :**
```html
<head><title>Annonces</title></head>
<body><h1>Annonces</h1></body>
```

**Indice :** h1 → body

### 20.
**Consigne :** Page minimale valide cours.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aboni</title>
</head>
<body>
<h1>Hello</h1>
</body>
</html>
```

**Indice :** squelette
