"""Turn the guide PDFs into MyST Markdown pages with their images (pymupdf4llm)."""
import os, re, warnings
warnings.filterwarnings("ignore")
import pymupdf4llm

GUIDES = [
    ("public/perpus/panduan-layout-composer.pdf", "panduan/layout-composer.md", "Panduan Layout Composer", "assets/panduan/layout-composer"),
    ("public/perpus/panduan-gbif-data.pdf", "panduan/gbif-data.md", "Panduan GBIF Data", "assets/panduan/gbif-data"),
]
for pdf, out, title, img_dir in GUIDES:
    os.makedirs(img_dir, exist_ok=True)
    md = pymupdf4llm.to_markdown(pdf, write_images=True, image_path=img_dir, image_format="png", dpi=110, show_progress=False)
    # Image paths relative to the page in panduan/.
    md = md.replace(img_dir.replace("\\", "/") + "/", "../" + img_dir + "/").replace(img_dir.replace("/", "\\") + "\\", "../" + img_dir + "/")
    md = re.sub(r"\n{3,}", "\n\n", md)
    open(out, "w", encoding="utf8").write(f"---\ntitle: {title}\n---\n\n" + md)
    print(out, len(md), "chars", len(os.listdir(img_dir)), "images")
