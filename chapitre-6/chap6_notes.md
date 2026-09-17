# Chapitre 6 — Les listes

## Objectif

Afficher des informations **comme une liste** (à puces, numérotée, ou glossaire). Ce n’est pas une “base de données” : c’est seulement une **présentation visuelle**, comme les boutons liste à puces / liste numérotée de Word.

## Les 3 types

| Type | Élément | Contenu | Rendu par défaut |
|---|---|---|---|
| Liste **non ordonnée** | `ul` | `li` | puces (•) |
| Liste **ordonnée** | `ol` | `li` | 1. 2. 3. |
| Liste de **descriptions** | `dl` | `dt` + `dd` | terme + définition |

## 1) `ul` — unordered list

Quand **l’ordre n’est pas important** : menu, réseaux sociaux, wilayas, avantages d’un produit.

```html
<ul>
  <li>Alger</li>
  <li>Oran</li>
  <li>Constantine</li>
</ul>
```

## 2) `ol` — ordered list

Quand **l’ordre compte** : étapes d’une recette, classement, tutoriel.

```html
<ol>
  <li>Aller sur Flaticon</li>
  <li>Télécharger l’icône</li>
  <li>L’insérer avec img</li>
</ol>
```

## 3) `li` — list item

Chaque ligne d’un `ul` ou d’un `ol` est un `li`.  
Un `li` peut contenir du texte, un lien, une image, même un `div`.

```html
<ul>
  <li><a href="https://www.google.com">Google</a></li>
  <li><a href="https://www.facebook.com">Facebook</a></li>
</ul>
```

## 4) `dl` — description list

Pour un **mot + sa définition** (glossaire, fiche produit).

- `dt` = *description term* = le mot
- `dd` = *description* = l’explication

Pas de `li` ici.

```html
<dl>
  <dt>HTML</dt>
  <dd>Langage qui structure une page web.</dd>
  <dt>CSS</dt>
  <dd>Langage qui habille (style) la page.</dd>
  <dt>JavaScript</dt>
  <dd>Langage qui rend la page interactive.</dd>
</dl>
```

## Exemple réel : page d’annonce

```html
<h2>Samsung Galaxy A54</h2>
<ul>
  <li>128 Go</li>
  <li>Couleur noir</li>
  <li>État 9/10</li>
</ul>

<h3>Étapes pour acheter</h3>
<ol>
  <li>Contacter le vendeur</li>
  <li>Voir le téléphone</li>
  <li>Payer et récupérer</li>
</ol>

<h3>Vocabulaire</h3>
<dl>
  <dt>État 9/10</dt>
  <dd>Très bon état, micro-rayures possibles.</dd>
  <dt>Première main</dt>
  <dd>Un seul propriétaire depuis l’achat.</dd>
</dl>
```

## À retenir

- `ul` + `li` → puces.
- `ol` + `li` → numéros.
- `dl` + `dt` + `dd` → mot et définition.
- L’ordre des `li` dans un `ol` **compte**. Dans un `ul`, non.
