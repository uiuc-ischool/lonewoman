"""
Build _data/kepler_reprints.csv for Kepler.gl time + arc visualisation.

For each reprint group the "original" row supplies the arc origin coords;
every other row in the group gets those coords as origin_lat / origin_lng.
Geocoding is done via geopy Nominatim and cached in geocode_cache.json.
"""

import csv
import json
import time
from pathlib import Path

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

INPUT_CSV = Path("../_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv")
OUTPUT_CSV = Path("../_data/kepler_reprints.csv")
CACHE_FILE = Path("geocode_cache.json")

OUTPUT_COLS = [
    "article_id", "title", "publication", "date",
    "publisher_location", "lat", "lng",
    "origin_location", "origin_lat", "origin_lng",
    "reprint_type", "group_reprint_id", "author", "tropes",
]

# ---------------------------------------------------------------------------
# Load cache
# ---------------------------------------------------------------------------
if CACHE_FILE.exists():
    with open(CACHE_FILE) as f:
        cache: dict = json.load(f)
else:
    cache = {}


def save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


# ---------------------------------------------------------------------------
# Geocoder
# ---------------------------------------------------------------------------
geolocator = Nominatim(user_agent="lonewoman_kepler_prep/1.0")


def geocode(location: str) -> tuple[float | None, float | None]:
    if not location:
        return None, None
    if location in cache:
        entry = cache[location]
        return entry["lat"], entry["lng"]

    time.sleep(1.1)
    try:
        result = geolocator.geocode(location, timeout=10)
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"  [WARN] geocoder error for '{location}': {e}")
        cache[location] = {"lat": None, "lng": None}
        save_cache()
        return None, None

    if result:
        lat, lng = result.latitude, result.longitude
    else:
        lat, lng = None, None

    cache[location] = {"lat": lat, "lng": lng}
    save_cache()
    return lat, lng


# ---------------------------------------------------------------------------
# Load and filter CSV
# ---------------------------------------------------------------------------
with open(INPUT_CSV, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    all_rows = list(reader)

compound_rows = [r for r in all_rows if r["display_template"] == "compound_object"]
print(f"Loaded {len(all_rows)} total rows → {len(compound_rows)} compound_object rows")

# ---------------------------------------------------------------------------
# Map group_reprint_id → origin publisher_location
# ---------------------------------------------------------------------------
origin_by_group: dict[str, str] = {}
for row in compound_rows:
    if row["reprint_type"] == "original" and row["group_reprint_id"]:
        origin_by_group[row["group_reprint_id"]] = row["publisher_location"]

print(f"Found {len(origin_by_group)} reprint groups with an 'original' row")

# ---------------------------------------------------------------------------
# Collect all unique locations to geocode
# ---------------------------------------------------------------------------
all_locations: set[str] = set()
for row in compound_rows:
    if row["publisher_location"]:
        all_locations.add(row["publisher_location"])
all_locations.update(origin_by_group.values())

already_cached = sum(1 for loc in all_locations if loc in cache)
to_fetch = len(all_locations) - already_cached
print(f"\nUnique locations: {len(all_locations)}  "
      f"({already_cached} cached, {to_fetch} to fetch)")

if to_fetch:
    print("Geocoding new locations …")
    for i, loc in enumerate(sorted(all_locations - set(cache.keys())), 1):
        lat, lng = geocode(loc)
        status = f"{lat:.4f}, {lng:.4f}" if lat is not None else "NOT FOUND"
        print(f"  [{i}/{to_fetch}] {loc!r:40s} → {status}")
    print("Done geocoding.\n")

# ---------------------------------------------------------------------------
# Build output rows
# ---------------------------------------------------------------------------
out_rows = []
missing_locations: set[str] = set()
missing_origins: list[str] = []

for row in compound_rows:
    gid = row["group_reprint_id"]
    pub_loc = row["publisher_location"]

    lat, lng = geocode(pub_loc) if pub_loc else (None, None)
    if pub_loc and lat is None:
        missing_locations.add(pub_loc)

    origin_loc = origin_by_group.get(gid, "")
    orig_lat, orig_lng = geocode(origin_loc) if origin_loc else (None, None)
    if gid and not origin_loc:
        missing_origins.append(gid)

    out_rows.append({
        "article_id": row["article_id"],
        "title": row["title"],
        "publication": row["publication"],
        "date": row["date"],
        "publisher_location": pub_loc,
        "lat": lat if lat is not None else "",
        "lng": lng if lng is not None else "",
        "origin_location": origin_loc,
        "origin_lat": orig_lat if orig_lat is not None else "",
        "origin_lng": orig_lng if orig_lng is not None else "",
        "reprint_type": row["reprint_type"],
        "group_reprint_id": gid,
        "author": row["author"],
        "tropes": row["tropes"],
    })

# ---------------------------------------------------------------------------
# Write output
# ---------------------------------------------------------------------------
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=OUTPUT_COLS)
    writer.writeheader()
    writer.writerows(out_rows)

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
geocoded_ok = sum(1 for r in out_rows if r["lat"] != "")
print(f"\n{'='*60}")
print(f"Output: {OUTPUT_CSV}  ({len(out_rows)} rows)")
print(f"Rows with lat/lng:       {geocoded_ok} / {len(out_rows)}")
print(f"Rows missing lat/lng:    {len(out_rows) - geocoded_ok}")

if missing_locations:
    print(f"\nLocations NOT found ({len(missing_locations)}):")
    for loc in sorted(missing_locations):
        print(f"  - {loc!r}")

if missing_origins:
    print(f"\nGroups with no 'original' row ({len(set(missing_origins))}):")
    for gid in sorted(set(missing_origins)):
        print(f"  - {gid!r}")

print("="*60)
