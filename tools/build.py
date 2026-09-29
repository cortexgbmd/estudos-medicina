#!/usr/bin/env python3
"""Regenera index.html a partir de data/materials.json + tools/template.html.
Uso: python3 tools/build.py   (rodar na raiz do repo)
"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
raw = (root / "data" / "materials.json").read_text(encoding="utf-8").strip()
mats = json.loads(raw)  # valida o JSON
tpl = (root / "tools" / "template.html").read_text(encoding="utf-8")
assert tpl.count("__MATERIALS_JSON__") == 1, "template sem placeholder unico"
(root / "index.html").write_text(tpl.replace("__MATERIALS_JSON__", raw), encoding="utf-8")
print(f"index.html regenerado com {len(mats)} materiais")
