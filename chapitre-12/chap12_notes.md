# Chapitre 12 — HTML Head

## Objectif

Comprendre que `<head>` est la **configuration** de la page : invisible pour le visiteur, indispensable pour le navigateur, Google, le téléphone, les icônes, le CSS et le JS.

Le contenu visible va dans `<body>`. Les réglages vont dans `<head>`.

## Structure

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <!-- configuration ici -->
</head>
<body>
  <!-- ce que l’on voit ici -->
</body>
</html>
```

## 1) Encodage : `charset`

```html
<meta charset="UTF-8">
```

Sans cette ligne, le navigateur peut **casser** :

- les accents : é è à ç
- les symboles : € $ ©
- les emojis : 😀 🇩🇿

Toujours la **première** (ou parmi les premières) lignes du `head`.

## 2) Viewport (téléphone / PC)

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Ça dit au téléphone : “prends **la largeur de l’écran** comme largeur de page”.

- Téléphone → version étroite.
- PC → version large.

Sans viewport, le téléphone affiche souvent la page **comme un mini-PC** (tout petit, il faut zoomer).

## 3) `title` (chapitre 4)

```html
<title>Cours HTML — Chapitre 12 | Aboni</title>
```

Texte de **l’onglet**.

## 4) Favicon (chapitre 4)

```html
<link rel="shortcut icon" href="icones/html.png" type="image/png">
```

Petite icône de l’onglet.

## 5) Bibliothèques (chapitre 7)

Exemple Akar Icons : un `<script>` dans le `head` pour transformer `<i>` en icône.

```html
<script src="https://unpkg.com/akar-icons-fonts"></script>
```

## 6) CSS et JavaScript

```html
<!-- CSS interne -->
<style>
  body { font-family: sans-serif; }
</style>

<!-- CSS externe -->
<link rel="stylesheet" href="style.css">

<!-- JS externe -->
<script src="app.js"></script>
```

Le JS peut aussi se mettre **juste avant** `</body>` (souvent mieux pour la vitesse).

## 7) Autres `meta` utiles

```html
<meta name="description" content="Cours HTML en français : listes, vidéo, iframe.">
<meta name="author" content="Aboni">
```

La description peut apparaître sous le titre **dans Google**.

## Exemple réel de `head` complet

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Mini site d'annonces à Alger.">
  <title>Annonces Alger | Aboni</title>
  <link rel="shortcut icon" href="icones/html.png" type="image/png">
  <link rel="stylesheet" href="style.css">
  <script src="https://unpkg.com/akar-icons-fonts"></script>
</head>
```

## Visible vs invisible

| Dans `head` | On le voit ? |
|---|---|
| `title` | onglet seulement |
| favicon | onglet seulement |
| `charset`, viewport | non (effet technique) |
| CSS | on voit **le résultat** sur le body |
| script d’icônes | on voit les icônes dans le body |

## À retenir

- `head` = configuration ; `body` = page visible.
- `charset="UTF-8"` → accents, €, emojis.
- `viewport` → téléphone et PC reçoivent la bonne largeur.
- On y met aussi : `title`, favicon, CSS, JS, librairies d’icônes.
