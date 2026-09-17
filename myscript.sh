#!/usr/bin/env bash
set -euo pipefail

# Cree un seul dossier chapitre-N dans le repertoire courant.
# Le numero est le plus petit entier libre (les trous sont rebouches).

n=1
while [ -d "chapitre-${n}" ]; do
  n=$((n + 1))
done

folder="chapitre-${n}"
mkdir "${folder}"

cat > "${folder}/index.html" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
</head>
<body>
   
</body>
</html>
EOF



: > "${folder}/chap${n}_notes.md"

echo "Dossier cree : ${folder}/"
echo "  - index.html"


echo "  - chap${n}_notes.md"
