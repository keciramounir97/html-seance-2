# Chapitre 11 — Iframe

## Objectif

Afficher **une autre page** (ou une vidéo YouTube) **dans un cadre** de ta page, sans quitter ton site.

## Qu’est-ce qu’un `iframe` ?

`iframe` = *inline frame* = **fenêtre dans la fenêtre**.

Le contenu vient d’ailleurs : un autre fichier HTML, un site, une carte, une vidéo YouTube.

```html
<iframe src="../chapitre-10/index.html" width="500" height="400"></iframe>
```

`src` = l’adresse à afficher dans le cadre.

## Attributs utiles

| Attribut | Rôle |
|---|---|
| `src` | URL ou fichier à charger |
| `width` / `height` | taille du cadre |
| `title` | description (accessibilité) |
| `allowfullscreen` | plein écran (YouTube) |
| `loading="lazy"` | charger seulement si on défile jusqu’au cadre |

`frameborder="0"` ou `1` est **ancien**. En HTML5 on préfère le CSS (`border`).

## Exemple 1 — un autre chapitre du cours

```html
<h2>Aperçu du lecteur audio (chapitre 10)</h2>
<iframe
  src="../chapitre-10/index.html"
  title="Page audio du chapitre 10"
  width="500"
  height="280">
</iframe>
```

## Exemple 2 — vidéo YouTube

YouTube donne un code à copier (Partager → Intégrer). C’est un `iframe`, **pas** un `<video>`.

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/U2-JPqrALsA"
  title="Lecteur vidéo YouTube"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen>
</iframe>
```

L’URL importante est `/embed/ID_DE_LA_VIDEO`, pas l’URL `watch?v=` du navigateur.

## Quand l’utiliser ?

- Vidéo YouTube / Vimeo
- Carte Google Maps
- Aperçu d’une autre page
- Formulaire externe, pub, widget

## Limites

- Tous les sites **n’autorisent pas** d’être mis dans un iframe (sécurité).
- Trop d’iframes = page plus lente.
- Le contenu de l’iframe est une **page séparée** : ton CSS ne le stylise pas de l’intérieur.

## À retenir

- `iframe` = cadre qui charge une **page externe** ou un fichier.
- YouTube = `iframe` avec `src="https://www.youtube.com/embed/..."`.
- Fichier local = `src="chemin/vers/page.html"`.
- `video` = fichier à toi (mp4). `iframe` = lecteur YouTube (ou autre site).
