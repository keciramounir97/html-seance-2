# Chapitre 13 — Symboles et emojis

## Exercices théoriques (20)

### 1.
Pour coller 😀 il faut :
- a) meta charset UTF-8
- b) un ol
- c) un iframe
- d) controls
**Réponse :** a
**Explication :** Sinon caractères cassés.

### 2.
Une entity commence par :
- a) & et finit par ;
- b) < seulement
- c) //
- d) <!--
**Réponse :** a
**Explication :** &copy;

### 3.
&lt; affiche :
- a) <
- b) >
- c) &
- d) ©
**Réponse :** a
**Explication :** less than.

### 4.
&gt; affiche :
- a) >
- b) <
- c) €
- d) ♥
**Réponse :** a
**Explication :** greater than.

### 5.
&amp; affiche :
- a) &
- b) <
- c) ©
- d) ½
**Réponse :** a
**Explication :** Sinon & commence une entity.

### 6.
&nbsp; :
- a) espace insécable / forcé
- b) un saut de page PDF
- c) une video
- d) un header
**Réponse :** a
**Explication :** 250 000 DA sans coupure.

### 7.
&copy; :
- a) ©
- b) €
- c) <
- d) 😀
**Réponse :** a
**Explication :** Copyright.

### 8.
&euro; :
- a) €
- b) $
- c) ©
- d) →
**Réponse :** a
**Explication :** Euro.

### 9.
&#169; et &copy; :
- a) le même © (numéro vs nom)
- b) deux symboles opposés
- c) un ol et un ul
- d) audio et video
**Réponse :** a
**Explication :** Deux écritures.

### 10.
&#128512; :
- a) 😀
- b) ©
- c) <p>
- d) un iframe
**Réponse :** a
**Explication :** Code emoji.

### 11.
Pourquoi &lt;p&gt; ?
- a) afficher la balise comme texte, pas l’interpréter
- b) créer un vrai p
- c) lire un mp3
- d) ouvrir YouTube
**Réponse :** a
**Explication :** Caractères réservés.

### 12.
Plusieurs espaces HTML :
- a) deviennent un seul ; d’où &nbsp;
- b) sont toujours gardés
- c) créent des ol
- d) cassent charset
**Réponse :** a
**Explication :** Règle HTML.

### 13.
&quot; :
- a) "
- b) '
- c) <
- d) ©
**Réponse :** a
**Explication :** Guillemet.

### 14.
Coller 🇩🇿 direct :
- a) OK avec UTF-8
- b) interdit
- c) besoin de ol
- d) besoin de video
**Réponse :** a
**Explication :** Méthode simple.

### 15.
&times; :
- a) ×
- b) ÷
- c) €
- d) <
**Réponse :** a
**Explication :** Multiplication.

### 16.
&ge; :
- a) ≥
- b) ≤
- c) ≠
- d) ©
**Réponse :** a
**Explication :** Plus grand ou égal.

### 17.
Le numéro marche :
- a) même si le nom d’entity n’existe pas (emojis)
- b) seulement pour ol
- c) seulement sans UTF-8
- d) jamais
**Réponse :** a
**Explication :** &#128512;

### 18.
&hearts; :
- a) ♥
- b) ©
- c) →
- d) <
**Réponse :** a
**Explication :** Cœur.

### 19.
Sans ; à la fin de &copy :
- a) l’entity peut échouer
- b) c’est mieux
- c) ça crée un iframe
- d) ça lit un mp4
**Réponse :** a
**Explication :** Toujours &...;

### 20.
Les plus utilisés en cours :
- a) &copy; &euro; &amp; &lt; &gt; &nbsp;
- b) seulement ol li
- c) seulement source type
- d) seulement target blank
**Réponse :** a
**Explication :** À retenir.

## Exercices pratiques (20)

### 1.
**Consigne :** Emoji collé.

**Code de départ :**
```html
<p>bonjour</p>
```

**Correction :**
```html
<p>bonjour 😀</p>
```

**Indice :** coller

### 2.
**Consigne :** Code 128512.

