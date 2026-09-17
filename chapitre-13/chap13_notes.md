# Chapitre 13 — Symboles HTML et emojis

## Objectif

Afficher correctement les **emojis**, les **accents**, et les **symboles** (`©`, `€`, `<`, `&`…).

## Condition : UTF-8 (chapitre 12)

```html
<meta charset="UTF-8">
```

Sans cette ligne, `é`, `€`, `😀` et `🇩🇿` peuvent s’afficher en `Ã©` ou en `?`.

## 1) Les emojis

On peut **coller** l’emoji directement (grâce à UTF-8) :

```html
<p>bonjour 😀 ❤️ 🇩🇿</p>
```

On peut aussi utiliser un **code numérique** :

```html
<p>&#128512;</p>
```

😀 = `&#128512;`

Le code est utile si le clavier n’a pas l’emoji, ou pour être sûr du caractère.

## 2) Les entités HTML (symbols)

Certains caractères sont **réservés** : le navigateur les croit être du **code**, pas du texte.

| Caractère | Problème |
|---|---|
| `<` | ouvre une balise |
| `>` | ferme une balise |
| `&` | commence une entité |
| `"` et `'` | entourent les attributs |

On les écrit avec des **entities** : ça commence par `&` et ça finit par `;`.

| Entity | Affiche |
|---|---|
| `&lt;` | `<` |
| `&gt;` | `>` |
| `&amp;` | `&` |
| `&quot;` | `"` |
| `&apos;` | `'` |

```html
<p>L’élément p s’écrit &lt;p&gt;&lt;/p&gt;</p>
```

À l’écran : `L’élément p s’écrit <p></p>`

## 3) L’espace insécable `&nbsp;`

En HTML, plusieurs espaces d’affilée = **un seul** espace.

`&nbsp;` = *non-breaking space* = espace **forcé**, et le mot **ne passe pas à la ligne** à cet endroit.

```html
<p>250&nbsp;000&nbsp;DA</p>
```

## 4) Symboles utiles

| Entity | Symbole | Entity | Symbole |
|---|---|---|---|
| `&copy;` | © | `&reg;` | ® |
| `&trade;` | ™ | `&euro;` | € |
| `&pound;` | £ | `&yen;` | ¥ |
| `&dollar;` | $ | `&deg;` | ° |
| `&plusmn;` | ± | `&times;` | × |
| `&divide;` | ÷ | `&ne;` | ≠ |
| `&le;` | ≤ | `&ge;` | ≥ |
| `&frac12;` | ½ | `&frac14;` | ¼ |
| `&frac34;` | ¾ | `&larr;` | ← |
| `&rarr;` | → | `&uarr;` | ↑ |
| `&darr;` | ↓ | `&hearts;` | ♥ |

```html
<p>Prix : 2500 &euro;</p>
<p>&copy; 2026 Aboni</p>
```

## 5) Deux façons d’écrire un symbole

Par **nom** :

```html
&copy;
```

Par **numéro** :

```html
&#169;
```

Les deux donnent ©.

- Le nom est plus facile à retenir.
- Le numéro marche **toujours**, même si le nom n’existe pas (surtout pour les emojis).

## Exemple réel : pied d’annonce

```html
<p>Prix : 85&nbsp;000 &euro; (environ 85 000 DA affichés en euro pour l’exemple)</p>
<p>Note &ge; 9/10 — surface 85 m&sup2;</p>
<p>&copy; 2026 Aboni — Alger 🇩🇿</p>
<p>Code HTML : &lt;article&gt; ... &lt;/article&gt;</p>
```

(`&sup2;` = ², comme `<sup>2</sup>`)

## À retenir

- UTF-8 dans le `head` pour emojis, accents, `$`, `€`.
- Coller l’emoji direct = OK.
- `& < > " '` → entities si on veut les **afficher** comme texte.
- `&nbsp;` = espace forcé.
- Les plus utilisés : `&copy;`, `&euro;`, `&amp;`, `&lt;`, `&gt;`.
