"""Tidy the copied notebooks for the web: a title cell (MyST frontmatter) naming the repo and file,
and long text output (install logs, prints) cut to 20 lines. Plots and tables stay as they are."""
import glob, json, sys

MAX = 20


def tidy(path, title):
    nb = json.load(open(path, encoding="utf8"))
    cells = nb.get("cells", [])
    if not (cells and "".join(cells[0].get("source", [])).startswith("---")):
        cells.insert(0, {"cell_type": "markdown", "metadata": {}, "source": [f"---\ntitle: {json.dumps(title)}\n---\n"]})
    for c in cells:
        for o in c.get("outputs", []):
            if o.get("output_type") == "stream":
                lines = "".join(o.get("text", [])).split("\n")
                if len(lines) > MAX:
                    o["text"] = "\n".join(lines[:MAX] + [f"… ({len(lines) - MAX} baris lagi)"])
    nb["cells"] = cells
    json.dump(nb, open(path, "w", encoding="utf8"), ensure_ascii=False)


if __name__ == "__main__":
    for p in glob.glob("repos/*/nb/*.ipynb"):
        meta = json.load(open(p, encoding="utf8")).get("metadata", {})
        tidy(p, meta.get("title") or p.split("/")[-1])
    print("tidied", len(glob.glob("repos/*/nb/*.ipynb")))
