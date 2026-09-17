# Chapitre 7 — Les icônes

## Objectif

Ajouter des icônes dans une page HTML de **deux façons** : image (`img`) ou police d’icônes (élément `i` + bibliothèque).

## Méthode 1 — Icône image (`img`)

L’icône est un **fichier PNG/SVG**. On l’affiche comme n’importe quelle image.

### Étapes (Flaticon)

1. Aller sur [flaticon.com](https://www.flaticon.com)
2. Se connecter
3. Rechercher l’icône
4. La personnaliser (couleur, taille)
5. Télécharger
6. La placer dans `icones/`
7. L’intégrer avec `img`

```html
<img src="icones/html.png" alt="Logo HTML" width="48" height="48">
```

On peut la mettre **dans un lien** (icône cliquable) :

```html
<a href="https://www.w3schools.com">
  <img src="icones/html.png" alt="W3Schools" width="24" height="24">
</a>
```

Taille = `width` et `height` (comme une photo).

## Méthode 2 — Bibliothèque d’icônes (ex. Akar Icons)

Une bibliothèque JS transforme un `<i>` (à l’origine : italique) en **icône**.

Ce n’est **plus traité comme une image** : c’est traité comme **du texte**.

Donc :

- couleur → `color` (comme le texte)
- taille → `font-size` (pas `width` / `height`)

### Étapes (Akar Icons)

1. Aller sur [akaricons.com](https://akaricons.com)
2. Cliquer sur **Get started**
3. Descendre jusqu’à l’exemple GitHub
4. Copier **seulement** la balise `<script ...>` dans le `<head>`
5. Revenir au site, choisir une icône
6. Copier le snippet HTML/CSS (`<i class="ai-..."></i>`)
7. Le coller dans le `<body>`

```html
<head>
  <script src="https://unpkg.com/akar-icons-fonts"></script>
</head>
<body>
  <i class="ai-facebook-fill" style="color: blue; font-size: 46px;"></i>

  <a href="https://www.facebook.com">
    <i class="ai-facebook-fill" style="color: blue; font-size: 46px;"></i>
  </a>
</body>
```

## Comparaison

| | Image `img` | Police (`i` + librairie) |
|---|---|---|
| Fichier | PNG/SVG local | aucun fichier image |
| Taille | `width` / `height` | `font-size` |
| Couleur | figée dans le PNG (sauf SVG) | `color` |
| Lien Internet | non (une fois téléchargée) | oui (script dans `head`) |

## Exemple réel : réseaux d’un vendeur

```html
<p>
  <a href="https://www.facebook.com"><i class="ai-facebook-fill" style="color:#1877f2; font-size:28px;"></i></a>
  <a href="https://www.instagram.com"><i class="ai-instagram-fill" style="color:#e1306c; font-size:28px;"></i></a>
</p>
```

## À retenir

- 2 familles : **image** ou **police d’icônes**.
- Image → `img` + `width`/`height`.
- Akar → `<script>` dans `head` + `<i class="ai-...">` + `font-size` et `color`.
