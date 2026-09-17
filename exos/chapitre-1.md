# Chapitre 1 — Éléments de texte

## Exercices théoriques (20)

### 1.
Quel élément est le titre le plus important ?
- a) h6
- b) h1
- c) p
- d) span
**Réponse :** b
**Explication :** h1 = titre principal.

### 2.
h6 est :
- a) plus grand que h1
- b) plus petit que h1
- c) un lien
- d) vide
**Réponse :** b
**Explication :** Plus le numéro grandit, plus le titre rétrécit.

### 3.
p signifie :
- a) picture
- b) paragraph
- c) page
- d) padding
**Réponse :** b
**Explication :** paragraph.

### 4.
div est plutôt :
- a) en ligne
- b) un bloc
- c) un audio
- d) un commentaire
**Réponse :** b
**Explication :** div = block container.

### 5.
span est plutôt :
- a) un bloc pleine largeur
- b) en ligne dans le texte
- c) un titre
- d) une liste
**Réponse :** b
**Explication :** span reste dans la phrase.

### 6.
Combien de niveaux de titres HTML ?
- a) 3
- b) 4
- c) 6
- d) 10
**Réponse :** c
**Explication :** h1 à h6.

### 7.
On met plusieurs phrases longues surtout dans :
- a) h1
- b) p
- c) title
- d) br
**Réponse :** b
**Explication :** p = paragraphe de texte.

### 8.
Pour grouper image + titre + prix d’une carte on utilise souvent :
- a) span
- b) div
- c) br
- d) title
**Réponse :** b
**Explication :** div = boîte.

### 9.
Pour colorer seulement le mot « Alger » plus tard en CSS on entoure avec :
- a) div
- b) span
- c) hr
- d) html
**Réponse :** b
**Explication :** span pour un bout de texte.

### 10.
Le contenu visible va dans :
- a) head
- b) body
- c) DOCTYPE
- d) charset
**Réponse :** b
**Explication :** body = page visible.

### 11.
h3 est :
- a) plus important que h1
- b) un sous-titre plus petit que h2
- c) une image
- d) un lien
**Réponse :** b
**Explication :** h1 > h2 > h3 …

### 12.
On peut mettre un span :
- a) seulement dans head
- b) dans un p
- c) à la place de html
- d) sans balise ouvrante
**Réponse :** b
**Explication :** span vit dans le texte.

### 13.
div sans CSS :
- a) est forcément vert
- b) prend en général toute la largeur (bloc)
- c) est invisible
- d) crée un onglet
**Réponse :** b
**Explication :** Comportement bloc par défaut.

### 14.
Le titre de l’onglet n’est PAS :
- a) title
- b) h1
- c) dans head
- d) un élément HTML
**Réponse :** b
**Explication :** h1 est dans la page, pas dans l’onglet.

### 15.
Quel élément n’est PAS un titre ?
- a) h4
- b) p
- c) h2
- d) h5
**Réponse :** b
**Explication :** p = paragraphe.

### 16.
On écrit un titre de section “Voitures” plutôt avec :
- a) h1 si la page s’appelle déjà Ouedkniss
- b) six h1
- c) span seulement
- d) hr seulement
**Réponse :** a
**Explication :** h1 = site/page, h2 = section.

### 17.
HTML sert d’abord à :
- a) donner un rôle / une structure au contenu
- b) dessiner des ombres 3D
- c) remplacer JavaScript
- d) héberger des vidéos YouTube uniquement
**Réponse :** a
**Explication :** HTML = structure.

### 18.
On ferme un p avec :
- a) </p>
- b) <p>
- c) </br>
- d) </img>
**Réponse :** a
**Explication :** Balise fermante </p>.

### 19.
Un div peut contenir :
- a) seulement du texte brut sans balises
- b) plusieurs éléments (h2, p, img…)
- c) uniquement un head
- d) un DOCTYPE
**Réponse :** b
**Explication :** div est un conteneur.

### 20.
span autour d’un prix sert à :
- a) créer un fichier MP3
- b) cibler ce mot plus tard (couleur, gras…)
- c) ouvrir YouTube
- d) remplacer charset
**Réponse :** b
**Explication :** span = crochet sémantique/visuel dans le texte.

## Exercices pratiques (20)

