# Chapitre 3 — Commentaires et éléments vides

## Exercices théoriques (20)

### 1.
Un commentaire HTML commence par :
- a) /*
- b) <!--
- c) //
- d) #
**Réponse :** b
**Explication :** <!-- texte -->

### 2.
Le visiteur voit-il le commentaire ?
- a) Oui, en gros
- b) Non, il est invisible dans la page
- c) Seulement sur mobile
- d) Dans l’onglet
**Réponse :** b
**Explication :** Le navigateur ignore le commentaire à l’affichage.

### 3.
br sert à :
- a) un trait horizontal
- b) un saut de ligne
- c) une image
- d) un titre
**Réponse :** b
**Explication :** br = line break.

### 4.
hr sert à :
- a) une ligne horizontale
- b) un lien
- c) un emoji
- d) UTF-8
**Réponse :** a
**Explication :** Séparateur visuel.

### 5.
img est vide parce que :
- a) il n’a pas de contenu texte entre deux balises ; le fichier est dans src
- b) il est interdit
- c) il va dans head seulement
- d) il remplace html
**Réponse :** a
**Explication :** Élément void.

### 6.
On n’écrit PAS :
- a) </p>
- b) </img>
- c) </div>
- d) </a>
**Réponse :** b
**Explication :** Pas de balise fermante pour img.

### 7.
Parmi ces éléments, lequel est vide ?
- a) p
- b) div
- c) meta
- d) h1
**Réponse :** c
**Explication :** meta, br, hr, img, link, input, source.

### 8.
source (vidéo/audio) est :
- a) un titre
- b) un élément vide
- c) un commentaire
- d) un iframe
**Réponse :** b
**Explication :** Pas de </source>.

### 9.
Plusieurs br d’affilée :
- a) est la meilleure façon de faire tout l’espacement d’un site
- b) marche mais le CSS est préférable pour la mise en page
- c) créent un favicon
- d) sont interdits par UTF-8
**Réponse :** b
**Explication :** br ≠ outil de layout.

### 10.
Un commentaire peut servir à :
- a) désactiver un bout de HTML sans l’effacer
- b) lire un MP3
- c) remplacer charset
- d) créer un ul
**Réponse :** a
**Explication :** On commente le code pour le “éteindre”.

### 11.
link (favicon) est :
- a) vide, dans head
- b) un p
- c) un h1
- d) un audio
**Réponse :** a
**Explication :** link est void.

### 12.
input de formulaire est :
- a) vide
- b) un titre h2
- c) un article
- d) un footer
**Réponse :** a
**Explication :** Pas de </input>.

### 13.
La bonne adresse d’un commentaire fermant :
- a) -->
- b) */
- c) </comment>
- d) ///
**Réponse :** a
**Explication :** <!-- ... -->

### 14.
br vs p :
- a) p = paragraphe (bloc) ; br = aller à la ligne
- b) c’est la même chose
- c) br va dans head
- d) p est vide
**Réponse :** a
**Explication :** Rôles différents.

### 15.
On peut commenter :
- a) une ligne ou un bloc de balises
- b) seulement les images PNG
- c) seulement les emojis
- d) le DOCTYPE obligatoire
**Réponse :** a
**Explication :** Très flexible.

### 16.
hr est :
- a) un élément vide
- b) un lien
- c) une liste
- d) un titre
**Réponse :** a
**Explication :** void.

### 17.
Quelle syntaxe est correcte ?
- a) <br></br>
- b) <br>
- c) </br>
- d) <break>
**Réponse :** b
**Explication :** <br> tout seul.

### 18.
img a besoin de :
- a) src (et alt recommandé)
- b) href seulement
- c) controls
- d) charset
**Réponse :** a
**Explication :** src = fichier.

### 19.
Un commentaire mal fermé peut :
- a) cacher le HTML suivant
- b) créer un MP4
- c) traduire en arabe
- d) ajouter un viewport
**Réponse :** a
**Explication :** Tout jusqu’au prochain --> disparaît.

### 20.
meta charset est un élément :
- a) vide dans head
- b) un paragraphe
- c) un footer
- d) une ul
**Réponse :** a
**Explication :** Configuration, pas de contenu.

## Exercices pratiques (20)

### 1.
**Consigne :** Ajoute un commentaire « menu ».

**Code de départ :**
```html
<nav></nav>
```

**Correction :**
```html
<!-- menu -->
<nav></nav>
```

**Indice :** <!-- -->

### 2.
**Consigne :** Saut de ligne entre nom et ville.

**Code de départ :**
```html
<p>Karim Alger</p>
```

