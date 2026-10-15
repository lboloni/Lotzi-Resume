"""List which bib entries have a PDF in source/papers/ and which do not.

usage (from the repository root):
  python3 tools/check_papers.py

Prints a Markdown report: PDFs without a bib entry, cited entries without a PDF
(by publication list), and uncited entries without a PDF. It only reports; it does
not fetch or rename anything. PDFs are named <bibkey>.pdf.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bibcheck import ROOT, cited_keys, parse_bib  # noqa: E402


def main():
    bib = parse_bib(ROOT / "source/bib/Boloni.bib")
    pdfs = {p.stem for p in (ROOT / "source/papers").glob("*.pdf")}
    cites = cited_keys()
    allc = {k for keys in cites.values() for k in keys}

    print("# Paper PDFs\n")
    print(f"{len(pdfs)} PDFs in `source/papers/`; {len(bib)} bib entries, "
          f"{len(pdfs & bib.keys())} of them with a PDF.\n")

    orphans = sorted(pdfs - bib.keys())
    print("## PDFs without a bib entry\n")
    print("\n".join(f"- `{k}.pdf`" for k in orphans) if orphans else "None.")
    print()

    print("## Cited entries without a PDF\n")
    for name, keys in cites.items():
        miss = sorted(set(keys) - pdfs, key=lambda k: (bib.get(k, {}).get("year", ""), k), reverse=True)
        print(f"### {name} ({len(miss)} of {len(set(keys))} missing)\n")
        for k in miss:
            print(f"- `{k}` ({bib.get(k, {}).get('year', '?')})")
        print()

    unc = sorted(k for k in bib.keys() - allc - pdfs)
    print("## Uncited entries without a PDF\n")
    print("\n".join(f"- `{k}`" for k in unc) if unc else "None.")


if __name__ == "__main__":
    main()
