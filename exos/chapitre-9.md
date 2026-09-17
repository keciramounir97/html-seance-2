# Chapitre 9 — Vidéo

## Exercices théoriques (20)

### 1.
L’élément pour un fichier vidéo local est :
- a) video
- b) audio
- c) ol
- d) title
**Réponse :** a
**Explication :** Pas YouTube : YouTube = iframe.

### 2.
Sans controls :
- a) pas de boutons play/pause
- b) la video devient une liste
- c) UTF-8 se casse
- d) on a un favicon
**Réponse :** a
**Explication :** Toujours controls en cours.

### 3.
source sert à :
- a) plusieurs formats ; le navigateur saute si non supporté
- b) créer un h1
- c) un commentaire
- d) un dl
**Réponse :** a
**Explication :** mp4, webm, ogg.

### 4.
type d’un MP4 :
- a) video/mp4
- b) audio/mpeg
- c) text/css
- d) image/png
**Réponse :** a
**Explication :** Attribut type de source.

### 5.
Le format le plus sûr aujourd’hui :
- a) MP4
- b) un fichier Word
- c) un ol
- d) un favicon
**Réponse :** a
**Explication :** Très compatible.

### 6.
poster :
- a) image avant la lecture
- b) un type audio
- c) un ul
- d) un charset
**Réponse :** a
**Explication :** Miniature.

### 7.
muted + autoplay :
- a) souvent autorisé (autoplay seul est bloqué)
- b) interdit en HTML
- c) crée un footer
- d) est un li
**Réponse :** a
**Explication :** Politique des navigateurs.

### 8.
loop :
- a) recommence en boucle
- b) ouvre un onglet
- c) est un dt
- d) remplace src
**Réponse :** a
**Explication :** Boucle.

### 9.
Le texte dans video s’affiche si :
- a) aucun format n’est lu
- b) on a un h1
- c) on a UTF-8 seulement
- d) on a un nav
**Réponse :** a
**Explication :** Fallback.

### 10.
width / height :
- a) taille du lecteur
- b) couleur
- c) une liste
- d) un emoji
**Réponse :** a
**Explication :** Comme une image.

### 11.
YouTube s’intègre avec :
- a) iframe, pas video
- b) ul
- c) mark
- d) sub
**Réponse :** a
**Explication :** Chapitre 11.

### 12.
source est un élément :
- a) vide
- b) un titre
- c) un main
- d) un article
**Réponse :** a
**Explication :** Pas de </source>.

### 13.
preload :
- a) auto / metadata / none
- b) ul / ol / dl
- c) b / i / u
- d) header / footer
**Réponse :** a
**Explication :** Chargement.

### 14.
On met autant de source que :
- a) de formats disponibles
- b) de h1
- c) de wilayas
- d) de favicons
**Réponse :** a
**Explication :** Le navigateur choisit.

### 15.
src sur video (cas simple) :
- a) chemin du fichier
- b) un dt
- c) un target
- d) un rel
**Réponse :** a
**Explication :** videos/video.mp4

### 16.
webm type :
- a) video/webm
- b) audio/wav
- c) text/html
- d) image/x-icon
**Réponse :** a
**Explication :** Deuxième format courant.

### 17.
ogg vidéo type :
- a) video/ogg
- b) audio/mpeg
- c) application/pdf
- d) font/ttf
**Réponse :** a
**Explication :** Troisième format.

### 18.
video contient source, pas l’inverse :
- a) Vrai
- b) Faux, source contient video
- c) Faux, c’est ol
- d) Faux, c’est head
**Réponse :** a
**Explication :** Parent video.

### 19.
Un fichier .docx dans video :
- a) ne se lira pas comme une video
- b) devient un h1
- c) est recommandé
- d) remplace charset
**Réponse :** a
**Explication :** Mauvais type.

### 20.
controls est un attribut :
- a) booléen (présent = afficher la barre)
- b) qui vaut toujours mp4
- c) de ol
- d) de title onglet
**Réponse :** a
**Explication :** Pas besoin de ="true".

## Exercices pratiques (20)

