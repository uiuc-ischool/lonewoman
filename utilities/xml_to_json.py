#!/usr/bin/env python3
"""Convert TEI XML articles to JSON transcript format.

Usage:
    python utilities/xml_to_json.py                         # process all XML files
    python utilities/xml_to_json.py AlbanyEveningJournal1853  # specific article(s)

Output: objects/{articleid}/{articleid}_transcript.json
"""

import json
import re
import sys
from pathlib import Path

from lxml import etree

NS = "http://www.tei-c.org/ns/1.0"

# Block-level elements to skip entirely when collecting paragraphs
BLOCK_SKIP = {"note", "head", "byline", "dateline", "opener", "closer", "salute", "figure", "figDesc"}

# Inline elements whose content should be dropped (e.g. footnote markers)
INLINE_SKIP = {"note"}


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def get_inner_text(elem):
    """Collect all text inside an element, skipping <note> footnotes, excluding the element's own tail."""
    parts = []
    if elem.text:
        parts.append(elem.text)
    for child in elem:
        if not isinstance(child.tag, str):
            if child.tail:
                parts.append(child.tail)
            continue
        local = etree.QName(child.tag).localname
        if local not in INLINE_SKIP:
            parts.append(get_inner_text(child))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def extract_segments(p_elem):
    """Walk a <p> element and return a list of text segments.

    Handles nested/overlapping trope spans via an active_tropes stack.
    Each segment: {'text': str} or {'text': str, 'tropes': [int, ...]}.
    """
    segments = []
    buf = []
    active_tropes = []

    def flush():
        text = normalize("".join(buf))
        if text:
            seg = {"text": text}
            if active_tropes:
                seg["tropes"] = list(active_tropes)
            segments.append(seg)
        buf.clear()

    def walk(elem):
        if not isinstance(elem.tag, str):
            if elem.tail:
                buf.append(elem.tail)
            return

        local = etree.QName(elem.tag).localname

        if local in INLINE_SKIP:
            if elem.tail:
                buf.append(elem.tail)
            return

        if local == "span" and elem.get("type") == "trope":
            flush()
            trope_n = int(elem.get("n"))
            active_tropes.append(trope_n)
            if elem.text:
                buf.append(elem.text)
            for child in elem:
                walk(child)
            flush()
            active_tropes.pop()
            if elem.tail:
                buf.append(elem.tail)
        else:
            if elem.text:
                buf.append(elem.text)
            for child in elem:
                walk(child)
            if elem.tail:
                buf.append(elem.tail)

    if p_elem.text:
        buf.append(p_elem.text)
    for child in p_elem:
        walk(child)
    flush()
    return segments


def process_lg(lg_elem):
    """Process a <lg> (line group / poem stanza) into a single segment."""
    lines = []
    for l in lg_elem.iter(f"{{{NS}}}l"):
        line_text = normalize(get_inner_text(l))
        if line_text:
            lines.append(line_text)
    if not lines:
        return None

    trope_n = None
    if lg_elem.get("type") == "trope-group":
        n = lg_elem.get("n")
        if n:
            trope_n = int(n)

    segment = {"text": "\n".join(lines)}
    if trope_n is not None:
        segment["tropes"] = [trope_n]
    return [segment]


def collect_paragraphs(elem, paragraphs):
    """Recursively walk a div tree collecting <p> and <floatingText> content."""
    for child in elem:
        if not isinstance(child.tag, str):
            continue
        local = etree.QName(child.tag).localname

        if local in BLOCK_SKIP:
            continue
        elif local == "p":
            segs = extract_segments(child)
            if segs:
                paragraphs.append(segs)
        elif local == "floatingText":
            for lg in child.iter(f"{{{NS}}}lg"):
                segs = process_lg(lg)
                if segs:
                    paragraphs.append(segs)
        else:
            collect_paragraphs(child, paragraphs)


def parse_article(xml_path):
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    body = root.find(f".//{{{NS}}}body")
    if body is None:
        raise ValueError(f"No <body> found in {xml_path}")

    # Prefer <div type="article">, then first <div> child, then body itself
    article_div = body.find(f".//{{{NS}}}div[@type='article']")
    if article_div is None:
        if body.find(f"{{{NS}}}p") is not None:
            # Body has direct <p> children — no wrapper div, use body itself
            article_div = body
        else:
            article_div = body.find(f"{{{NS}}}div")
    if article_div is None:
        raise ValueError(f"No processable content found in {xml_path}")

    paragraphs = []
    collect_paragraphs(article_div, paragraphs)
    return paragraphs


def main():
    repo_root = Path(__file__).parent.parent
    objects_dir = repo_root / "objects"

    if len(sys.argv) < 2:
        xml_files = sorted(objects_dir.glob("*/m_*_TEI.xml"))
        if not xml_files:
            print("No TEI XML files found under objects/", file=sys.stderr)
            sys.exit(1)
    else:
        xml_files = []
        for article_id in sys.argv[1:]:
            p = objects_dir / article_id / f"m_{article_id}_TEI.xml"
            xml_files.append(p)

    for xml_path in xml_files:
        xml_path = Path(xml_path)
        if not xml_path.exists():
            print(f"Warning: {xml_path} not found", file=sys.stderr)
            continue

        article_id = xml_path.parent.name
        print(f"Processing {article_id}...", end=" ", flush=True)

        try:
            paragraphs = parse_article(xml_path)
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            continue

        output = {"article_id": article_id, "paragraphs": paragraphs}
        out_path = xml_path.parent / f"{article_id}_transcript.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"-> {out_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
