# Chapitre 10 — Audio

## Exercices théoriques (20)

### 1.
Même logique que video mais :
- a) sans image
- b) sans controls jamais
- c) uniquement dans head
- d) remplace html
**Réponse :** a
**Explication :** audio = son.

### 2.
Fichier simple :
- a) <audio src="audio/audio.mp3" controls>
- b) <ul src="audio.mp3">
- c) <p controls>
- d) <img src="audio.mp3">
**Réponse :** a
**Explication :** src + controls.

### 3.
type MP3 :
- a) audio/mpeg
- b) video/mp4
- c) text/css
- d) image/png
**Réponse :** a
**Explication :** Parfois écrit audio/mp3.

### 4.
ogg audio :
- a) audio/ogg
- b) video/ogg seulement
- c) text/html
- d) rel icon
**Réponse :** a
**Explication :** Deuxième format.

### 5.
wav :
- a) audio/wav
- b) video/mp4
- c) application/json
- d) font/woff
**Réponse :** a
**Explication :** Troisième format.

### 6.
Si un format n’est pas supporté :
- a) le navigateur saute au source suivant
- b) la page explose
- c) UTF-8 s’enlève
- d) ol se crée
**Réponse :** a
**Explication :** Comme la video.

### 7.
width/height sur audio :
- a) ne s’appliquent pas vraiment (pas une image)
- b) sont obligatoires
- c) créent un iframe
- d) remplacent controls
**Réponse :** a
**Explication :** Barre par défaut.

### 8.
controls sur audio :
- a) play / pause / volume / barre
- b) un h1
- c) un favicon
- d) un dl
**Réponse :** a
**Explication :** Toujours les mettre.

### 9.
loop sur audio :
- a) rejoue en boucle
- b) ouvre Google
- c) est un span
- d) est un header
**Réponse :** a
**Explication :** Musique de fond (avec prudence).

### 10.
autoplay audio :
- a) souvent bloqué sans interaction
- b) toujours autorisé
- c) crée un ul
- d) est charset
**Réponse :** a
**Explication :** Les navigateurs protègent l’utilisateur.

### 11.
video vs audio : poster :
- a) poster existe pour video, pas pour audio
- b) audio a toujours poster
- c) poster est un ol
- d) poster est UTF-8
**Réponse :** a
**Explication :** Pas d’image d’audio.

### 12.
source va dans :
- a) audio (ou video)
- b) title onglet
- c) uniquement nav
- d) DOCTYPE
**Réponse :** a
**Explication :** Parent média.

### 13.
Le plus compatible audio :
- a) MP3
- b) un fichier EXE
- c) un h6
- d) un iframe maps
**Réponse :** a
**Explication :** audio/mpeg.

### 14.
Chemin du cours :
- a) audio/audio.mp3
- b) videos/video.mp4 seulement
- c) icones/html.png comme son
- d) chapitre-1/index.html comme mp3
**Réponse :** a
**Explication :** Corriger audios/ vs audio/.

### 15.
Fallback texte :
- a) entre <audio> et </audio>
- b) dans head seulement
- c) dans charset
- d) dans rel
**Réponse :** a
**Explication :** Si rien n’est lu.

### 16.
preload metadata :
- a) charge les infos, pas tout le fichier
- b) crée 10 ol
- c) est un emoji
- d) est un footer
**Réponse :** a
**Explication :** Compromis.

### 17.
On n’utilise pas audio pour YouTube.
- a) Vrai (iframe)
- b) Faux, audio=YouTube
- c) Faux, ul=YouTube
- d) Faux, mark=YouTube
**Réponse :** a
**Explication :** YouTube = iframe.

### 18.
muted :
- a) sans son
- b) plein écran
- c) liste
- d) sémantique header
**Réponse :** a
**Explication :** Muet.

### 19.
Plusieurs source dans audio :
- a) oui, comme video
- b) interdit
- c) seulement 1 dans tout HTML
- d) uniquement dans ol
**Réponse :** a
**Explication :** Même idée chapitre 9.

### 20.
audio est :
- a) un conteneur (peut contenir source + texte)
- b) vide comme br (jamais de contenu)
- c) un titre h1
- d) un charset
**Réponse :** a
**Explication :** Pas un void element.

## Exercices pratiques (20)

