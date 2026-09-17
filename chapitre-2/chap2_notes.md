# Chapitre 2 — La mise en forme du texte

## Objectif

Mettre un mot en **gras**, *italique*, souligné, surligné, ou en indice / exposant, **sans** CSS.

## Les éléments de mise en forme

| Balise | Rôle visuel | Exemple d’usage |
|---|---|---|
| `<b>` | gras | un mot important |
| `<strong>` | gras + importance | une alerte, un prix |
| `<i>` | italique | un mot étranger, un nom |
| `<em>` | italique + emphase | insister sur un mot |
| `<u>` | souligné | un lien visuel (à éviter trop souvent) |
| `<mark>` | surligné | un résultat de recherche |
| `<sub>` | indice (en bas) | H<sub>2</sub>O |
| `<sup>` | exposant (en haut) | 250 m<sup>2</sup>, x<sup>2</sup> |

## Exemples réels

```html
<p>Appartement <b>F3</b> à <i>Bab Ezzouar</i>.</p>
<p>Prix : <strong>1 850 000 DA</strong></p>
<p>Surface : 85 m<sup>2</sup> — 3<sup>e</sup> étage</p>
<p>Formule chimique de l’eau : H<sub>2</sub>O</p>
<p>Le mot <mark>Alger</mark> apparaît dans l’annonce.</p>
```

## Différence importante

- `b` / `i` → surtout **l’apparence**.
- `strong` / `em` → l’apparence **et** le sens (lecteur d’écran, SEO).

Pour un cours débutant : `b`, `i`, `u`, `mark`, `sub`, `sup` suffisent. Plus tard on préfère `strong` et `em`.

## On les met **dans** un paragraphe

Ces balises ne remplacent pas `p`. Elles s’utilisent **à l’intérieur** du texte :

```html
<p>Ceci est <b>important</b> et ceci est <i>en italique</i>.</p>
```

## À retenir

- Mise en forme = balise **autour du mot**.
- `sub` = en bas (H2O), `sup` = en haut (m²).
- `mark` = surlignage jaune par défaut.
