"""Check the CV bibliography and print a Markdown report for Lotzi.

usage (from the repository root):
  python3 tools/bibcheck.py [--inventory PATH] [--damla PATH] > report.md

Sections of the report:
  1. duplicated \\nocite keys in source/publists/*.tex, and cited keys missing from Boloni.bib;
  2. Boloni.bib entries that no publication list cites;
  3. 2025-2026 papers in Lotzi-Literature-Review/OurPapers/INVENTORY.tsv
     (published or accepted) that are not in Boloni.bib;
  4. joint papers with Damla's damla.bib whose author list or DOI differ.
It only reports; it does not change any file.
"""
import argparse, csv, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = ROOT.parent if (ROOT.parent / "Damla-Resume").exists() else Path.home() / "Documents/Develop/Github"


def parse_bib(path):
    """Return {key: {'type': ..., field: value}} for a .bib file (brace-balanced, stdlib only)."""
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    out, i = {}, 0
    while True:
        m = re.compile(r"@(\w+)\s*([{(])", re.S).search(text, i)
        if not m:
            return out
        etype, start = m.group(1).lower(), m.end()
        depth, j = 1, start
        while j < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        body, i = text[start:j - 1], j
        if etype in ("comment", "string", "preamble"):
            continue
        key, _, rest = body.partition(",")
        fields = {"type": etype}
        k = 0
        while k < len(rest):
            fm = re.compile(r"\s*([\w-]+)\s*=\s*", re.S).match(rest, k)
            if not fm:
                break
            name, k = fm.group(1).lower(), fm.end()
            if k < len(rest) and rest[k] == "{":
                d, s = 1, k + 1
                k += 1
                while k < len(rest) and d:
                    d += {"{": 1, "}": -1}.get(rest[k], 0)
                    k += 1
                val = rest[s:k - 1]
            elif k < len(rest) and rest[k] == '"':
                e = rest.index('"', k + 1)
                val, k = rest[k + 1:e], e + 1
            else:
                vm = re.compile(r"[^,]*").match(rest, k)
                val, k = vm.group(0), vm.end()
            fields[name] = " ".join(val.split())
            cm = re.compile(r"\s*,?").match(rest, k)
            k = cm.end()
        out[key.strip()] = fields


def norm_title(t):
    t = re.sub(r"\\([ij])(?![a-zA-Z])", r"\1", t or "")  # dotless i/j, e.g. Bacanl{\i}
    t = unicodedata.normalize("NFKD", re.sub(r"\\[a-zA-Z]+|[{}\\\"'`^~]", "", t))
    return re.sub(r"[^a-z0-9]", "", t.encode("ascii", "ignore").decode().lower())


def norm_doi(d):
    d = (d or "").strip().lower()
    return re.sub(r"^(https?://)?(dx\.)?doi\.org/|^doi:\s*", "", d)


def last_names(authors):
    names = []
    for a in re.split(r"\s+and\s+", authors or ""):
        a = a.replace("~", " ").strip()
        if not a:
            continue
        last = a.split(",")[0] if "," in a else a.split()[-1]
        names.append(norm_title(last))
    return names


def cited_keys():
    cites = {}
    for f in sorted((ROOT / "source/publists").glob("*.tex")):
        keys = []
        for line in f.read_text().splitlines():
            line = line.split("%")[0]
            keys += re.findall(r"\\nocite\{([^}]+)\}", line)
        cites[f.stem] = keys
    return cites


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", default=GITHUB / "Lotzi-Literature-Review/OurPapers/INVENTORY.tsv")
    ap.add_argument("--damla", default=GITHUB / "Damla-Resume/source/bib/damla.bib")
    args = ap.parse_args()

    bib = parse_bib(ROOT / "source/bib/Boloni.bib")
    by_doi = {norm_doi(v.get("doi")): k for k, v in bib.items() if v.get("doi")}
    by_title = {norm_title(v.get("title")): k for k, v in bib.items()}
    cites = cited_keys()
    p = print

    p("# Bibliography check\n")
    p(f"`source/bib/Boloni.bib`: {len(bib)} entries.\n")

    p("## 1. Publication lists\n")
    problems = False
    for name, keys in cites.items():
        dups = sorted({k for k in keys if keys.count(k) > 1})
        missing = sorted({k for k in keys if k not in bib})
        p(f"- `{name}.tex`: {len(set(keys))} keys"
          + (f"; duplicated: {', '.join(dups)}" if dups else "")
          + (f"; **not in the bib**: {', '.join(missing)}" if missing else ""))
        problems |= bool(dups or missing)
    p("" if problems else "\nNo duplicated or missing keys.\n")

    p("## 2. Bib entries not cited by any list\n")
    allc = {k for keys in cites.values() for k in keys}
    unc = sorted(k for k in bib if k not in allc)
    for k in unc:
        v = bib[k]
        p(f"- `{k}` ({v['type']}, {v.get('year', '?')}): {v.get('title', '')}")
    p("")

    inv = Path(args.inventory)
    p("## 3. 2025-2026 papers in the inventory that are not in Boloni.bib\n")
    if not inv.exists():
        p(f"Inventory not found: `{inv}`\n")
    else:
        n = 0
        for r in csv.DictReader(inv.open(encoding="utf-8"), delimiter="\t"):
            if r["year"] not in ("2025", "2026") or r["kind"] != "paper" or r["status"] not in ("published", "accepted"):
                continue
            listed = {x.strip().removesuffix(".bib") for x in r["publication_list_bib"].split(";")}
            if listed & bib.keys() or norm_doi(r["doi"]) in by_doi or norm_title(r["title"]) in by_title:
                continue
            n += 1
            p(f"- {r['work_id']} ({r['year']}, {r['status']}): {r['title']}. {r['venue']}."
              + (f" doi:{r['doi']}" if r["doi"] else ""))
        p("" if n else "None.\n")

    damla = Path(args.damla)
    p("## 4. Joint papers with damla.bib\n")
    if not damla.exists():
        p(f"Not found: `{damla}`\n")
        return
    dbib = parse_bib(damla)
    joint = matched = 0
    rows = []
    for dk, dv in dbib.items():
        if "boloni" not in norm_title(dv.get("author")):
            continue
        joint += 1
        k = by_doi.get(norm_doi(dv.get("doi"))) if dv.get("doi") else None
        k = k or by_title.get(norm_title(dv.get("title")))
        k = k or (dk if dk in bib else None)  # same key, different title
        if not k:
            rows.append(f"- `{dk}` ({dv.get('year', '?')}) is in damla.bib only: {dv.get('title', '')}")
            continue
        matched += 1
        bv = bib[k]
        diffs = []
        if last_names(bv.get("author")) != last_names(dv.get("author")):
            diffs.append(f"authors: Boloni.bib `{bv.get('author')}` / damla.bib `{dv.get('author')}`")
        if norm_title(bv.get("title")) != norm_title(dv.get("title")):
            diffs.append(f"title: Boloni.bib `{bv.get('title')}` / damla.bib `{dv.get('title')}`")
        if dv.get("doi") and norm_doi(bv.get("doi")) != norm_doi(dv.get("doi")):
            diffs.append(f"DOI: Boloni.bib `{bv.get('doi', '(none)')}` / damla.bib `{dv.get('doi')}`")
        if diffs:
            rows.append(f"- `{k}` = damla `{dk}`: " + "; ".join(diffs))
    p(f"{joint} damla.bib entries have Bölöni as an author; {matched} match a Boloni.bib entry (by DOI, title or key).\n")
    p("\n".join(rows) if rows else "No differences.")
    p("")


if __name__ == "__main__":
    sys.exit(main())
