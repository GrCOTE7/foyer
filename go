#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

PORT="${FOYER_PORT:-8000}"
HOST="${FOYER_HOST:-127.0.0.1}"
URL="http://localhost:${PORT}"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Erreur: python3 est requis mais introuvable." >&2
    exit 1
fi

if ! python3 -c "import mkdocs" >/dev/null 2>&1; then
    echo "Installation des dependances docs..."
    python3 -m pip install -r requirements-docs.txt
fi

echo "Serveur local en cours de lancement..."
echo "Ouvre ${URL}"
exec python3 -m mkdocs serve \
--dev-addr "${HOST}:${PORT}" \
--watch "README.md" \
--watch "Manifeste-Foyer.md" \
--watch "Methode-Foyer.md" \
--watch "Boucle-de-retroaction.md" \
--watch "Simulateur-Synthese.md" \
--watch "skills" \
--watch "personas" \
--watch "bmad" \
--watch "tools" \
--watch "notebooklm"
