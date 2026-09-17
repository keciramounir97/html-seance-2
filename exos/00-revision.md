# Révision séance précédente

## Exercices théoriques (20)

### 1.
Où place-t-on le titre de l’onglet ?
- a) Dans body, avec h1
- b) Dans head, avec title
- c) Dans un attribut alt
- d) Dans un commentaire
**Réponse :** b
**Explication :** title va dans head. h1 est le titre visible dans la page.

### 2.
Quelle est la forme d’un attribut ?
- a) valeur=nom
- b) nom='valeur' dans la balise ouvrante
- c) nom dans la balise fermante
- d) un commentaire
**Réponse :** b
**Explication :** Toujours nom="valeur" dans la balise ouvrante.

### 3.
Quel élément crée un lien ?
- a) img
- b) a
- c) p
- d) div
**Réponse :** b
**Explication :** a (anchor) + href.

### 4.
Quel attribut ouvre le lien dans un nouvel onglet ?
- a) src
- b) alt
- c) target="_blank"
- d) href
**Réponse :** c
**Explication :** target="_blank".

### 5.
img est un élément :
- a) avec balise fermante obligatoire
- b) vide (pas de </img>)
- c) un titre
- d) un lien
**Réponse :** b
**Explication :** img, br, hr, meta sont vides.

### 6.
À quoi sert alt sur une image ?
- a) Changer la couleur
- b) Texte si l’image ne charge pas + accessibilité
- c) Ouvrir un onglet
- d) Mettre en gras
**Réponse :** b
**Explication :** alt décrit l’image.

### 7.
Quelle balise fait un saut de ligne ?
- a) hr
- b) br
- c) p
- d) span
**Réponse :** b
**Explication :** br = line break. hr = trait horizontal.

### 8.
Un commentaire HTML s’écrit :
- a) // texte
- b) <!-- texte -->
- c) # texte
- d) /* texte */
**Réponse :** b
**Explication :** <!-- commentaire -->

### 9.
div est :
- a) en ligne
- b) un bloc (boîte)
- c) un lien
- d) vide
**Réponse :** b
**Explication :** div = conteneur bloc. span = en ligne.

### 10.
Combien de h1 recommande-t-on par page ?
- a) Autant que possible
- b) Un en général
- c) Zéro
- d) Exactement 6
**Réponse :** b
**Explication :** Un h1 principal.

### 11.
mark sert à :
- a) un lien
- b) surligner
- c) une image
- d) un titre
**Réponse :** b
**Explication :** mark = surlignage.

### 12.
sup affiche le texte :
- a) en bas (indice)
- b) en haut (exposant)
- c) en gras
- d) caché
**Réponse :** b
**Explication :** sup = exposant (m²). sub = indice (H2O).

### 13.
href est essentiel pour :
- a) img
- b) a
- c) br
- d) hr
**Réponse :** b
**Explication :** Sans href, a ne mène nulle part.

### 14.
title (attribut) affiche :
- a) l’onglet
- b) une infobulle au survol
- c) une vidéo
- d) un favicon
**Réponse :** b
**Explication :** title attribut = tooltip. title élément = onglet.

### 15.
Le favicon se met avec :
- a) img dans body
- b) link rel="shortcut icon" dans head
- c) a href
- d) p
**Réponse :** b
**Explication :** link dans head, href vers le PNG.

### 16.
span sert surtout à :
- a) créer une page
- b) entourer un mot dans une phrase
- c) une liste
- d) une vidéo
**Réponse :** b
**Explication :** span = en ligne.

### 17.
hr affiche :
- a) un lien
- b) une ligne horizontale
- c) un titre
- d) un emoji
**Réponse :** b
**Explication :** hr = séparateur.

### 18.
UTF-8 se met dans :
- a) un p
- b) meta charset dans head
- c) footer
- d) ul
**Réponse :** b
**Explication :** meta charset="UTF-8".

### 19.
Quelle balise met en gras “simple” ?
- a) b
- b) a
- c) img
- d) hr
**Réponse :** a
**Explication :** b (ou strong).

### 20.
Le chemin d’une image locale se met dans :
- a) href
- b) src
- c) alt
- d) target
**Réponse :** b
**Explication :** src = source du fichier. href = destination d’un lien.

## Exercices pratiques (20)

### 1.
**Consigne :** Écris un h1 « Annonces Alger » et un paragraphe.

**Code de départ :**
```html
<body>

</body>
```

**Correction :**
```html
<body>
  <h1>Annonces Alger</h1>
  <p>Bienvenue sur le site d'annonces.</p>
</body>
```

**Indice :** h1 puis p dans body.

### 2.
**Consigne :** Mets le mot F3 en gras dans un paragraphe.

**Code de départ :**
```html
<p>Appartement F3 à Hydra.</p>
```