### 1.
**Consigne :** video simple + controls.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<video src="videos/video.mp4" controls></video>
```

**Indice :** src + controls

### 2.
**Consigne :** Ajoute controls.

**Code de départ :**
```html
<video src="videos/video.mp4"></video>
```

**Correction :**
```html
<video src="videos/video.mp4" controls></video>
```

**Indice :** controls

### 3.
**Consigne :** width 640 height 360.

**Code de départ :**
```html
<video src="videos/video.mp4" controls></video>
```

**Correction :**
```html
<video src="videos/video.mp4" controls width="640" height="360"></video>
```

**Indice :** taille

### 4.
**Consigne :** 3 source mp4 webm ogg.

**Code de départ :**
```html
<video controls></video>
```

**Correction :**
```html
<video controls>
<source src="videos/video.mp4" type="video/mp4">
<source src="videos/video.webm" type="video/webm">
<source src="videos/video.ogg" type="video/ogg">
</video>
```

**Indice :** formats

### 5.
**Consigne :** Texte fallback.

**Code de départ :**
```html
<video src="videos/video.mp4" controls></video>
```

**Correction :**
```html
<video src="videos/video.mp4" controls>Ton navigateur ne lit pas la vidéo.</video>
```

**Indice :** texte intérieur.

### 6.
**Consigne :** muted loop.

**Code de départ :**
```html
<video src="videos/video.mp4" controls></video>
```

**Correction :**
```html
<video src="videos/video.mp4" controls muted loop></video>
```

**Indice :** deux attributs.

### 7.
**Consigne :** poster.

**Code de départ :**
```html
<video src="videos/video.mp4" controls></video>
```

**Correction :**
```html
<video src="videos/video.mp4" controls poster="images/apercu.jpg"></video>
```

**Indice :** poster

### 8.
**Consigne :** type manquant sur source.

**Code de départ :**
```html
<source src="videos/video.mp4">
```

**Correction :**
```html
<source src="videos/video.mp4" type="video/mp4">
```

**Indice :** type

### 9.
**Consigne :** Corrige audio pour une video.

**Code de départ :**
```html
<audio src="videos/video.mp4" controls></audio>
```

**Correction :**
```html
<video src="videos/video.mp4" controls></video>
```

**Indice :** video

### 10.
**Consigne :** Chemin videos/video.mp4.

**Code de départ :**
```html
<video controls></video>
```

**Correction :**
```html
<video src="videos/video.mp4" controls></video>
```

**Indice :** src

### 11.
**Consigne :** h2 + video visite.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h2>Visite virtuelle — F3 Hydra</h2>
<video src="videos/video.mp4" controls width="640"></video>
```

**Indice :** exemple réel.

### 12.
**Consigne :** preload none.

**Code de départ :**
```html
<video src="v.mp4" controls></video>
```

**Correction :**
```html
<video src="v.mp4" controls preload="none"></video>
```

**Indice :** preload

### 13.
**Consigne :** Deuxieme source webm.

**Code de départ :**
```html
<video controls>
<source src="v.mp4" type="video/mp4">
</video>
```

**Correction :**
```html
<video controls>
<source src="v.mp4" type="video/mp4">
<source src="v.webm" type="video/webm">
</video>
```

**Indice :** ajouter source.

### 14.
**Consigne :** autoplay muted.

**Code de départ :**
```html
<video src="v.mp4" controls></video>
```

**Correction :**
```html
<video src="v.mp4" controls autoplay muted></video>
```

**Indice :** les deux.

### 15.
**Consigne :** Ne pas utiliser iframe pour un mp4 local.

**Code de départ :**
```html
<iframe src="videos/video.mp4"></iframe>
```

**Correction :**
```html
<video src="videos/video.mp4" controls></video>
```

**Indice :** video

### 16.
**Consigne :** height 280.

**Code de départ :**
```html
<video src="v.mp4" controls width="500"></video>
```

**Correction :**
```html
<video src="v.mp4" controls width="500" height="280"></video>
```

**Indice :** height

### 17.
**Consigne :** source ogg.

**Code de départ :**
```html
<video controls></video>
```

**Correction :**
```html
<video controls>
<source src="videos/video.ogg" type="video/ogg">
</video>
```

**Indice :** video/ogg

### 18.
**Consigne :** Article + video.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<article>
<h3>Visite F3</h3>
<video src="videos/video.mp4" controls></video>
</article>
```

**Indice :** conteneur + média.

### 19.
**Consigne :** Corrige type audio/mpeg sur mp4.

**Code de départ :**
```html
<source src="v.mp4" type="audio/mpeg">
```

**Correction :**
```html
<source src="v.mp4" type="video/mp4">
```

**Indice :** video/mp4

### 20.
**Consigne :** Lecteur complet 3 formats + fallback.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<video controls width="500">
<source src="videos/video.mp4" type="video/mp4">
<source src="videos/video.webm" type="video/webm">
<source src="videos/video.ogg" type="video/ogg">
Navigateur non supporté.
</video>
```

**Indice :** notes du chapitre 9.
