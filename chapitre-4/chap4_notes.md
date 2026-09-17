# Chapitre 4 — Titre de l’onglet et favicon

## Objectif

Configurer **ce qui se voit dans l’onglet** du navigateur : le titre et la petite icône.

Ces deux choses se placent dans `<head>` (la zone de **configuration**, pas le contenu visible de la page).

## 1) L’élément `title`

```html
<title>Annonces voitures Alger | Aboni</title>
```

- C’est le texte de **l’onglet**.
- C’est aussi le titre proposé quand on **enregistre** la page dans les favoris.
- Google l’utilise comme titre du résultat de recherche.

Sans `title`, l’onglet affiche souvent `Document` ou le nom du fichier.

## 2) Le favicon

Le favicon est la **petite icône** à gauche du titre dans l’onglet.

Snippet VS Code : `link:favicon`

```html
<link rel="shortcut icon" href="icones/html.png" type="image/x-icon">
```

| Attribut | Rôle |
|---|---|
| `rel` | dit que c’est l’icône du site |
| `href` | **chemin** vers le fichier image |
| `type` | type du fichier (`image/x-icon`, `image/png`…) |

### Étapes (Flaticon)

1. Aller sur [flaticon.com](https://www.flaticon.com)
2. Se connecter
3. Chercher une icône (ex. `html`, `car`, `home`)
4. La personnaliser si besoin
5. Télécharger (PNG)
6. La placer dans un dossier `icones/`
7. Mettre le chemin dans `href`

```html
<link rel="shortcut icon" href="icones/html.png" type="image/png">
```

## Exemple réel de `head` minimal

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ouedkniss — Annonces Alger</title>
  <link rel="shortcut icon" href="icones/html.png" type="image/png">
</head>
<body>
  <h1>Bienvenue</h1>
</body>
</html>
```

Le `h1` s’affiche **dans la page**. Le `title` s’affiche **dans l’onglet**. Ce n’est pas la même chose.

## À retenir

- `title` → texte de l’onglet.
- `link rel="shortcut icon"` → icône de l’onglet.
- Tout ça va dans `<head>`, jamais dans `<body>`.
