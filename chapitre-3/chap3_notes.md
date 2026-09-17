# Chapitre 3 — Commentaires et éléments vides

## Objectif

Comprendre :
1. comment laisser une note dans le code (invisible sur la page) ;
2. ce qu’est un **élément vide** (pas de balise fermante).

## 1) Les commentaires

Un commentaire s’écrit :

```html
<!-- Ceci est un commentaire. Le visiteur ne le voit pas. -->
```

### À quoi ça sert ?

- Expliquer une zone du code.
- Désactiver un bout de HTML sans l’effacer.
- Se repérer dans une longue page (`<!-- MENU -->`, `<!-- PIED DE PAGE -->`).

```html
<!-- Carte de l'annonce Peugeot 208 -->
<div>
  <h2>Peugeot 208</h2>
</div>
```

Le navigateur **ignore** le commentaire. Il n’apparaît pas dans la page.

## 2) Les éléments vides (void elements)

Certains éléments **n’ont pas de contenu** et **pas de balise fermante**.

Les plus utilisés au début :

| Élément | Rôle |
|---|---|
| `<br>` | saut de **ligne** (comme Entrée) |
| `<hr>` | ligne horizontale (séparateur) |
| `<img>` | image (le contenu est le fichier, via `src`) |
| `<meta>` | information dans le `head` |
| `<link>` | lien vers CSS ou favicon |
| `<input>` | champ de formulaire |
| `<source>` | fichier vidéo / audio |

```html
<p>Ligne 1<br>Ligne 2</p>
<hr>
<img src="voiture.jpg" alt="Peugeot 208 à Alger">
```

## Différence `br` vs `p`

- `p` = un **paragraphe** (bloc, avec marge).
- `br` = juste **aller à la ligne** dans le même paragraphe.

On n’empile pas 10 `<br>` pour “faire de l’espace” : plus tard, le CSS s’en charge.

## Exemple réel

```html
<h1>Contact vendeur</h1>
<p>
  Karim B.<br>
  Hydra, Alger<br>
  0550 12 34 56
</p>
<hr>
<p>Annonce n°20481</p>
```

## À retenir

- `<!-- commentaire -->` = note invisible.
- Élément vide = **une seule balise**, pas de `</br>` ni de `</img>`.
- `br` = saut de ligne, `hr` = trait, `img` = image.