### 1.
**Consigne :** Ajoute un h1 « Ouedkniss ».

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h1>Ouedkniss</h1>
```

**Indice :** Balise h1.

### 2.
**Consigne :** Ajoute un h2 « Téléphones ».

**Code de départ :**
```html
<h1>Ouedkniss</h1>
```

**Correction :**
```html
<h1>Ouedkniss</h1>
<h2>Téléphones</h2>
```

**Indice :** h2 sous h1.

### 3.
**Consigne :** Écris un paragraphe de description.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>iPhone 13 128 Go, état 9/10, Alger Centre.</p>
```

**Indice :** p

### 4.
**Consigne :** Crée un span autour de « Alger ».

**Code de départ :**
```html
<p>Ville : Alger</p>
```

**Correction :**
```html
<p>Ville : <span>Alger</span></p>
```

**Indice :** span

### 5.
**Consigne :** Regroupe h3 et p dans un div.

**Code de départ :**
```html
<h3>Peugeot 208</h3>
<p>Hydra</p>
```

**Correction :**
```html
<div>
  <h3>Peugeot 208</h3>
  <p>Hydra</p>
</div>
```

**Indice :** div enveloppe.

### 6.
**Consigne :** Ajoute h4, h5 et h6 pour un contact.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h4>Détails</h4>
<h5>Contact</h5>
<h6>Annonce n°20481</h6>
```

**Indice :** niveaux 4 à 6.

### 7.
**Consigne :** Prix dans un span à l’intérieur du p.

**Code de départ :**
```html
<p>Prix : 85000 DA</p>
```

**Correction :**
```html
<p>Prix : <span>85000 DA</span></p>
```

**Indice :** span

### 8.
**Consigne :** Deux cartes (deux div) l’une sous l’autre.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<div><h3>iPhone 13</h3></div>
<div><h3>Galaxy A54</h3></div>
```

**Indice :** deux div.

### 9.
**Consigne :** Un h3 « Galaxy A54 » et un p « Oran ».

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h3>Galaxy A54</h3>
<p>Oran</p>
```

**Indice :** h3 + p.

### 10.
**Consigne :** span autour de « 9/10 ».

**Code de départ :**
```html
<p>État 9/10</p>
```

**Correction :**
```html
<p>État <span>9/10</span></p>
```

**Indice :** span

### 11.
**Consigne :** Page avec h1, h2, p.

**Code de départ :**
```html
<body></body>
```

**Correction :**
```html
<body>
  <h1>Annonces</h1>
  <h2>Voitures</h2>
  <p>Peugeot 208 à Alger.</p>
</body>
```

**Indice :** ordre titres puis texte.

### 12.
**Consigne :** div + h2 + deux p.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<div>
  <h2>F3 Hydra</h2>
  <p>85 m2</p>
  <p>3e étage</p>
</div>
```

**Indice :** un seul div parent.

### 13.
**Consigne :** N’utilise pas h1 deux fois : un h1 et un h2.

**Code de départ :**
```html
<h1>Site</h1>
<h1>Section</h1>
```

**Correction :**
```html
<h1>Site</h1>
<h2>Section</h2>
```

**Indice :** section = h2.

### 14.
**Consigne :** Texte « Bienvenue » dans un p, pas dans un h1.

**Code de départ :**
```html
<h1>Bienvenue sur la fiche.</h1>
```

**Correction :**
```html
<p>Bienvenue sur la fiche.</p>
```

**Indice :** p pour le texte courant.

### 15.
**Consigne :** Entoure seulement le prénom avec span.

**Code de départ :**
```html
<p>Karim B. — Alger</p>
```

**Correction :**
```html
<p><span>Karim</span> B. — Alger</p>
```

**Indice :** span autour de Karim.

### 16.
**Consigne :** Ajoute un h2 vide de contenu « À propos ».

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h2>À propos</h2>
```

**Indice :** h2

### 17.
**Consigne :** Trois niveaux : h1 site, h2 catégorie, h3 produit.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h1>Ouedkniss</h1>
<h2>Voitures</h2>
<h3>Peugeot 208</h3>
```

**Indice :** hiérarchie.

### 18.
**Consigne :** Un div avec un span de ville.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<div>
  <p>Ville : <span>Oran</span></p>
</div>
```

**Indice :** div > p > span.

### 19.
**Consigne :** Paragraphe de 2 phrases sur un téléphone.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>Samsung Galaxy A54 128 Go. Boîte et facture disponibles à Oran.</p>
```

**Indice :** un seul p.

### 20.
**Consigne :** Carte complète : div, h3, p, span prix.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<div>
  <h3>iPhone 13</h3>
  <p>Alger</p>
  <p>Prix : <span>85000 DA</span></p>
</div>
```

**Indice :** comme une annonce.
