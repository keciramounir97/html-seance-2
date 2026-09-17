# Chapitre 11 — Iframe

## Exercices théoriques (20)

### 1.
iframe signifie :
- a) inline frame (cadre dans la page)
- b) image frame PNG
- c) icon font
- d) input form
**Réponse :** a
**Explication :** Fenêtre dans la fenêtre.

### 2.
src d’iframe :
- a) URL ou fichier HTML à afficher
- b) un type audio/mpeg
- c) un alt obligatoire d’img
- d) un li
**Réponse :** a
**Explication :** Destination du cadre.

### 3.
YouTube : URL embed :
- a) /embed/ID pas watch?v=
- b) seulement un mp3
- c) un ol
- d) un charset
**Réponse :** a
**Explication :** Partager → Intégrer.

### 4.
Video locale mp4 → :
- a) élément video, pas iframe
- b) iframe obligatoire
- c) ul
- d) mark
**Réponse :** a
**Explication :** Chaque outil son usage.

### 5.
width et height :
- a) taille du cadre
- b) couleur du texte
- c) UTF-8
- d) favicon
**Réponse :** a
**Explication :** 560×315 souvent YouTube.

### 6.
title sur iframe :
- a) accessibilité (décrire le cadre)
- b) remplace src
- c) est un h1
- d) crée un mp3
**Réponse :** a
**Explication :** Important.

### 7.
allowfullscreen :
- a) autorise le plein écran (YouTube)
- b) crée une liste
- c) est un dt
- d) est charset
**Réponse :** a
**Explication :** Attribut YouTube.

### 8.
Tous les sites autorisent-ils l’iframe ?
- a) Non (sécurité)
- b) Oui toujours
- c) Seulement les PNG
- d) Seulement ol
**Réponse :** a
**Explication :** X-Frame-Options etc.

### 9.
Un iframe trop nombreux :
- a) ralentit la page
- b) améliore UTF-8
- c) remplace head
- d) crée des li
**Réponse :** a
**Explication :** Page plus lourde.

### 10.
Le CSS de ta page :
- a) ne stylise pas l’intérieur du site externe
- b) change YouTube en vert forcément
- c) supprime src
- d) devient un audio
**Réponse :** a
**Explication :** Page séparée.

### 11.
Fichier local chapitre 10 dans iframe :
- a) src="../chapitre-10/index.html"
- b) src="audio.mp3" comme iframe YouTube
- c) src sans chemin
- d) href sur iframe
**Réponse :** a
**Explication :** Chemin relatif.

### 12.
loading="lazy" :
- a) charge le cadre plus tard (performance)
- b) met en gras
- c) est un ol
- d) est un emoji
**Réponse :** a
**Explication :** Utile.

### 13.
frameborder est :
- a) ancien ; préférer le CSS border
- b) obligatoire HTML5
- c) un type mp4
- d) un header
**Réponse :** a
**Explication :** HTML5 moderne.

### 14.
Maps / carte :
- a) souvent un iframe aussi
- b) uniquement ul
- c) uniquement b
- d) uniquement source
**Réponse :** a
**Explication :** Même idée YouTube.

### 15.
allow="..." YouTube :
- a) permissions (autoplay, fullscreen…)
- b) un dt
- c) un charset
- d) un favicon
**Réponse :** a
**Explication :** Copié depuis YouTube.

### 16.
iframe n’est PAS :
- a) l’élément video pour un mp4 à toi
- b) un cadre
- c) capable d’afficher une page
- d) utile pour YouTube
**Réponse :** a
**Explication :** video ≠ iframe.

### 17.
On peut iframe un autre chapitre du cours :
- a) oui, fichier HTML local
- b) non, interdit
- c) seulement en MP3
- d) seulement sans src
**Réponse :** a
**Explication :** Exemple chapitre 11.

### 18.
Sandbox :
- a) restreint ce que l’iframe a le droit de faire
- b) une liste ol
- c) un emoji
- d) un h1
**Réponse :** a
**Explication :** Sécurité avancée.

### 19.
Le contenu iframe est :
- a) une page séparée
- b) des li de ta page
- c) ton head mélangé
- d) un commentaire
**Réponse :** a
**Explication :** Document autre.

### 20.
Intégrer YouTube sans iframe :
- a) pas la méthode vue en cours
- b) avec ul seulement
- c) avec br seulement
- d) avec sub
**Réponse :** a
**Explication :** YouTube donne un iframe.

## Exercices pratiques (20)

### 1.
**Consigne :** iframe local 500×280.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<iframe src="../chapitre-10/index.html" width="500" height="280" title="Audio"></iframe>
```

**Indice :** src local

### 2.
**Consigne :** Ajoute title.

**Code de départ :**
```html
<iframe src="page.html"></iframe>
```

**Correction :**
```html
<iframe src="page.html" title="Aperçu de la page"></iframe>
```

**Indice :** title

### 3.
**Consigne :** YouTube embed.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/U2-JPqrALsA" title="YouTube" allowfullscreen></iframe>
```

