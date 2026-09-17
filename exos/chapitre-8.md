# Chapitre 8 — Conteneurs sémantiques et non sémantiques

## Exercices théoriques (20)

### 1.
Un conteneur :
- a) regroupe d’autres éléments dans un cadre
- b) est forcément une video
- c) remplace UTF-8
- d) est un fichier MP3
**Réponse :** a
**Explication :** Carte Ouedkniss = une boîte.

### 2.
Non sémantique veut dire :
- a) le nom ne dit pas le métier (div, span)
- b) interdit en HTML
- c) uniquement YouTube
- d) uniquement ol
**Réponse :** a
**Explication :** Générique.

### 3.
Sémantique veut dire :
- a) le nom donne le job (header, article…)
- b) plus de CSS possible
- c) élément vide
- d) commentaire
**Réponse :** a
**Explication :** HTML5.

### 4.
div est :
- a) bloc générique
- b) un titre h1
- c) un type audio
- d) un iframe YouTube
**Réponse :** a
**Explication :** Non sémantique.

### 5.
span est :
- a) en ligne, générique
- b) un footer
- c) un ol
- d) un source
**Réponse :** a
**Explication :** Dans la phrase.

### 6.
header :
- a) en-tête (logo, titre, parfois menu)
- b) pied de page
- c) une video
- d) un charset
**Réponse :** a
**Explication :** Haut de page.

### 7.
nav :
- a) navigation / menu
- b) audio
- c) emoji
- d) favicon seulement
**Réponse :** a
**Explication :** Liens de menu.

### 8.
main :
- a) contenu principal, un seul par page
- b) autant que de div
- c) dans head
- d) un élément vide
**Réponse :** a
**Explication :** Un main.

### 9.
article :
- a) contenu indépendant (une annonce)
- b) uniquement un journal papier
- c) un br
- d) un mp3
**Réponse :** a
**Explication :** Carte d’annonce.

### 10.
section :
- a) partie thématique
- b) un saut de ligne
- c) un type video
- d) un commentaire
**Réponse :** a
**Explication :** Ex. « Téléphones ».

### 11.
aside :
- a) contenu à côté (pub, secondaire)
- b) le h1 obligatoire
- c) un ol type A
- d) meta charset
**Réponse :** a
**Explication :** Barre latérale.

### 12.
footer :
- a) pied de page
- b) en-tête
- c) un source
- d) un mark
**Réponse :** a
**Explication :** Copyright, contact.

### 13.
Pourquoi pas que des div ?
- a) SEO / accessibilité / clarté : le moteur aime le sens
- b) div est interdit
- c) div casse UTF-8
- d) div ne peut pas contenir img
**Réponse :** a
**Explication :** Mixte sémantique + div.

### 14.
La carte Ouedkniss est plutôt un :
- a) article (ou div si juste le CSS)
- b) title d’onglet
- c) source mp3
- d) DOCTYPE
**Réponse :** a
**Explication :** Contenu indépendant.

### 15.
figure + figcaption :
- a) image + légende
- b) audio + video
- c) head + body
- d) ul + ol
**Réponse :** a
**Explication :** Légende liée à l’image.

### 16.
details / summary :
- a) bloc repliable « voir plus »
- b) un iframe YouTube
- c) un charset
- d) un favicon
**Réponse :** a
**Explication :** Interactif natif.

### 17.
html / head / body sont :
- a) conteneurs racine (page / config / visible)
- b) des listes
- c) des videos
- d) des emojis
**Réponse :** a
**Explication :** Structure globale.

### 18.
span vs div :
- a) span en ligne, div bloc
- b) identiques
- c) span va dans head
- d) div est vide comme br
**Réponse :** a
**Explication :** Choix selon le flux.

### 19.
On mélange sémantique et div quand :
- a) la zone a un nom (sémantique) ou c’est juste du CSS (div)
- b) jamais
- c) seulement sans charset
- d) seulement dans ol
**Réponse :** a
**Explication :** Règle du chapitre 8.

### 20.
Plusieurs articles vont dans :
- a) souvent une section
- b) un unique h1 chacun dans head
- c) un source
- d) un target _blank
**Réponse :** a
**Explication :** Section « Téléphones ».

## Exercices pratiques (20)

