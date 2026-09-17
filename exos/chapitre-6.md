# Chapitre 6 — Les listes

## Exercices théoriques (20)

### 1.
ul signifie :
- a) unordered list (puces)
- b) unique link
- c) under line
- d) UTF list
**Réponse :** a
**Explication :** Liste à puces.

### 2.
ol signifie :
- a) ordered list (numéros)
- b) old link
- c) open line
- d) only list
**Réponse :** a
**Explication :** 1. 2. 3.

### 3.
Chaque ligne d’un ul/ol est :
- a) li (list item)
- b) dt
- c) source
- d) meta
**Réponse :** a
**Explication :** li dans ul ou ol.

### 4.
dl est :
- a) description list
- b) div long
- c) data link
- d) dark list
**Réponse :** a
**Explication :** Glossaire.

### 5.
dt + dd :
- a) terme + définition
- b) deux titres h1
- c) audio + video
- d) head + body
**Réponse :** a
**Explication :** Pas de li dans dl.

### 6.
Menu de réseaux sociaux → plutôt :
- a) ul
- b) ol
- c) video
- d) title
**Réponse :** a
**Explication :** L’ordre n’est pas une recette.

### 7.
Étapes d’achat → plutôt :
- a) ol
- b) span
- c) hr
- d) iframe
**Réponse :** a
**Explication :** L’ordre compte.

### 8.
HTML n’est pas une base de données, une liste est :
- a) une présentation visuelle
- b) un serveur SQL
- c) un fichier MP4
- d) un charset
**Réponse :** a
**Explication :** Comme Word : puces ou numéros.

### 9.
On peut mettre un a dans un li :
- a) oui
- b) non
- c) seulement dans head
- d) seulement avec audio
**Réponse :** a
**Explication :** Menu de liens.

### 10.
On peut mettre un img dans un li :
- a) oui (galerie)
- b) jamais
- c) ça casse UTF-8
- d) seulement en h1
**Réponse :** a
**Explication :** Galerie numérotée = ol + img.

### 11.
Sans li, ul :
- a) est incorrect / incomplet
- b) devient une video
- c) est un favicon
- d) remplace main
**Réponse :** a
**Explication :** ul contient des li.

### 12.
Imbriquer une liste :
- a) ul dans un li
- b) ul dans head
- c) li dans title onglet
- d) ol dans charset
**Réponse :** a
**Explication :** Sous-liste.

### 13.
Wilayas (Alger, Oran…) :
- a) ul
- b) ol si le rang compte (classement)
- c) les deux selon le besoin
- d) iframe seulement
**Réponse :** c
**Explication :** Puces ou classement.

### 14.
dt veut dire :
- a) description term
- b) div title
- c) data table
- d) dark theme
**Réponse :** a
**Explication :** Le mot.

### 15.
dd veut dire :
- a) description (définition)
- b) document data
- c) doctype default
- d) drag drop
**Réponse :** a
**Explication :** L’explication du dt.

### 16.
Glossaire HTML / CSS / JS → :
- a) dl
- b) video
- c) img
- d) br seulement
**Réponse :** a
**Explication :** Paires mot / sens.

### 17.
start="3" sur ol :
- a) commence la numérotation à 3
- b) crée 3 videos
- c) est un iframe
- d) casse li
**Réponse :** a
**Explication :** Attribut d’ol.

### 18.
type="A" sur ol :
- a) A. B. C. au lieu de 1. 2. 3.
- b) ajoute du son
- c) est UTF-8
- d) ouvre YouTube
**Réponse :** a
**Explication :** Lettres.

### 19.
Une liste n’est PAS :
- a) un stockage de base de données
- b) une présentation
- c) du HTML
- d) des li groupés
**Réponse :** a
**Explication :** Juste de la mise en forme structurelle.

### 20.
li peut contenir :
- a) texte, liens, images, même un div
- b) seulement un chiffre
- c) uniquement head
- d) un DOCTYPE
**Réponse :** a
**Explication :** Conteneur d’item.

## Exercices pratiques (20)

### 1.
**Consigne :** ul de 3 wilayas.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ul>
<li>Alger</li>
<li>Oran</li>
<li>Constantine</li>
</ul>
```

**Indice :** ul>li

### 2.
**Consigne :** ol de 3 étapes.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ol>
<li>Contacter</li>
<li>Voir</li>
<li>Payer</li>
</ol>
```

**Indice :** ol>li

