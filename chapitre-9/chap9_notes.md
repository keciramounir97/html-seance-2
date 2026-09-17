# Chapitre 9 — La vidéo

## Objectif

Intégrer une vidéo dans la page avec `<video>`, avec un ou plusieurs formats.

## Syntaxe simple (un seul fichier)

```html
<video src="videos/video.mp4" controls width="500" height="280"></video>
```

`src` = chemin du fichier.  
`controls` = afficher play / pause / volume / plein écran.

Sans `controls`, la vidéo est là mais **le visiteur n’a pas de boutons**.

## Plusieurs formats (`source`)

Tous les navigateurs ne lisent pas les mêmes formats. On donne **plusieurs fichiers**. Le navigateur prend **le premier qu’il sait lire**, et saute les autres.

```html
<video controls width="500">
  <source src="videos/video.mp4"  type="video/mp4">
  <source src="videos/video.webm" type="video/webm">
  <source src="videos/video.ogg"  type="video/ogg">
  Ton navigateur ne lit pas la vidéo HTML5.
</video>
```

On ajoute autant de `<source>` que de formats. Le texte à la fin s’affiche **seulement** si rien n’est supporté.

| Format | `type` |
|---|---|
| `.mp4` | `video/mp4` |
| `.webm` | `video/webm` |
| `.ogg` / `.ogv` | `video/ogg` |

Le plus sûr aujourd’hui : **MP4**.

## Attributs utiles

| Attribut | Rôle |
|---|---|
| `controls` | barre de lecture |
| `width` / `height` | taille |
| `autoplay` | démarre toute seule (souvent bloqué sans `muted`) |
| `muted` | sans son |
| `loop` | recommence en boucle |
| `poster` | image affichée **avant** la lecture |
| `preload` | `auto`, `metadata` ou `none` |

```html
<video controls muted loop poster="images/apercu.jpg" width="500">
  <source src="videos/video.mp4" type="video/mp4">
</video>
```

## Exemple réel : visite d’un appartement

```html
<h2>Visite virtuelle — F3 Hydra</h2>
<video src="videos/video.mp4" controls width="640" height="360">
  Désolé, votre navigateur ne peut pas lire cette vidéo.
</video>
```

Pour une vidéo **YouTube**, on n’utilise pas `<video>` : on utilise un **`iframe`** (chapitre 11).

## À retenir

- `<video src="..." controls>` = cas simple.
- Plusieurs formats = plusieurs `<source>` dans `<video>`.
- Si un format n’est pas supporté, le navigateur **saute** au suivant.
- `controls` est presque toujours nécessaire.