### 1.
**Consigne :** header avec h1.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<header><h1>Ouedkniss</h1></header>
```

**Indice :** header

### 2.
**Consigne :** nav de 2 liens.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<nav><a href="#">Accueil</a> <a href="#">Annonces</a></nav>
```

**Indice :** nav

### 3.
**Consigne :** footer copyright.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<footer><p>© 2026 Mini Ouedkniss</p></footer>
```

**Indice :** footer

### 4.
**Consigne :** article annonce.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<article>
<h3>iPhone 13</h3>
<p>Alger — 85000 DA</p>
</article>
```

**Indice :** article

### 5.
**Consigne :** section + 2 articles.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<section>
<h2>Téléphones</h2>
<article><h3>iPhone</h3></article>
<article><h3>Galaxy</h3></article>
</section>
```

**Indice :** section enveloppe.

### 6.
**Consigne :** aside pub.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<aside><p>Publicité</p></aside>
```

**Indice :** aside

### 7.
**Consigne :** main autour du contenu.

**Code de départ :**
```html
<h2>Annonces</h2>
```

**Correction :**
```html
<main>
<h2>Annonces</h2>
</main>
```

**Indice :** un main.

### 8.
**Consigne :** div carte générique.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<div>
<img src="v.png" alt="voiture">
<h2>Peugeot 208</h2>
<p>Prix : <span>1850000 DA</span></p>
</div>
```

**Indice :** div + span

### 9.
**Consigne :** Remplace div menu par nav.

**Code de départ :**
```html
<div><a href="#">Accueil</a></div>
```

**Correction :**
```html
<nav><a href="#">Accueil</a></nav>
```

**Indice :** sémantique.

### 10.
**Consigne :** Remplace div pied par footer.

**Code de départ :**
```html
<div>© 2026</div>
```

**Correction :**
```html
<footer>© 2026</footer>
```

**Indice :** footer

### 11.
**Consigne :** figure légende.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<figure>
<img src="v.png" alt="208">
<figcaption>Peugeot 208 — Alger</figcaption>
</figure>
```

**Indice :** figcaption dans figure.

### 12.
**Consigne :** details voir plus.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<details>
<summary>Voir plus</summary>
<p>Première main.</p>
</details>
```

**Indice :** summary

### 13.
**Consigne :** span sur le prix.

**Code de départ :**
```html
<p>Prix : 85000 DA</p>
```

**Correction :**
```html
<p>Prix : <span>85000 DA</span></p>
```

**Indice :** span

### 14.
**Consigne :** header + nav ensemble.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<header>
<h1>Ouedkniss</h1>
<nav><a href="#">Annonces</a></nav>
</header>
```

**Indice :** nav dans header OK.

### 15.
**Consigne :** Page squelette sémantique.

**Code de départ :**
```html
<body></body>
```

**Correction :**
```html
<body>
<header><h1>Site</h1></header>
<main><article><h2>Annonce</h2></article></main>
<footer>© 2026</footer>
</body>
```

**Indice :** 3 zones.

### 16.
**Consigne :** aside à côté de section (ordre HTML).

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<main>
<section><h2>Annonces</h2></section>
<aside>Pub</aside>
</main>
```

**Indice :** main contient les deux.

### 17.
**Consigne :** Ne pas mettre 2 main.

**Code de départ :**
```html
<main>A</main>
<main>B</main>
```

**Correction :**
```html
<main>
<section>A</section>
<section>B</section>
</main>
```

**Indice :** un main, plusieurs section.

### 18.
**Consigne :** Carte : article pas div (sémantique).

**Code de départ :**
```html
<div><h3>iPhone 13</h3><p>Alger</p></div>
```

**Correction :**
```html
<article><h3>iPhone 13</h3><p>Alger</p></article>
```

**Indice :** article

### 19.
**Consigne :** address contact.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<address>Karim — Hydra — 0550</address>
```

**Indice :** address

### 20.
**Consigne :** Mini Ouedkniss complet.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<header><h1>Ouedkniss</h1><nav><a href="#">Accueil</a></nav></header>
<main>
<section>
<article><h3>iPhone 13</h3><p>Alger</p></article>
</section>
<aside>Publicité</aside>
</main>
<footer>© 2026</footer>
```

**Indice :** toutes les zones.
