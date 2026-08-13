#!/usr/bin/env bash
# Installe les gates de poste de travail dans le dépôt courant.
# Prérequis : Python (pour pipx/pre-commit) et Git.
set -euo pipefail

if ! command -v pre-commit >/dev/null 2>&1; then
  echo "Installation de pre-commit..."
  if command -v pipx >/dev/null 2>&1; then
    pipx install pre-commit
  else
    pip install --user pre-commit
  fi
fi

# Copie la config si le dépôt n'en a pas déjà une (ne jamais écraser une
# config existante sans confirmation).
if [ -f .pre-commit-config.yaml ]; then
  echo "Un .pre-commit-config.yaml existe déjà dans ce dépôt — non modifié."
  echo "Comparer manuellement avec $(dirname "$0")/.pre-commit-config.yaml.example"
else
  cp "$(dirname "$0")/.pre-commit-config.yaml.example" .pre-commit-config.yaml
  echo "Config copiée."
fi

pre-commit install
pre-commit install --hook-type pre-push

echo ""
echo "Gates de poste installés. Test :"
pre-commit run --all-files || true

echo ""
echo "Pour le sweep secrets vérifié (TruffleHog), voir le job planifié"
echo "en CI — il n'est volontairement pas installé sur le poste (appels"
echo "réseau, plus lent, pertinent en balayage périodique seulement)."
