# HTML — Séance 2 (Aboni)

Cours HTML pour les étudiants : **notes**, **exemples ouvrables**, **exercices**, et un **site de documentation** (style W3Schools, FR / EN / AR).

## Site (Vercel + GitHub Pages)

Le fichier principal est **`index.html` à la racine** (obligatoire pour Vercel).

Après le déploiement :

- documentation interactive : `/` (`index.html`)
- exemple d’un chapitre : `/chapitre-6/index.html`
- exercices markdown : `/exos/`

### Vercel

1. Import the GitHub repo `html-seance-2`
2. Framework preset : **Other**
3. Root directory : `.` (leave empty)
4. Output : the repo itself (`index.html` is already at the root)

### GitHub Pages

The workflow `.github/workflows/pages.yml` publishes the repo.

Public URL (once Pages is enabled):

`https://keciramounir97.github.io/html-seance-2/`

The original `chapitre-9/videos/video.mp4` is **too large for GitHub/Vercel** (247 MB, limit 100 MB). It stays on your computer only (gitignored). The hosted demo uses the light file `cours.mp4`.

## Comment ouvrir le cours (étudiants)

1. Clone :

```bash
git clone git@github.com:keciramounir97/html-seance-2.git
cd html-seance-2
```

2. Ouvre **`index.html`** dans le navigateur (documentation).
3. Ou ouvre un chapitre directement, par exemple `chapitre-8/index.html`.

| Dossier | Contenu |
|---|---|
| `index.html` + `css/` + `js/` | Site de documentation |
| `chapitre-1` … `chapitre-13` | Notes `.md` + exemple `index.html` |
| `exos/` | 20 QCM + 20 pratiques par chapitre |
| `revision_notes.md` | Révision séance précédente |

## Chapitres

1. Éléments de texte  
2. Mise en forme  
3. Commentaires et éléments vides  
4. Titre d’onglet et favicon  
5. Attributs, liens, images  
6. Listes  
7. Icônes  
8. Conteneurs sémantiques / non sémantiques  
9. Vidéo  
10. Audio  
11. Iframe  
12. HTML Head  
13. Symboles et emojis  