### 3.
**Consigne :** dl HTML/CSS.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<dl>
<dt>HTML</dt>
<dd>Structure la page.</dd>
<dt>CSS</dt>
<dd>Habille la page.</dd>
</dl>
```

**Indice :** dt dd

### 4.
**Consigne :** Ajoute un 4e li.

**Code de départ :**
```html
<ul><li>A</li><li>B</li><li>C</li></ul>
```

**Correction :**
```html
<ul><li>A</li><li>B</li><li>C</li><li>D</li></ul>
```

**Indice :** un li de plus.

### 5.
**Consigne :** Transforme ul en ol.

**Code de départ :**
```html
<ul><li>Un</li><li>Deux</li></ul>
```

**Correction :**
```html
<ol><li>Un</li><li>Deux</li></ol>
```

**Indice :** changer la balise parent.

### 6.
**Consigne :** Liens dans ul.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ul>
<li><a href="https://www.google.com">Google</a></li>
<li><a href="https://www.facebook.com">Facebook</a></li>
</ul>
```

**Indice :** a dans li.

### 7.
**Consigne :** Images dans ol.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ol>
<li><img src="images/image.png" alt="1" width="100"></li>
<li><img src="images/image2.png" alt="2" width="100"></li>
</ol>
```

**Indice :** img dans li.

### 8.
**Consigne :** Caractéristiques téléphone en ul.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ul>
<li>128 Go</li>
<li>Noir</li>
<li>9/10</li>
</ul>
```

**Indice :** puces produit.

### 9.
**Consigne :** Glossaire État 9/10.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<dl>
<dt>État 9/10</dt>
<dd>Très bon état, micro-rayures possibles.</dd>
</dl>
```

**Indice :** dt dd

### 10.
**Consigne :** Sous-liste : ul dans li.

**Code de départ :**
```html
<ul><li>Alger</li></ul>
```

**Correction :**
```html
<ul>
<li>Alger
  <ul><li>Hydra</li><li>Centre</li></ul>
</li>
</ul>
```

**Indice :** imbriquer.

### 11.
**Consigne :** Corrige li hors ul.

**Code de départ :**
```html
<li>Alger</li><li>Oran</li>
```

**Correction :**
```html
<ul>
<li>Alger</li>
<li>Oran</li>
</ul>
```

**Indice :** parent ul.

### 12.
**Consigne :** Corrige dt dans ul.

**Code de départ :**
```html
<ul><dt>HTML</dt><dd>Langage</dd></ul>
```

**Correction :**
```html
<dl><dt>HTML</dt><dd>Langage</dd></dl>
```

**Indice :** dl pas ul.

### 13.
**Consigne :** ol start à 3.

**Code de départ :**
```html
<ol><li>C</li><li>D</li></ol>
```

**Correction :**
```html
<ol start="3"><li>C</li><li>D</li></ol>
```

**Indice :** start

### 14.
**Consigne :** 5 réseaux en ul.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ul>
<li>Google</li>
<li>Facebook</li>
<li>Twitter</li>
<li>Instagram</li>
<li>Linkedin</li>
</ul>
```

**Indice :** 5 li.

### 15.
**Consigne :** Recette ol 4 étapes icône.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ol>
<li>Flaticon</li>
<li>Recherche</li>
<li>Télécharger</li>
<li>img src</li>
</ol>
```

**Indice :** ordre.

### 16.
**Consigne :** dl trois termes web.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<dl>
<dt>HTML</dt><dd>Structure</dd>
<dt>CSS</dt><dd>Style</dd>
<dt>JS</dt><dd>Interaction</dd>
</dl>
```

**Indice :** 3 paires.

### 17.
**Consigne :** Mélange page : ul + ol.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h2>Avantages</h2>
<ul><li>Boîte</li><li>Facture</li></ul>
<h2>Étapes</h2>
<ol><li>Appeler</li><li>Payer</li></ol>
```

**Indice :** deux listes.

### 18.
**Consigne :** li avec span de prix.

**Code de départ :**
```html
<ul><li>iPhone 85000</li></ul>
```

**Correction :**
```html
<ul><li>iPhone <span>85000 DA</span></li></ul>
```

**Indice :** span

### 19.
**Consigne :** Menu nav ul.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<nav>
<ul>
<li><a href="#">Accueil</a></li>
<li><a href="#">Annonces</a></li>
</ul>
</nav>
```

**Indice :** nav>ul>li>a

### 20.
**Consigne :** Fiche complète listes.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h2>Galaxy A54</h2>
<ul><li>128 Go</li><li>Noir</li></ul>
<ol><li>Contacter</li><li>Voir</li><li>Payer</li></ol>
<dl><dt>IMEI</dt><dd>Numéro unique du téléphone</dd></dl>
```

**Indice :** ul ol dl.