**Correction :**
```html
<p>Appartement <b>F3</b> à Hydra.</p>
```

**Indice :** Entoure F3 avec b.

### 3.
**Consigne :** Ajoute un commentaire HTML au-dessus du h1.

**Code de départ :**
```html
<h1>Contact</h1>
```

**Correction :**
```html
<!-- Fiche vendeur -->
<h1>Contact</h1>
```

**Indice :** <!-- texte -->

### 4.
**Consigne :** Sépare deux phrases avec un saut de ligne br.

**Code de départ :**
```html
<p>Karim Hydra</p>
```

**Correction :**
```html
<p>Karim<br>Hydra</p>
```

**Indice :** br au milieu du p.

### 5.
**Consigne :** Ajoute un trait hr entre le titre et le texte.

**Code de départ :**
```html
<h1>Annonce</h1>
<p>Peugeot 208</p>
```

**Correction :**
```html
<h1>Annonce</h1>
<hr>
<p>Peugeot 208</p>
```

**Indice :** hr est vide.

### 6.
**Consigne :** Crée un lien vers Google.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<a href="https://www.google.com">Google</a>
```

**Indice :** a + href.

### 7.
**Consigne :** Le lien doit s’ouvrir dans un nouvel onglet.

**Code de départ :**
```html
<a href="https://www.google.com">Google</a>
```

**Correction :**
```html
<a href="https://www.google.com" target="_blank">Google</a>
```

**Indice :** target="_blank"

### 8.
**Consigne :** Ajoute une image avec alt.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<img src="images/voiture.png" alt="Peugeot 208 à Alger">
```

**Indice :** img src alt, pas de balise fermante.

### 9.
**Consigne :** Ajoute un attribut title (infobulle) au paragraphe.

**Code de départ :**
```html
<p>Karim — Alger</p>
```

**Correction :**
```html
<p title="Fiche du vendeur">Karim — Alger</p>
```

**Indice :** title dans la balise ouvrante.

### 10.
**Consigne :** Mets 85 m² avec un exposant.

**Code de départ :**
```html
<p>85 m2</p>
```

**Correction :**
```html
<p>85 m<sup>2</sup></p>
```

**Indice :** sup autour de 2.

### 11.
**Consigne :** Surligna le mot Alger.

**Code de départ :**
```html
<p>Ville : Alger</p>
```

**Correction :**
```html
<p>Ville : <mark>Alger</mark></p>
```

**Indice :** mark

### 12.
**Consigne :** Entoure le prix avec span.

**Code de départ :**
```html
<p>Prix : 85000 DA</p>
```

**Correction :**
```html
<p>Prix : <span>85000 DA</span></p>
```

**Indice :** span en ligne.

### 13.
**Consigne :** Crée un div qui contient un h2 et un p.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<div>
  <h2>iPhone 13</h2>
  <p>Alger</p>
</div>
```

**Indice :** div = boîte.

### 14.
**Consigne :** Écris H2O avec un indice.

**Code de départ :**
```html
<p>H2O</p>
```

**Correction :**
```html
<p>H<sub>2</sub>O</p>
```

**Indice :** sub autour de 2.

### 15.
**Consigne :** Mets un titre d’onglet « Mini Ouedkniss ».

**Code de départ :**
```html
<head>
</head>
```

**Correction :**
```html
<head>
  <title>Mini Ouedkniss</title>
</head>
```

**Indice :** élément title dans head.

### 16.
**Consigne :** Ajoute charset UTF-8.

**Code de départ :**
```html
<head>
  <title>Test</title>
</head>
```

**Correction :**
```html
<head>
  <meta charset="UTF-8">
  <title>Test</title>
</head>
```

**Indice :** meta charset.

### 17.
**Consigne :** Italique sur Bab Ezzouar.

**Code de départ :**
```html
<p>Appartement à Bab Ezzouar</p>
```

**Correction :**
```html
<p>Appartement à <i>Bab Ezzouar</i></p>
```

**Indice :** i

### 18.
**Consigne :** Souligne « Visite samedi ».

**Code de départ :**
```html
<p>Visite samedi</p>
```

**Correction :**
```html
<p><u>Visite samedi</u></p>
```

**Indice :** u

### 19.
**Consigne :** Image 100x100 avec title.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<img src="photo.png" alt="Annonce" title="Galaxy A54" width="100" height="100">
```

**Indice :** width height title.

### 20.
**Consigne :** Page mini complète : title, h1, lien nouvel onglet.

**Code de départ :**
```html
<!DOCTYPE html>
<html>
<head></head>
<body></body>
</html>
```

**Correction :**
```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Annonce</title>
</head>
<body>
  <h1>Peugeot 208</h1>
  <a href="https://www.google.com" target="_blank">Google</a>
</body>
</html>
```

**Indice :** head + body.
