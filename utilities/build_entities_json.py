#!/usr/bin/env python3
"""Build _data/entities.json — a single lookup keyed by entity ID.

Usage:
    python utilities/build_entities_json.py

Sources: _data/{persons,places,groups,orgs,ships}_entities.csv
Output:  _data/entities.json
"""

import json
from pathlib import Path

import pandas as pd

repo_root = Path(__file__).parent.parent
data_dir  = repo_root / "_data"

SOURCES = [
    ("persons_entities.csv", "person"),
    ("places_entities.csv",  "place"),
    ("groups_entities.csv",  "group"),
    ("orgs_entities.csv",    "org"),
    ("ships_entities.csv",   "ship"),
]

entities = {}

for filename, entity_type in SOURCES:
    df = pd.read_csv(data_dir / filename, dtype=str).fillna("")
    df = df[df["key"].str.strip() != ""]

    for _, row in df.iterrows():
        entity_id = row["key"].strip().lstrip("#")
        entry = {
            "name":        row["name"].strip(),
            "description": row["write_up"].strip(),
            "type":        entity_type,
        }
        if entity_type == "place":
            for field, col in (("lat", "latitude"), ("lng", "longitude")):
                raw = row.get(col, "").strip().rstrip(",")
                if raw:
                    try:
                        entry[field] = float(raw)
                    except ValueError:
                        print(f"  Warning: bad {col} for {entity_id!r}: {raw!r} — skipped")

        entities[entity_id] = entry

    print(f"  {filename}: {len(df)} entries loaded")

out_path = data_dir / "entities.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(entities, f, ensure_ascii=False, indent=2)

print(f"\nWrote {out_path.relative_to(repo_root)}  ({len(entities)} total entries)")
