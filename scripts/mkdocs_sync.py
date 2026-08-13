from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / ".build" / "docs"

DOCS_SOURCE_FILES = {
    "docs/index.md": "index.md",
    "docs/.pages": ".pages",
}

ROOT_FILES = [
    "Manifeste-Foyer.md",
    "Methode-Foyer.md",
    "Boucle-de-retroaction.md",
    "Simulateur-Synthese.md",
]

RENAMED_FILES = {
    "README.md": "carte.md",
}

DIRS_TO_SYNC = [
    # "assets",
    "skills",
    "personas",
    "bmad",
    "tools",
    "notebooklm",
]


def _needs_copy(src: Path, dst: Path) -> bool:
    if not dst.exists():
        return True
    src_stat = src.stat()
    dst_stat = dst.stat()
    return (
        src_stat.st_mtime_ns > dst_stat.st_mtime_ns
        or src_stat.st_size != dst_stat.st_size
    )


def _sync_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if _needs_copy(src, dst):
        shutil.copy2(src, dst)


def _sync_dir(src_dir: Path, dst_dir: Path) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src_path in src_dir.rglob("*"):
        rel = src_path.relative_to(src_dir)
        dst_path = dst_dir / rel
        if src_path.is_dir():
            dst_path.mkdir(parents=True, exist_ok=True)
            continue
        _sync_file(src_path, dst_path)


def sync_docs_content() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)

    DOCS.mkdir(parents=True, exist_ok=True)

    for src_name, dst_name in DOCS_SOURCE_FILES.items():
        src = ROOT / src_name
        dst = DOCS / dst_name
        _sync_file(src, dst)

    for filename in ROOT_FILES:
        src = ROOT / filename
        dst = DOCS / filename
        _sync_file(src, dst)

    for src_name, dst_name in RENAMED_FILES.items():
        src = ROOT / src_name
        dst = DOCS / dst_name
        _sync_file(src, dst)

    for dirname in DIRS_TO_SYNC:
        src_dir = ROOT / dirname
        dst_dir = DOCS / dirname
        _sync_dir(src_dir, dst_dir)


def generate_docs_pages() -> None:
    env = os.environ.copy()
    env["FOYER_DOCS_DIR"] = str(DOCS)

    subprocess.run(
        [sys.executable, "scripts/gen_supports.py"], cwd=ROOT, env=env, check=True
    )
    subprocess.run(
        [sys.executable, "scripts/gen_gates.py"], cwd=ROOT, env=env, check=True
    )


def on_pre_build(config, **kwargs):
    """Synchronise les sources vers .build/docs avant chaque build/reload MkDocs."""
    sync_docs_content()
    generate_docs_pages()
    return config
