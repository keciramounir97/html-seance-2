# Chapitre 1 — Les éléments de texte

## Objectif

Savoir afficher du texte dans une page HTML : titres, paragraphes, et petits / grands cadres (`span` / `div`).

## Idée simple

HTML ne “dessine” pas le design. Il **donne un rôle** à chaque morceau de texte. Le navigateur affiche ensuite ce rôle avec une taille et une mise en page par défaut.

## Les titres : `h1` à `h6`

- `h1` : le titre **principal** de la page (en général **un seul** par page).
- `h2` : un sous-titre important (section).
- `h3` à `h6` : des titres de plus en plus petits (sous-sections).

Plus le numéro est grand, plus le titre est petit.

```html
<h1>Ouedkniss</h1>
<h2>Téléphones à Alger</h2>
<h3>iPhone 13 — 85 000 DA</h3>
```

## Le paragraphe : `p`

`p` contient un **bloc de texte**. Le navigateur ajoute un espace avant et après.

```html
<p>iPhone 13 128 Go, état 9/10, vendu à Alger Centre. Livraison possible.</p>
```

## `div` et `span` (première rencontre)

Ce ne sont pas des titres. Ce sont des **cadres** :

| Élément | Comportement | Usage |
|---|---|---|
| `div` | bloc (prend la largeur, va à la ligne) | regrouper une carte, une zone |
| `span` | en ligne (reste dans la phrase) | colorer un mot, un prix, une ville |

```html
<div>
  <h2>Peugeot 208</h2>
  <p>Ville : <span>Alger</span> — Prix : <span>250 000 DA</span></p>
</div>
```

## Exemple réel

Une petite fiche d’annonce :

```html
<h1>Annonces Algérie</h1>
<h2>Voitures</h2>
<div>
  <h3>Peugeot 208 2020</h3>
  <p>Boîte automatique, 65 000 km, première main.</p>
  <p>Contact : 0550 00 00 00 — <span>Hydra, Alger</span></p>
</div>
```

## À retenir

- `h1` → titre de la page.
- `p` → texte normal.
- `div` → boîte (bloc).
- `span` → bout de texte (en ligne).
- On n’utilise pas `h1` dix fois pour “faire gros” : on choisit le bon niveau.
