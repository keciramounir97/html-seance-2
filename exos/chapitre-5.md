# Chapitre 5 — Attributs, liens, images

## Exercices théoriques (20)

### 1.
Un attribut s’écrit :
- a) dans la balise fermante
- b) nom="valeur" dans la balise ouvrante
- c) après </html>
- d) dans un commentaire seulement
**Réponse :** b
**Explication :** Toujours la balise ouvrante.

### 2.
href sert à :
- a) l’adresse du lien
- b) une image locale seulement
- c) un saut de ligne
- d) un titre d’onglet
**Réponse :** a
**Explication :** hypertext reference.

### 3.
target="_blank" :
- a) ouvre un nouvel onglet
- b) met en gras
- c) ajoute UTF-8
- d) crée un ul
**Réponse :** a
**Explication :** Garde la page actuelle ouverte.

### 4.
src sur img :
- a) chemin ou URL de l’image
- b) texte alternatif
- c) infobulle
- d) lien hypertexte
**Réponse :** a
**Explication :** source du fichier.

### 5.
alt sert à :
- a) décrire l’image (accessibilité + image cassée)
- b) ouvrir YouTube
- c) numéroter une liste
- d) remplacer head
**Réponse :** a
**Explication :** Obligatoire pour une image correcte.

### 6.
title (attribut) :
- a) infobulle au survol
- b) texte de l’onglet
- c) un iframe
- d) un dl
**Réponse :** a
**Explication :** Ne pas confondre avec l’élément title.

### 7.
Sans href, a :
- a) ne mène nulle part
- b) devient une video
- c) est un h1
- d) est vide comme br
**Réponse :** a
**Explication :** href est essentiel.

### 8.
width et height sur img :
- a) tailles d’affichage
- b) couleur
- c) UTF-8
- d) target
**Réponse :** a
**Explication :** Pixels souvent.

### 9.
class et id :
- a) identifient / groupent pour le CSS plus tard
- b) lisent le MP3
- c) sont des listes
- d) vont dans DOCTYPE
**Réponse :** a
**Explication :** Attributs globaux.

### 10.
Un lien interne vers index.html :
- a) <a href="index.html">Accueil</a>
- b) <img href="index.html">
- c) <p src="index.html">
- d) <br href="index.html">
**Réponse :** a
**Explication :** a + href fichier local.

### 11.
img est :
- a) vide
- b) un titre
- c) un ol
- d) un head
**Réponse :** a
**Explication :** Pas de </img>.

### 12.
On peut mettre une image dans un lien :
- a) oui : a enveloppe img
- b) jamais
- c) seulement dans head
- d) seulement avec audio
**Réponse :** a
**Explication :** Image cliquable.

### 13.
https:// est :
- a) une URL absolue (site externe)
- b) un commentaire
- c) un favicon obligatoire
- d) un h6
**Réponse :** a
**Explication :** Vers un autre site.

### 14.
alt vide alt="" :
- a) image décorative (acceptable parfois)
- b) crée une video
- c) est href
- d) ouvre un onglet
**Réponse :** a
**Explication :** Sinon décrire vraiment.

### 15.
L’ordre des attributs :
- a) libre, tous dans la balise ouvrante
- b) href après la balise fermante
- c) alt dans head
- d) src dans title onglet
**Réponse :** a
**Explication :** src, alt, title, width…

### 16.
Un lien sans texte visible :
- a) est peu accessible (mettre un texte ou un alt d’image)
- b) est obligatoire
- c) remplace charset
- d) crée dl
**Réponse :** a
**Explication :** Toujours un contenu cliquable clair.

### 17.
target par défaut :
- a) même onglet
- b) _blank
- c) une video
- d) head
**Réponse :** a
**Explication :** Sans target = même page.

### 18.
photo.png dans images/ :
- a) src="images/photo.png"
- b) href="images/photo.png" sur img
- c) alt="images/photo.png" seulement
- d) src dans a
**Réponse :** a
**Explication :** src pour img, href pour a.

### 19.
title sur img :
- a) infobulle, en plus de alt
- b) remplace src
- c) est un h1
- d) ouvre YouTube
**Réponse :** a
**Explication :** alt ≠ title.

### 20.
a est l’abréviation de :
- a) anchor
- b) audio
- c) article
- d) aside
**Réponse :** a
**Explication :** Ancre / hyperlien.

