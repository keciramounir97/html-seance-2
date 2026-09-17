# Chapitre 7 — Les icônes

## Exercices théoriques (20)

### 1.
Deux familles d’icônes vues en cours :
- a) image img / police d’icônes (i + librairie)
- b) video / audio seulement
- c) ul / ol seulement
- d) iframe / canvas seulement
**Réponse :** a
**Explication :** PNG vs Akar.

### 2.
Icône PNG : on règle la taille avec :
- a) width et height
- b) font-size seulement
- c) charset
- d) controls
**Réponse :** a
**Explication :** Comme une photo.

### 3.
Icône Akar (élément i) : taille avec :
- a) font-size
- b) width/height d’image
- c) start d’ol
- d) poster
**Réponse :** a
**Explication :** C’est du texte.

### 4.
Couleur d’une icône Akar :
- a) color (comme le texte)
- b) alt
- c) src
- d) type video/mp4
**Réponse :** a
**Explication :** style="color:..."

### 5.
Le script Akar se colle dans :
- a) head
- b) le fichier MP3
- c) un li obligatoire
- d) après </html>
**Réponse :** a
**Explication :** Bibliothèque JS.

### 6.
Flaticon sert à :
- a) trouver et télécharger un PNG
- b) héberger YouTube
- c) créer un dl
- d) remplacer UTF-8
**Réponse :** a
**Explication :** Puis img src.

### 7.
ai-facebook-fill est :
- a) une classe CSS de l’icône
- b) un charset
- c) un type audio
- d) un élément ul
**Réponse :** a
**Explication :** class="ai-..."

### 8.
On peut cliquer une icône si :
- a) on l’entoure d’un a
- b) on ajoute controls
- c) on met ol
- d) on retire href partout
**Réponse :** a
**Explication :** Comme une image-lien.

### 9.
Sans le script Akar, le i :
- a) reste de l’italique / pas l’icône
- b) devient une video
- c) crée un favicon
- d) est un iframe
**Réponse :** a
**Explication :** La librairie transforme i.

### 10.
PNG figé vs police :
- a) changer la couleur d’un PNG est plus dur ; la police se recolore
- b) c’est identique à ol
- c) PNG a besoin de controls
- d) la police a besoin de src mp4
**Réponse :** a
**Explication :** Avantage Akar : color.

### 11.
Étapes Akar : Get started → script GitHub → snippet HTML.
- a) Vrai
- b) Faux, on utilise seulement ol
- c) Faux, Akar est une video
- d) Faux, ça va dans dl
**Réponse :** a
**Explication :** Comme dans tes notes.

### 12.
img alt sur une icône image :
- a) toujours utile (accessibilité)
- b) interdit
- c) remplace le script Akar
- d) est un iframe
**Réponse :** a
**Explication :** Décrire l’icône.

### 13.
font-size: 46px sur i :
- a) agrandit l’icône police
- b) crée 46 listes
- c) est un charset
- d) ouvre YouTube
**Réponse :** a
**Explication :** Comme une police d’écriture.

### 14.
On copie seulement le script, pas toute la page GitHub.
- a) Vrai
- b) Faux
- c) On copie un mp3
- d) On copie un ol
**Réponse :** a
**Explication :** Une balise script.

### 15.
Une icône image n’a pas besoin d’Internet une fois téléchargée.
- a) Vrai (fichier local)
- b) Faux, toujours YouTube
- c) Faux, besoin de Akar
- d) Faux, besoin de ol
**Réponse :** a
**Explication :** PNG dans icones/.

### 16.
Akar a besoin d’Internet pour charger le script unpkg.
- a) Vrai en général
- b) Faux, c’est un PNG local
- c) Faux, c’est ol
- d) Faux, c’est charset
**Réponse :** a
**Explication :** CDN.

### 17.
i était à l’origine :
- a) italique
- b) iframe
- c) image
- d) input
**Réponse :** a
**Explication :** Réutilisé pour les icônes.

### 18.
Mettre width=46 sur un i Akar :
- a) n’est pas la bonne méthode (utiliser font-size)
- b) est obligatoire
- c) crée un mp4
- d) remplace head
**Réponse :** a
**Explication :** Police ≠ bitmap.

### 19.
Icône dans le menu :
- a) a > i ou a > img
- b) source type audio
- c) seulement hr
- d) seulement meta
**Réponse :** a
**Explication :** Lien + icône.

### 20.
html-5.png dans icones/ s’affiche avec :
- a) img src="icones/html-5.png"
- b) audio src
- c) iframe youtube
- d) ol type=A
**Réponse :** a
**Explication :** Méthode 1.

## Exercices pratiques (20)

### 1.
**Consigne :** img icône 48×48.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<img src="icones/html.png" alt="HTML" width="48" height="48">
```

**Indice :** width height

### 2.
**Consigne :** Script Akar dans head.

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

### 3.
**Consigne :** i facebook bleu 46px.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<i class="ai-facebook-fill" style="color: blue; font-size: 46px;"></i>
```

