# Chapitre 10 — L’audio

## Objectif

Intégrer un son (musique, voix, podcast) avec `<audio>`. C’est **la même logique** que la vidéo (chapitre 9), sans image.

## Syntaxe simple (un seul fichier)

```html
<audio src="audio/audio.mp3" controls></audio>
```

`controls` affiche play / pause / volume / barre de progression.

`width` et `height` ne s’appliquent **pas vraiment** à `audio` (ce n’est pas une image). La barre a une taille par défaut.

## Plusieurs formats (`source`)

Comme pour la vidéo : si un format n’est pas lu, le navigateur **passe au suivant**.

```html
<audio controls>
  <source src="audio/audio.mp3" type="audio/mpeg">
  <source src="audio/audio.ogg" type="audio/ogg">
  <source src="audio/audio.wav" type="audio/wav">
  Ton navigateur ne lit pas l’audio HTML5.
</audio>
```

| Format | `type` |
|---|---|
| `.mp3` | `audio/mpeg` (parfois écrit `audio/mp3`) |
| `.ogg` | `audio/ogg` |
| `.wav` | `audio/wav` |

Le plus compatible : **MP3**.

## Attributs utiles

| Attribut | Rôle |
|---|---|
| `controls` | boutons de lecture |
| `autoplay` | démarre tout seul (souvent bloqué) |
| `muted` | muet |
| `loop` | en boucle |
| `preload` | `auto`, `metadata`, `none` |

```html
<audio controls loop>
  <source src="audio/audio.mp3" type="audio/mpeg">
</audio>
```

## Exemple réel : message du vendeur

```html
<h2>Écoutez la description de l’annonce</h2>
<audio src="audio/audio.mp3" controls>
  Votre navigateur ne prend pas en charge l’audio.
</audio>
```

## Vidéo vs audio

| | `video` | `audio` |
|---|---|---|
| Fichier | mp4, webm, ogg | mp3, ogg, wav |
| Image | oui | non |
| `source` | oui | oui |
| `controls` | oui | oui |
| `poster` | oui | non |

## À retenir

- `<audio src="..." controls>` = cas simple.
- Plusieurs formats = plusieurs `<source>` dans `<audio>`.
- Si un format n’est pas supporté, le navigateur **saute** vers l’autre.
- Toujours `controls` pour que l’utilisateur puisse lancer le son.
