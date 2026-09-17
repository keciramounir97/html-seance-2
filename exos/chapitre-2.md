# Chapitre 2 — Mise en forme

## Exercices théoriques (20)

### 1.
Quelle balise met en gras ?
- a) i
- b) b
- c) u
- d) p
**Réponse :** b
**Explication :** b (ou strong).

### 2.
i affiche le texte :
- a) souligné
- b) en italique
- c) surligné
- d) en exposant
**Réponse :** b
**Explication :** i = italic.

### 3.
mark sert à :
- a) surligner
- b) une vidéo
- c) un lien
- d) un saut de ligne
**Réponse :** a
**Explication :** Surlignage jaune par défaut.

### 4.
sub place le texte :
- a) en haut
- b) en bas (indice)
- c) au centre
- d) caché
**Réponse :** b
**Explication :** H2O → H<sub>2</sub>O.

### 5.
sup place le texte :
- a) en exposant
- b) en indice
- c) en bloc
- d) dans head
**Réponse :** a
**Explication :** m², 3e étage.

### 6.
u sert à :
- a) souligner
- b) une liste
- c) un iframe
- d) UTF-8
**Réponse :** a
**Explication :** underline.

### 7.
Ces balises de forme se mettent :
- a) à la place de html
- b) à l’intérieur d’un p
- c) seulement dans head
- d) sans balise ouvrante
**Réponse :** b
**Explication :** On entoure un mot dans le paragraphe.

### 8.
strong est proche de :
- a) b (gras + importance)
- b) img
- c) br
- d) ol
**Réponse :** a
**Explication :** strong a aussi un sens d’importance.

### 9.
em est proche de :
- a) i (emphase)
- b) hr
- c) table
- d) source
**Réponse :** a
**Explication :** em = emphase.

### 10.
Pour 85 m² on utilise :
- a) sub
- b) sup
- c) ul
- d) audio
**Réponse :** b
**Explication :** exposant 2.

### 11.
Pour H2O on utilise :
- a) sup
- b) sub
- c) mark
- d) u
**Réponse :** b
**Explication :** indice 2.

### 12.
On peut combiner :
- a) b et i autour du même mot
- b) deux DOCTYPE
- c) head dans p
- d) body dans title
**Réponse :** a
**Explication :** <b><i>texte</i></b> est valide.

### 13.
Quelle balise n’est PAS de mise en forme de mot ?
- a) b
- b) video
- c) mark
- d) u
**Réponse :** b
**Explication :** video = média.

### 14.
Le surlignage d’un résultat de recherche ressemble à :
- a) mark
- b) hr
- c) iframe
- d) meta
**Réponse :** a
**Explication :** mark.

### 15.
i à l’origine signifie :
- a) image
- b) italic
- c) iframe
- d) icon only
**Réponse :** b
**Explication :** italic — plus tard réutilisé pour les icônes.

### 16.
On évite trop de u parce que :
- a) ça ressemble à un lien
- b) ça casse UTF-8
- c) c’est interdit
- d) ça crée un iframe
**Réponse :** a
**Explication :** Le soulignement évoque les liens.

### 17.
Pour insister sur un prix on peut :
- a) strong
- b) source
- c) nav
- d) charset
**Réponse :** a
**Explication :** strong = important.

### 18.
La mise en forme HTML de base se fait :
- a) sans CSS, avec des balises
- b) uniquement en Python
- c) dans le favicon
- d) avec audio
**Réponse :** a
**Explication :** b, i, u, mark, sub, sup.

### 19.
un <b> non fermé :
- a) peut casser l’affichage du texte suivant
- b) crée une vidéo
- c) est obligatoire
- d) remplace head
**Réponse :** a
**Explication :** Toujours fermer </b>.

### 20.
3e étage s’écrit bien :
- a) 3<sup>e</sup> étage
- b) 3<sub>e</sub> étage
- c) <video>3e</video>
- d) <ul>3e</ul>
**Réponse :** a
**Explication :** exposant e.

## Exercices pratiques (20)

### 1.
**Consigne :** Gras sur F3.

**Code de départ :**
```html
<p>Appartement F3</p>
```

**Correction :**
```html
<p>Appartement <b>F3</b></p>
```

**Indice :** b

### 2.
**Consigne :** Italique sur Hydra.

**Code de départ :**
```html
<p>à Hydra</p>
```

**Correction :**
```html
<p>à <i>Hydra</i></p>
```

