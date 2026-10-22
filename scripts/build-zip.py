#!/usr/bin/env python3
"""Construit le zip du Business Starter à téléverser dans Pilora (Admin > Business Starter).

Usage : python3 scripts/build-zip.py
Prend les fichiers suivis par git (copie de travail), retire ceux qui ne doivent pas
être livrés, et écrit dist/pilora-starter-<version>.zip.
"""
import json, subprocess, zipfile, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# Pilora est déjà branché au niveau de l'agent (connecteur claude.ai ou réglages Codex) :
# les fichiers de connexion par projet feraient apparaître le serveur en double.
EXCLURE = {".mcp.json", ".codex/config.toml"}
EXCLURE_DOSSIERS = ("scripts/", "dist/")

version = json.loads((ROOT / "pilora-starter.json").read_text(encoding="utf-8"))["version"]
fichiers = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
fichiers += ["pilora-starter.json"]  # au cas où il n'est pas encore commité
fichiers = sorted({f for f in fichiers if f and f not in EXCLURE and not f.startswith(EXCLURE_DOSSIERS) and (ROOT / f).is_file()})

sortie = ROOT / "dist" / f"pilora-starter-{version}.zip"
sortie.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(sortie, "w", zipfile.ZIP_DEFLATED) as z:
    for f in fichiers:
        z.write(ROOT / f, f)
print(f"{sortie} : {len(fichiers)} fichiers, {sortie.stat().st_size // 1024} Ko")
if any(f in EXCLURE for f in fichiers):
    sys.exit("erreur : fichier de connexion inclus")