**Code de départ :**
```html
<p></p>
```

**Correction :**
```html
<p>&#128512;</p>
```

**Indice :** &#

### 3.
**Consigne :** Copyright nom.

**Code de départ :**
```html
<p>2026 Aboni</p>
```

**Correction :**
```html
<p>&copy; 2026 Aboni</p>
```

**Indice :** &copy;

### 4.
**Consigne :** Euro.

**Code de départ :**
```html
<p>2500</p>
```

**Correction :**
```html
<p>2500 &euro;</p>
```

**Indice :** &euro;

### 5.
**Consigne :** Afficher <p></p> comme texte.

**Code de départ :**
```html
<p>l'element p s'ecrit p</p>
```

**Correction :**
```html
<p>l'element p s'ecrit &lt;p&gt;&lt;/p&gt;</p>
```

**Indice :** lt gt

### 6.
**Consigne :** &amp; pour &.

**Code de départ :**
```html
<p>HTML CSS</p>
```

**Correction :**
```html
<p>HTML &amp; CSS</p>
```

**Indice :** amp

### 7.
**Consigne :** nbsp dans le prix.

**Code de départ :**
```html
<p>85 000 DA</p>
```

**Correction :**
```html
<p>85&nbsp;000&nbsp;DA</p>
```

**Indice :** nbsp

### 8.
**Consigne :** © par numéro.

**Code de départ :**
```html
<p></p>
```

**Correction :**
```html
<p>&#169;</p>
```

**Indice :** 169

### 9.
**Consigne :** Algérie emoji.

**Code de départ :**
```html
<p>Alger</p>
```

**Correction :**
```html
<p>Alger 🇩🇿</p>
```

**Indice :** UTF-8

### 10.
**Consigne :** ≥ 9/10.

**Code de départ :**
```html
<p>Note 9/10</p>
```

**Correction :**
```html
<p>Note &ge; 9/10</p>
```

**Indice :** ge

### 11.
**Consigne :** m² entity ou sup.

**Code de départ :**
```html
<p>85 m2</p>
```

**Correction :**
```html
<p>85 m&sup2;</p>
```

**Indice :** sup2

### 12.
**Consigne :** flèche droite.

**Code de départ :**
```html
<p>Voir annonce</p>
```

**Correction :**
```html
<p>Voir annonce &rarr;</p>
```

**Indice :** rarr

### 13.
**Consigne :** cœur.

**Code de départ :**
```html
<p>Favori</p>
```

**Correction :**
```html
<p>Favori &hearts;</p>
```

**Indice :** hearts

### 14.
**Consigne :** guillemets entity.

**Code de départ :**
```html
<p>ok</p>
```

**Correction :**
```html
<p>&quot;ok&quot;</p>
```

**Indice :** quot

### 15.
**Consigne :** demi ½.

**Code de départ :**
```html
<p>1/2</p>
```

**Correction :**
```html
<p>&frac12;</p>
```

**Indice :** frac12

### 16.
**Consigne :** pied d’annonce complet.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>Prix : 85&nbsp;000 DA</p>
<p>&copy; 2026 Aboni — Alger 🇩🇿</p>
```

**Indice :** nbsp copy emoji

### 17.
**Consigne :** tableau 2 entities.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>&copy; = &#169;</p>
<p>&euro;</p>
```

**Indice :** nom + numéro

### 18.
**Consigne :** Corrige < brut dans le texte.

**Code de départ :**
```html
<p>balise <p></p>
```

**Correction :**
```html
<p>balise &lt;p&gt;</p>
```

**Indice :** lt

### 19.
**Consigne :** times multiplication.

**Code de départ :**
```html
<p>3 x 4</p>
```

**Correction :**
```html
<p>3 &times; 4</p>
```

**Indice :** times

### 20.
**Consigne :** Phrase cours : UTF-8 + entity + emoji.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>bonjour 😀 — l'élément s'écrit &lt;p&gt; — &copy; 2026</p>
```

**Indice :** tout le chapitre.