**Indice :** embed

### 4.
**Consigne :** Corrige watch?v= en embed.

**Code de départ :**
```html
<iframe src="https://www.youtube.com/watch?v=U2-JPqrALsA"></iframe>
```

**Correction :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YouTube"></iframe>
```

**Indice :** /embed/

### 5.
**Consigne :** allowfullscreen.

**Code de départ :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA"></iframe>
```

**Correction :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" allowfullscreen title="YouTube"></iframe>
```

**Indice :** allowfullscreen

### 6.
**Consigne :** width 560 height 315.

**Code de départ :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA"></iframe>
```

**Correction :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" width="560" height="315" title="YouTube"></iframe>
```

**Indice :** taille YT.

### 7.
**Consigne :** loading lazy.

**Code de départ :**
```html
<iframe src="page.html" title="p"></iframe>
```

**Correction :**
```html
<iframe src="page.html" title="p" loading="lazy"></iframe>
```

**Indice :** lazy

### 8.
**Consigne :** h2 + iframe local.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h2>Aperçu chapitre 10</h2>
<iframe src="../chapitre-10/index.html" title="Audio" width="500" height="280"></iframe>
```

**Indice :** exemple cours.

### 9.
**Consigne :** Corrige video pour YouTube.

**Code de départ :**
```html
<video src="https://www.youtube.com/watch?v=U2-JPqrALsA" controls></video>
```

**Correction :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YouTube" allowfullscreen></iframe>
```

**Indice :** iframe embed

### 10.
**Consigne :** Corrige href sur iframe.

**Code de départ :**
```html
<iframe href="page.html"></iframe>
```

**Correction :**
```html
<iframe src="page.html" title="page"></iframe>
```

**Indice :** src

### 11.
**Consigne :** Deux iframes : local + YT.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<iframe src="../chapitre-10/index.html" title="Local" width="400" height="200"></iframe>
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YouTube" width="400" height="200"></iframe>
```

**Indice :** deux cadres.

### 12.
**Consigne :** allow copié YouTube (autoplay…).

**Code de départ :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA"></iframe>
```

**Correction :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YouTube" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

**Indice :** allow

### 13.
**Consigne :** article + iframe.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<article>
<h3>Tutoriel</h3>
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="Tuto" width="560" height="315"></iframe>
</article>
```

**Indice :** conteneur

### 14.
**Consigne :** title FR descriptif.

**Code de départ :**
```html
<iframe src="page.html"></iframe>
```

**Correction :**
```html
<iframe src="page.html" title="Aperçu de la fiche audio du chapitre 10"></iframe>
```

**Indice :** décrire

### 15.
**Consigne :** Taille 400×250 fichier local.

**Code de départ :**
```html
<iframe src="../chapitre-9/index.html"></iframe>
```

**Correction :**
```html
<iframe src="../chapitre-9/index.html" width="400" height="250" title="Vidéo chapitre 9"></iframe>
```

**Indice :** chapitre 9

### 16.
**Consigne :** Ne pas oublier la balise fermante iframe.

**Code de départ :**
```html
<iframe src="page.html" title="p">
```

**Correction :**
```html
<iframe src="page.html" title="p"></iframe>
```

**Indice :** </iframe>

### 17.
**Consigne :** p d’explication + iframe.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>Je suis dans le chapitre 11.</p>
<iframe src="../chapitre-10/index.html" title="Audio" width="500" height="280"></iframe>
```

**Indice :** comme index.html

### 18.
**Consigne :** referrerpolicy (YT).

**Code de départ :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YT"></iframe>
```

**Correction :**
```html
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YT" referrerpolicy="strict-origin-when-cross-origin"></iframe>
```

**Indice :** copié YT

### 19.
**Consigne :** Mini page 11 : h1 + 2 sections iframe.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h1>Iframe</h1>
<h2>Local</h2>
<iframe src="../chapitre-10/index.html" title="Local" width="500" height="200"></iframe>
<h2>YouTube</h2>
<iframe src="https://www.youtube.com/embed/U2-JPqrALsA" title="YouTube" width="500" height="200" allowfullscreen></iframe>
```

**Indice :** les 2 usages.

### 20.
**Consigne :** sandbox allow-scripts (aperçu doc).

**Code de départ :**
```html
<iframe src="page.html" title="p"></iframe>
```

**Correction :**
```html
<iframe src="page.html" title="p" sandbox="allow-scripts allow-same-origin"></iframe>
```

**Indice :** sécurité
