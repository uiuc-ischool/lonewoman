#!/usr/bin/env python3
"""Export each tab of tropes_entities_types_keys.xlsx to a CSV in _data/.

Usage:
    python utilities/xlsx_to_csv.py
"""

import csv
from pathlib import Path

import openpyxl

ENTITY_HEADERS = ["person_writing", "type", "key", "name", "write_up", "notes"]

# (output filename, clean headers, number of original header rows to skip)
SHEET_CONFIG = {
    "Persons": ("persons_entities.csv", ENTITY_HEADERS,                                        2),
    "Places":  ("places_entities.csv",  ENTITY_HEADERS + ["latitude", "longitude"],            2),
    "Groups":  ("groups_entities.csv",  ENTITY_HEADERS,                                        2),
    "Orgs":    ("orgs_entities.csv",    ENTITY_HEADERS,                                        2),
    "Ships":   ("ships_entities.csv",   ENTITY_HEADERS,                                        2),
    "Tropes":  ("tropes_key.csv",       ["type", "title"],                                     1),
}

repo_root = Path(__file__).parent.parent
src = repo_root / "_source_data" / "tropes_entities_types_keys.xlsx"
out_dir = repo_root / "_data"

wb = openpyxl.load_workbook(src, read_only=True, data_only=True)

for sheet_name, (filename, headers, skip_rows) in SHEET_CONFIG.items():
    ws = wb[sheet_name]
    out_path = out_dir / filename
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if i < skip_rows:
                continue
            writer.writerow(["" if v is None else v for v in row])
    print(f"Wrote {out_path.relative_to(repo_root)}")

wb.close()