**Indice :** class + style

### 4.
**Consigne :** Icône dans un lien.

**Code de départ :**
```html
<i class="ai-facebook-fill"></i>
```

**Correction :**
```html
<a href="https://www.facebook.com"><i class="ai-facebook-fill"></i></a>
```

**Indice :** a enveloppe.

### 5.
**Consigne :** img cliquable W3Schools.

**Code de départ :**
```html
<img src="icones/html.png" alt="HTML">
```

**Correction :**
```html
<a href="https://www.w3schools.com"><img src="icones/html.png" alt="HTML" width="24" height="24"></a>
```

**Indice :** a + img

### 6.
**Consigne :** Passe 64px en font-size.

**Code de départ :**
```html
<i class="ai-instagram-fill" style="width:64px"></i>
```

**Correction :**
```html
<i class="ai-instagram-fill" style="font-size:64px; color:#e1306c;"></i>
```

**Indice :** font-size + color

### 7.
**Consigne :** Trois icônes sociales.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<i class="ai-facebook-fill" style="color:#1877f2;font-size:40px;"></i>
<i class="ai-instagram-fill" style="color:#e1306c;font-size:40px;"></i>
<i class="ai-whatsapp-fill" style="color:#25d366;font-size:40px;"></i>
```

**Indice :** 3 i

### 8.
**Consigne :** alt sur icône image.

**Code de départ :**
```html
<img src="icones/html-5.png" width="64" height="64">
```

**Correction :**
```html
<img src="icones/html-5.png" alt="HTML 5" width="64" height="64">
```

**Indice :** alt

### 9.
**Consigne :** title sur img icône.

**Code de départ :**
```html
<img src="icones/html.png" alt="HTML">
```

**Correction :**
```html
<img src="icones/html.png" alt="HTML" title="Logo HTML">
```

**Indice :** title

### 10.
**Consigne :** Réduis l’image à 20px.

**Code de départ :**
```html
<img src="icones/html.png" alt="HTML" width="100" height="100">
```

**Correction :**
```html
<img src="icones/html.png" alt="HTML" width="20" height="20">
```

**Indice :** 20

### 11.
**Consigne :** WhatsApp lien.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<a href="https://www.whatsapp.com"><i class="ai-whatsapp-fill" style="color:#25d366;font-size:36px;"></i></a>
```

**Indice :** a+i

### 12.
**Consigne :** Deux méthodes côte à côte.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<img src="icones/html.png" alt="PNG" width="40" height="40">
<i class="ai-facebook-fill" style="font-size:40px;color:blue;"></i>
```

**Indice :** img + i

### 13.
**Consigne :** style color purple.

**Code de départ :**
```html
<i class="ai-facebook-fill"></i>
```

**Correction :**
```html
<i class="ai-facebook-fill" style="color:purple; font-size:32px;"></i>
```

**Indice :** color

### 14.
**Consigne :** Icônes dans ul.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<ul>
<li><i class="ai-facebook-fill"></i> Facebook</li>
<li><i class="ai-instagram-fill"></i> Instagram</li>
</ul>
```

**Indice :** li + i

### 15.
**Consigne :** Corrige width sur i.

**Code de départ :**
```html
<i class="ai-facebook-fill" width="46"></i>
```

**Correction :**
```html
<i class="ai-facebook-fill" style="font-size:46px;"></i>
```

**Indice :** font-size

### 16.
**Consigne :** Chemin icones/html-5.png.

**Code de départ :**
```html
<img alt="HTML5">
```

**Correction :**
```html
<img src="icones/html-5.png" alt="HTML5" width="48" height="48">
```

**Indice :** src

### 17.
**Consigne :** script + i ensemble.

**Code de départ :**
```html
<html><head></head><body></body></html>
```

**Correction :**
```html
<html><head>
<script src="https://unpkg.com/akar-icons-fonts"></script>
</head>
<body>
<i class="ai-facebook-fill" style="font-size:40px;color:blue;"></i>
</body></html>
```

**Indice :** head script, body i.

### 18.
**Consigne :** Accessibilité : alt descriptif.

**Code de départ :**
```html
<img src="icones/html.png">
```

**Correction :**
```html
<img src="icones/html.png" alt="Logo du langage HTML">
```

**Indice :** alt clair.

### 19.
**Consigne :** Instagram 28px rose.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<i class="ai-instagram-fill" style="color:#e1306c; font-size:28px;"></i>
```

**Indice :** font-size 28

### 20.
**Consigne :** Rangée vendeur : 2 liens icônes.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>
<a href="https://www.facebook.com"><i class="ai-facebook-fill" style="color:#1877f2;font-size:28px;"></i></a>
<a href="https://www.instagram.com"><i class="ai-instagram-fill" style="color:#e1306c;font-size:28px;"></i></a>
</p>
```

**Indice :** exemple réel du cours.
