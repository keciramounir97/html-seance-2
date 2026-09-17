# Chapitre 8 — Conteneurs sémantiques et non sémantiques

## Objectif

Comprendre ce qu’est un **conteneur**, puis choisir entre un cadre **générique** (`div`, `span`) et un cadre **sémantique** (`header`, `article`, `footer`…).

## Qu’est-ce qu’un conteneur ?

Un élément conteneur **regroupe plusieurs éléments** dans un même cadre.

Exemple réel : une **carte d’annonce Ouedkniss**. Dans le même carré on trouve :

- une image
- un titre
- deux icônes
- un prix
- une ville

Tout ça vit dans **une seule boîte**. Cette boîte est un conteneur.

## 1) Conteneurs non sémantiques (génériques)

Ils n’ont **aucun métier** dans leur nom. Ils servent à grouper, souvent pour le CSS.

| Élément | Type | Rôle |
|---|---|---|
| `div` | bloc | grande boîte (carte, ligne, colonne) |
| `span` | en ligne | petite boîte dans une phrase |

```html
<div>
  <img src="voiture.jpg" alt="Peugeot 208">
  <h2>Peugeot 208</h2>
  <p>Prix : <span>250 000 DA</span></p>
</div>
```

`div` peut remplacer visuellement `header`, `footer`, `article`… Mais le navigateur et Google **ne savent pas** ce que c’est.

## 2) Conteneurs sémantiques (HTML5)

Même travail qu’un `div` (ils **contiennent**), mais **le nom dit le métier**.

| Élément | Métier |
|---|---|
| `header` | en-tête (logo, titre, parfois menu) |
| `nav` | menu de navigation |
| `main` | contenu principal (**un seul** par page) |
| `section` | partie thématique (“Annonces”, “À propos”) |
| `article` | contenu indépendant (une annonce, un article) |
| `aside` | contenu à côté (pub, infos secondaires) |
| `footer` | pied de page (copyright, contact) |

**Sémantique** = l’élément **annonce son job** par son nom.  
**Non sémantique** = élément générique (`div`) qui peut tout remplacer.

## Pourquoi ne pas tout mettre dans des `div` ?

Parce que :

- Google / le SEO aiment une structure claire (`article`, `nav`, `main`).
- Les lecteurs d’écran naviguent plus facilement.
- Le code se lit mieux pour un humain (`<footer>` est plus clair que `<div>` n°27).

On utilise un **mixte** : sémantique dès qu’on peut nommer la zone, `div` pour le reste (mise en page CSS).

## Exemple réel : mini Ouedkniss

```html
<body>
  <header>
    <h1>Ouedkniss</h1>
    <nav>
      <ul>
        <li><a href="#">Accueil</a></li>
        <li><a href="#">Annonces</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section>
      <h2>Téléphones</h2>
      <article>
        <img src="phone.jpg" alt="iPhone 13">
        <h3>iPhone 13</h3>
        <p>Alger — 85 000 DA</p>
      </article>
    </section>
    <aside>
      <p>Publicité</p>
    </aside>
  </main>

  <footer>
    <p>© 2026 Ouedkniss</p>
  </footer>
</body>
```

La carte d’annonce = un **`article`**. Un `div` afficherait la même chose, mais `article` **explique** que c’est un contenu indépendant.

## Autres conteneurs utiles

| Élément | Rôle |
|---|---|
| `figure` + `figcaption` | image + légende |
| `blockquote` | citation longue |
| `address` | coordonnées |
| `details` + `summary` | bloc repliable “voir plus” |
| `ul` / `ol` / `dl` | listes (chapitre 6) |
| `form` / `fieldset` | formulaires |
| `html` / `head` / `body` | racine, config, page visible |

```html
<figure>
  <img src="voiture.jpg" alt="Peugeot 208">
  <figcaption>Peugeot 208 — Alger, 2020</figcaption>
</figure>

<details>
  <summary>Voir plus</summary>
  <p>Première main, carnet d’entretien complet.</p>
</details>
```

## Règle de choix

1. Tu peux dire *ce que c’est* (menu, pied de page, une annonce) → **sémantique**.
2. C’est juste un cadre pour le style → **`div`** (ou `span` dans le texte).

## À retenir

- Conteneur = boîte qui contient d’autres éléments.
- Non sémantique : `div`, `span`.
- Sémantique : `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.
- On mélange les deux : diversité + clarté pour le moteur de recherche.