## Exercices pratiques (20)

### 1.
**Consigne :** Lien Google.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<a href="https://www.google.com">Google</a>
```

**Indice :** a href

### 2.
**Consigne :** Nouvel onglet.

**Code de départ :**
```html
<a href="https://www.google.com">Google</a>
```

**Correction :**
```html
<a href="https://www.google.com" target="_blank">Google</a>
```

**Indice :** target

### 3.
**Consigne :** Infobulle sur p.

**Code de départ :**
```html
<p>Karim</p>
```

**Correction :**
```html
<p title="Vendeur">Karim</p>
```

**Indice :** title

### 4.
**Consigne :** Image avec alt.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<img src="images/image.png" alt="Téléphone à Oran">
```

**Indice :** img

### 5.
**Consigne :** Image 200×120.

**Code de départ :**
```html
<img src="a.png" alt="a">
```

**Correction :**
```html
<img src="a.png" alt="a" width="200" height="120">
```

**Indice :** width height

### 6.
**Consigne :** Image dans un lien.

**Code de départ :**
```html
<img src="html.png" alt="HTML">
```

**Correction :**
```html
<a href="https://www.w3schools.com"><img src="html.png" alt="HTML"></a>
```

**Indice :** a autour.

### 7.
**Consigne :** Lien interne about.html.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<a href="about.html">À propos</a>
```

**Indice :** href local.

### 8.
**Consigne :** alt + title sur img.

**Code de départ :**
```html
<img src="v.png">
```

**Correction :**
```html
<img src="v.png" alt="Peugeot 208" title="1 850 000 DA">
```

**Indice :** deux attributs.

### 9.
**Consigne :** class sur img.

**Code de départ :**
```html
<img src="v.png" alt="v">
```

**Correction :**
```html
<img src="v.png" alt="v" class="annonce">
```

**Indice :** class

### 10.
**Consigne :** id unique.

**Code de départ :**
```html
<img src="v.png" alt="v">
```

**Correction :**
```html
<img src="v.png" alt="v" id="photo-principale">
```

**Indice :** id

### 11.
**Consigne :** Corrige href sur img.

**Code de départ :**
```html
<img href="a.png" alt="a">
```

**Correction :**
```html
<img src="a.png" alt="a">
```

**Indice :** src pas href.

### 12.
**Consigne :** Corrige src sur a.

**Code de départ :**
```html
<a src="https://www.google.com">Google</a>
```

**Correction :**
```html
<a href="https://www.google.com">Google</a>
```

**Indice :** href

### 13.
**Consigne :** Menu de 2 liens.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p><a href="index.html">Accueil</a> | <a href="contact.html">Contact</a></p>
```

**Indice :** deux a.

### 14.
**Consigne :** Image + paragraphe title.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p title="Fiche">Galaxy A54</p>
<img src="images/image.png" alt="Galaxy A54">
```

**Indice :** p + img.

### 15.
**Consigne :** Lien Facebook nouvel onglet.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<a href="https://www.facebook.com" target="_blank">Facebook</a>
```

**Indice :** _blank

### 16.
**Consigne :** width 280 height 160.

**Code de départ :**
```html
<img src="p.png" alt="p">
```

**Correction :**
```html
<img src="p.png" alt="p" width="280" height="160">
```

**Indice :** nombres.

### 17.
**Consigne :** Trois attributs img.

**Code de départ :**
```html
<img>
```

**Correction :**
```html
<img src="p.png" alt="Annonce" title="A54">
```

**Indice :** src alt title

### 18.
**Consigne :** Texte du lien clair.

**Code de départ :**
```html
<a href="https://www.google.com">clique ici</a>
```

**Correction :**
```html
<a href="https://www.google.com">Rechercher sur Google</a>
```

**Indice :** éviter « clique ici ».

### 19.
**Consigne :** Chemin images/image2.png.

**Code de départ :**
```html
<img alt="2">
```

**Correction :**
```html
<img src="images/image2.png" alt="Annonce 2">
```

**Indice :** src

### 20.
**Consigne :** Mini fiche : p title, lien blank, img.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p title="Vendeur">Karim — Alger</p>
<a href="https://www.google.com" target="_blank">Google</a>
<img src="images/image.png" alt="Annonce Alger">
```

**Indice :** les 3 idées du chapitre.
