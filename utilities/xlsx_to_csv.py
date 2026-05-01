#!/usr/bin/env python3
"""Export each tab of tropes_entities_types_keys.xlsx to a CSV in _data/.

Usage:
    python utilities/xlsx_to_csv.py
"""

import csv
from pathlib import Path

import openpyxl

SHEET_TO_FILE = {
    "Persons": "persons_entities.csv",
    "Places":  "places_entities.csv",
    "Groups":  "groups_entities.csv",
    "Orgs":    "orgs_entities.csv",
    "Ships":   "ships_entities.csv",
    "Tropes":  "tropes_key.csv",
}

repo_root = Path(__file__).parent.parent
src = repo_root / "_source_data" / "tropes_entities_types_keys.xlsx"
out_dir = repo_root / "_data"

wb = openpyxl.load_workbook(src, read_only=True, data_only=True)

for sheet_name, filename in SHEET_TO_FILE.items():
    ws = wb[sheet_name]
    out_path = out_dir / filename
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            writer.writerow(["" if v is None else v for v in row])
    print(f"Wrote {out_path.relative_to(repo_root)}")

wb.close()