### 1.
**Consigne :** audio mp3 + controls.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<audio src="audio/audio.mp3" controls></audio>
```

**Indice :** src controls

### 2.
**Consigne :** Ajoute controls.

**Code de départ :**
```html
<audio src="audio/audio.mp3"></audio>
```

**Correction :**
```html
<audio src="audio/audio.mp3" controls></audio>
```

**Indice :** controls

### 3.
**Consigne :** 3 formats source.

**Code de départ :**
```html
<audio controls></audio>
```

**Correction :**
```html
<audio controls>
<source src="audio/audio.mp3" type="audio/mpeg">
<source src="audio/audio.ogg" type="audio/ogg">
<source src="audio/audio.wav" type="audio/wav">
</audio>
```

**Indice :** mpeg ogg wav

### 4.
**Consigne :** type audio/mpeg.

**Code de départ :**
```html
<source src="audio/audio.mp3">
```

**Correction :**
```html
<source src="audio/audio.mp3" type="audio/mpeg">
```

**Indice :** type

### 5.
**Consigne :** Fallback.

**Code de départ :**
```html
<audio src="audio/audio.mp3" controls></audio>
```

**Correction :**
```html
<audio src="audio/audio.mp3" controls>Votre navigateur ne prend pas en charge l'audio.</audio>
```

**Indice :** texte

### 6.
**Consigne :** loop.

**Code de départ :**
```html
<audio src="audio/audio.mp3" controls></audio>
```

**Correction :**
```html
<audio src="audio/audio.mp3" controls loop></audio>
```

**Indice :** loop

### 7.
**Consigne :** Corrige video pour un mp3.

**Code de départ :**
```html
<video src="audio/audio.mp3" controls></video>
```

**Correction :**
```html
<audio src="audio/audio.mp3" controls></audio>
```

**Indice :** audio

### 8.
**Consigne :** Corrige le dossier audios/ → audio/.

**Code de départ :**
```html
<source src="audios/audio.mp3" type="audio/mpeg">
```

**Correction :**
```html
<source src="audio/audio.mp3" type="audio/mpeg">
```

**Indice :** chemin du cours.

### 9.
**Consigne :** h2 message vendeur + audio.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<h2>Écoutez la description</h2>
<audio src="audio/audio.mp3" controls></audio>
```

**Indice :** exemple réel.

### 10.
**Consigne :** preload none.

**Code de départ :**
```html
<audio src="a.mp3" controls></audio>
```

**Correction :**
```html
<audio src="a.mp3" controls preload="none"></audio>
```

**Indice :** preload

### 11.
**Consigne :** muted.

**Code de départ :**
```html
<audio src="a.mp3" controls></audio>
```

**Correction :**
```html
<audio src="a.mp3" controls muted></audio>
```

**Indice :** muted

### 12.
**Consigne :** article + audio.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<article>
<h3>Message du vendeur</h3>
<audio src="audio/audio.mp3" controls></audio>
</article>
```

**Indice :** conteneur

### 13.
**Consigne :** Deuxieme source ogg.

**Code de départ :**
```html
<audio controls>
<source src="a.mp3" type="audio/mpeg">
</audio>
```

**Correction :**
```html
<audio controls>
<source src="a.mp3" type="audio/mpeg">
<source src="a.ogg" type="audio/ogg">
</audio>
```

**Indice :** ajouter

### 14.
**Consigne :** type wav.

**Code de départ :**
```html
<source src="a.wav">
```

**Correction :**
```html
<source src="a.wav" type="audio/wav">
```

**Indice :** audio/wav

### 15.
**Consigne :** Ne pas mettre width height comme une image.

**Code de départ :**
```html
<audio src="a.mp3" controls width="500" height="500"></audio>
```

**Correction :**
```html
<audio src="a.mp3" controls></audio>
```

**Indice :** inutile.

### 16.
**Consigne :** autoplay muted (si test).

**Code de départ :**
```html
<audio src="a.mp3" controls></audio>
```

**Correction :**
```html
<audio src="a.mp3" controls autoplay muted></audio>
```

**Indice :** souvent bloqué sinon.

### 17.
**Consigne :** figure + audio + légende.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<figure>
<audio src="audio/audio.mp3" controls></audio>
<figcaption>Description orale de l'annonce</figcaption>
</figure>
```

**Indice :** figcaption

### 18.
**Consigne :** Corrige type video/mp4 sur mp3.

**Code de départ :**
```html
<source src="a.mp3" type="video/mp4">
```

**Correction :**
```html
<source src="a.mp3" type="audio/mpeg">
```

**Indice :** audio/mpeg

### 19.
**Consigne :** p + audio.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>Écoutez avant d'acheter :</p>
<audio src="audio/audio.mp3" controls></audio>
```

**Indice :** intro

### 20.
**Consigne :** Lecteur complet 3 formats.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<audio controls>
<source src="audio/audio.mp3" type="audio/mpeg">
<source src="audio/audio.ogg" type="audio/ogg">
<source src="audio/audio.wav" type="audio/wav">
Ton navigateur ne lit pas l'audio HTML5.
</audio>
```

**Indice :** notes chapitre 10.
