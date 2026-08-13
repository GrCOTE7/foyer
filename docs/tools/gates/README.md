# tools/gates/

Implémentation exécutable du skill **`skills/gates.md`**. Ce dossier
porte le *comment* ; le skill porte le *pourquoi* et où passe la ligne
enforcement/guidance — lisez-le en premier.

## Contenu

- `TOOLS.md` — comparatif d'outils par gate, justifié selon le veto
  lexicographique (altérité → réversibilité → érosion → coût), et
  annexe dédiée à la sélection de l'agrégateur.
- `gitlab/`, `github/workflows/` — templates par stack : Rust, Java,
  Python, Next.js/Astro/Svelte, PHP (Symfony/Drupal), PowerShell, C#,
  migrations PostgreSQL.
- `workstation/` — gates de poste (pre-commit), secrets uniquement en
  bloquant, le reste délégué aux hooks natifs de chaque écosystème.

## Statut

Templates génériques, pensés pour être copiés dans un projet consommateur
(KoproGo ou autre) et adaptés à ses stacks réels — pas pour tourner tels
quels sur ce dépôt de méthodologie.
