#!/usr/bin/env python3
"""Génère docs/gates-templates.md à partir des templates de tools/gates/.

Idempotent : relancé à chaque build, la page reflète exactement l'état du
dossier — ajouter un template dans tools/gates/<plateforme>/ suffit à le
publier, sans rien éditer à la main.

Pourquoi une page générée plutôt qu'une copie du dossier : les templates
portent le suffixe `.example` (pour qu'aucun runner ne les découvre comme de
la CI active), et MkDocs ne rend pas un `.yml.example` comme une page. Sans
ce générateur, ils seraient publiés en fichiers statiques — téléchargeables,
mais illisibles en ligne.

Chaque template est rendu dans un bloc repliable `???` (pymdownx.details, déjà
activé dans mkdocs.yml) : la page reste parcourable malgré ~2000 lignes de YAML.
"""
from pathlib import Path

SRC = Path("tools/gates")
OUT = Path("docs/gates-templates.md")

# Une entrée par plateforme. `glob` est relatif à SRC ; `lang` fixe la
# coloration du bloc de code.
PLATFORMS = [
    {
        "dir": "github/workflows",
        "label": "GitHub Actions",
        "glob": "*.yml.example",
        "lang": "yaml",
        "desc": (
            "Un workflow par stack. Les workflows `gate-secrets` et "
            "`gate-container` sont appelés par les autres via `workflow_call` — "
            "les copier tous les deux, quelle que soit la stack."
        ),
    },
    {
        "dir": "gitlab",
        "label": "GitLab CI",
        "glob": ".gitlab-ci.*.yml.example",
        "lang": "yaml",
        "desc": (
            "`.gitlab-ci.gates.yml` porte les gates communs et les variables de "
            "version ; il s'inclut avec le fichier de la stack. "
            "`.gitlab-ci.root.yml` montre le `.gitlab-ci.yml` racine résultant."
        ),
    },
    {
        "dir": "workstation",
        "label": "Poste de travail",
        "glob": ".pre-commit-config.yaml.example",
        "lang": "yaml",
        "desc": (
            "Seul le gate secrets est bloquant au commit (rapide, hors ligne). "
            "Le reste est délégué aux hooks natifs de chaque écosystème — voir "
            "`install.sh` dans le dépôt."
        ),
    },
]

HEADER = """# Templates de gates

Implémentation exécutable du skill [Gates qualité & sécurité](skills/gates.md).
Le skill porte le *pourquoi* et où passe la ligne plancher/jalon ;
[la liste consolidée des outils](tools/gates/ADR-outillage.md) porte le *quoi* et
son verdict de veto ; cette page porte le *comment*.

!!! warning "Des exemples, pas un livrable"
    Ces fichiers sont **des templates dont on s'inspire**, à réinstancier selon
    les stacks réelles du projet — pas à copier tels quels. Ils ne tournent pas
    sur ce dépôt : le suffixe `.example` garantit qu'aucun runner ne les
    découvre comme de la CI active.

    Les actions sont épinglées par SHA et les images par version à la date de
    rédaction. **Les revérifier avant reprise** — un SHA épinglé se périme, et
    sa mise à jour relève du cercle de réexamen de l'ADR.
"""


def main() -> None:
    lines = [HEADER]
    rendered_any = False

    for platform in PLATFORMS:
        folder = SRC / platform["dir"]
        if not folder.is_dir():
            continue
        templates = sorted(folder.glob(platform["glob"]))
        if not templates:
            continue

        rendered_any = True
        lines += ["", f"## {platform['label']}", "", platform["desc"], ""]

        for template in templates:
            # Nom affiché sans le suffixe : c'est celui que le fichier portera
            # une fois copié dans le dépôt consommateur.
            shown = template.name.removesuffix(".example")
            body = template.read_text(encoding="utf-8").rstrip("\n")
            indented = "\n".join(
                f"    {line}" if line.strip() else "" for line in body.splitlines()
            )
            lines += [
                f'??? example "{shown}"',
                "",
                f"    ```{platform['lang']}",
                indented,
                "    ```",
                "",
            ]

    if not rendered_any:
        lines += ["", "*Aucun template trouvé dans `tools/gates/`.*"]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Généré {OUT}")


if __name__ == "__main__":
    main()
