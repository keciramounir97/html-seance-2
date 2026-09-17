# Révision — Séance précédente

Cette fiche reprend **tout ce qui précède les listes** : texte, mise en forme, commentaires, éléments vides, onglet / favicon, attributs, liens et images.

## 1. Squelette d’une page

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Titre de l’onglet</title>
  <link rel="shortcut icon" href="icones/html.png" type="image/png">
</head>
<body>
  <!-- contenu visible -->
</body>
</html>
```

- `head` = configuration (invisible, sauf onglet).
- `body` = ce que le visiteur voit.

## 2. Texte (chapitre 1)

- `h1` … `h6` : titres (un seul `h1` par page).
- `p` : paragraphe.
- `div` : boîte en **bloc**.
- `span` : bout de texte **en ligne**.

## 3. Mise en forme (chapitre 2)

`b` gras, `i` italique, `u` souligné, `mark` surligné, `sub` indice, `sup` exposant.

```html
<p>Appartement <b>F3</b> — 85 m<sup>2</sup> à <i>Hydra</i>.</p>
```

## 4. Commentaires et vides (chapitre 3)

```html
<!-- note invisible -->
<br>   <!-- saut de ligne -->
<hr>   <!-- trait -->
<img src="photo.jpg" alt="description">  <!-- pas de balise fermante -->
```

## 5. Onglet (chapitre 4)

- `title` → texte de l’onglet.
- `link rel="shortcut icon"` → icône (Flaticon → dossier `icones/` → `href`).

## 6. Attributs, liens, images (chapitre 5)

Attribut = `nom="valeur"` **dans la balise ouvrante**.

```html
<p title="Infobulle">Survole-moi</p>
<a href="https://www.google.com" target="_blank">Google</a>
<img src="images/photo.png" alt="Annonce à Alger" width="300">
```

- `a` + `href` = lien.
- `target="_blank"` = nouvel onglet.
- `img` + `src` + `alt` = image.

## Mini page complète (révision)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Fiche Peugeot 208 | Alger</title>
</head>
<body>
  <!-- Annonce -->
  <h1>Peugeot 208</h1>
  <p>Année <b>2020</b> — <mark>65 000 km</mark> — Alger.</p>
  <p>Prix : 250 000 DA — 3<sup>e</sup> main.</p>
  <hr>
  <p>
    <a href="https://www.google.com" target="_blank">Voir sur Google</a>
  </p>
  <img src="images/voiture.png" alt="Peugeot 208 blanche">
</body>
</html>
```

## Suite du cours (cette séance)

1. Listes (`ul`, `ol`, `dl`)
2. Icônes (image vs Akar)
3. Conteneurs sémantiques / non sémantiques
4. Vidéo, audio, iframe
5. Head complet
6. Symboles et emojis