**Indice :** i

### 3.
**Consigne :** Souligne Visite samedi.

**Code de départ :**
```html
<p>Visite samedi</p>
```

**Correction :**
```html
<p><u>Visite samedi</u></p>
```

**Indice :** u

### 4.
**Consigne :** Surligna Alger.

**Code de départ :**
```html
<p>Ville Alger</p>
```

**Correction :**
```html
<p>Ville <mark>Alger</mark></p>
```

**Indice :** mark

### 5.
**Consigne :** m2 en m².

**Code de départ :**
```html
<p>85 m2</p>
```

**Correction :**
```html
<p>85 m<sup>2</sup></p>
```

**Indice :** sup

### 6.
**Consigne :** H2O correct.

**Code de départ :**
```html
<p>H2O</p>
```

**Correction :**
```html
<p>H<sub>2</sub>O</p>
```

**Indice :** sub

### 7.
**Consigne :** Prix en strong.

**Code de départ :**
```html
<p>Prix : 85000 DA</p>
```

**Correction :**
```html
<p>Prix : <strong>85000 DA</strong></p>
```

**Indice :** strong

### 8.
**Consigne :** 3e avec sup.

**Code de départ :**
```html
<p>3e étage</p>
```

**Correction :**
```html
<p>3<sup>e</sup> étage</p>
```

**Indice :** sup autour de e.

### 9.
**Consigne :** b et i ensemble.

**Code de départ :**
```html
<p>urgent</p>
```

**Correction :**
```html
<p><b><i>urgent</i></b></p>
```

**Indice :** imbriquer.

### 10.
**Consigne :** em sur « vraiment ».

**Code de départ :**
```html
<p>C'est vraiment bien</p>
```

**Correction :**
```html
<p>C'est <em>vraiment</em> bien</p>
```

**Indice :** em

### 11.
**Consigne :** Formule CO2.

**Code de départ :**
```html
<p>CO2</p>
```

**Correction :**
```html
<p>CO<sub>2</sub></p>
```

**Indice :** sub

### 12.
**Consigne :** Surligna le mot iPhone.

**Code de départ :**
```html
<p>Annonce iPhone 13</p>
```

**Correction :**
```html
<p>Annonce <mark>iPhone</mark> 13</p>
```

**Indice :** mark

### 13.
**Consigne :** Gras sur l’état 9/10.

**Code de départ :**
```html
<p>État 9/10</p>
```

**Correction :**
```html
<p>État <b>9/10</b></p>
```

**Indice :** b

### 14.
**Consigne :** Italique nom de ville Oran.

**Code de départ :**
```html
<p>à Oran</p>
```

**Correction :**
```html
<p>à <i>Oran</i></p>
```

**Indice :** i

### 15.
**Consigne :** x2 en exposant.

**Code de départ :**
```html
<p>x2</p>
```

**Correction :**
```html
<p>x<sup>2</sup></p>
```

**Indice :** sup

### 16.
**Consigne :** Deux mises en forme : b et mark.

**Code de départ :**
```html
<p>Promo Alger</p>
```

**Correction :**
```html
<p><b>Promo</b> <mark>Alger</mark></p>
```

**Indice :** deux balises.

### 17.
**Consigne :** Souligner uniquement samedi.

**Code de départ :**
```html
<p>Visite samedi 10h</p>
```

**Correction :**
```html
<p>Visite <u>samedi</u> 10h</p>
```

**Indice :** u autour d’un mot.

### 18.
**Consigne :** strong + sup dans le même p.

**Code de départ :**
```html
<p>Prix 85000 DA - 85 m2</p>
```

**Correction :**
```html
<p>Prix <strong>85000 DA</strong> - 85 m<sup>2</sup></p>
```

**Indice :** strong et sup.

### 19.
**Consigne :** Phrase complète d’annonce formatée.

**Code de départ :**
```html
<!-- vide -->
```

**Correction :**
```html
<p>Appartement <b>F3</b> de 85 m<sup>2</sup> à <i>Hydra</i> — <mark>promo</mark>.</p>
```

**Indice :** combine b sup i mark.

### 20.
**Consigne :** Indice et exposant dans la même ligne.

**Code de départ :**
```html
<p>H2O et m2</p>
```

**Correction :**
```html
<p>H<sub>2</sub>O et m<sup>2</sup></p>
```

**Indice :** sub et sup.