**Correction :**
```html
<p>Karim<br>Alger</p>
```

**Indice :** br

### 3.
**Consigne :** Trait sous le titre.

**Code de départ :**
```html
<h1>Contact</h1>
<p>0550</p>
```

**Correction :**
```html
<h1>Contact</h1>
<hr>
<p>0550</p>
```

**Indice :** hr

### 4.
**Consigne :** Image vide correcte avec alt.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<img src="photo.png" alt="Annonce">
```

**Indice :** pas de </img>

### 5.
**Consigne :** Commente le paragraphe (désactive-le).

**Code de départ :**
```html
<p>Brouillon</p>
```

**Correction :**
```html
<!-- <p>Brouillon</p> -->
```

**Indice :** entourer avec commentaire.

### 6.
**Consigne :** Trois lignes d’adresse avec br.

**Code de départ :**
```html
<p>Karim Hydra 0550</p>
```

**Correction :**
```html
<p>Karim<br>Hydra<br>0550</p>
```

**Indice :** deux br.

### 7.
**Consigne :** Corrige </br> en br correct.

**Code de départ :**
```html
<p>A</br>B</p>
```

**Correction :**
```html
<p>A<br>B</p>
```

**Indice :** <br>

### 8.
**Consigne :** Ajoute hr entre deux annonces.

**Code de départ :**
```html
<h2>iPhone</h2>
<h2>Galaxy</h2>
```

**Correction :**
```html
<h2>iPhone</h2>
<hr>
<h2>Galaxy</h2>
```

**Indice :** hr

### 9.
**Consigne :** Commentaire de section PIED.

**Code de départ :**
```html
<footer>© 2026</footer>
```

**Correction :**
```html
<!-- PIED DE PAGE -->
<footer>© 2026</footer>
```

**Indice :** <!-- -->

### 10.
**Consigne :** meta charset vide dans un head.

**Code de départ :**
```html
<head>
<title>X</title>
</head>
```

**Correction :**
```html
<head>
<meta charset="UTF-8">
<title>X</title>
</head>
```

**Indice :** meta

### 11.
**Consigne :** Deux images l’une sous l’autre (br).

**Code de départ :**
```html
<img src="a.png" alt="a">
<img src="b.png" alt="b">
```

**Correction :**
```html
<img src="a.png" alt="a"><br>
<img src="b.png" alt="b">
```

**Indice :** br entre les img.

### 12.
**Consigne :** Commente l’image.

**Code de départ :**
```html
<img src="x.png" alt="x">
```

**Correction :**
```html
<!-- <img src="x.png" alt="x"> -->
```

**Indice :** commentaire autour.

### 13.
**Consigne :** Adresse 4 lignes.

**Code de départ :**
```html
<p>Nom Rue Ville Tel</p>
```

**Correction :**
```html
<p>Nom<br>Rue<br>Ville<br>Tel</p>
```

**Indice :** br

### 14.
**Consigne :** hr + commentaire.

**Code de départ :**
```html
<h1>A</h1>
```

**Correction :**
```html
<h1>A</h1>
<!-- séparateur -->
<hr>
```

**Indice :** les deux.

### 15.
**Consigne :** Corrige </img>.

**Code de départ :**
```html
<img src="a.png" alt="a"></img>
```

**Correction :**
```html
<img src="a.png" alt="a">
```

**Indice :** élément vide.

### 16.
**Consigne :** link favicon (élément vide).

**Code de départ :**
```html
<head></head>
```

**Correction :**
```html
<head>
<link rel="shortcut icon" href="icon.png">
</head>
```

**Indice :** link

### 17.
**Consigne :** source dans une video.

**Code de départ :**
```html
<video controls></video>
```

**Correction :**
```html
<video controls>
<source src="v.mp4" type="video/mp4">
</video>
```

**Indice :** source vide.

### 18.
**Consigne :** Double hr (deux séparateurs).

**Code de départ :**
```html
<p>A</p>
<p>B</p>
```

**Correction :**
```html
<p>A</p>
<hr>
<hr>
<p>B</p>
```

**Indice :** deux hr.

### 19.
**Consigne :** Commentaire multiligne.

**Code de départ :**
```html
<div>carte</div>
```

**Correction :**
```html
<!--
  carte annonce
-->
<div>carte</div>
```

**Indice :** <!-- sur plusieurs lignes -->

### 20.
**Consigne :** Fiche contact complète.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h1>Contact</h1>
<p>Karim<br>Hydra<br>0550</p>
<hr>
<p>Annonce 20481</p>
```

**Indice :** h1 p br hr.
