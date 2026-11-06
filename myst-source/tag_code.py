"""Give every fenced code block in the generated pages a language, so each gets syntax
highlighting and a language label. Blocks that already name one keep it."""
import glob, re, sys

RULES = [
    ("r", r"(<-|library\(|ggplot\(|rast\(|terra::|\bc\(|data\.frame\(|install\.packages)"),
    ("javascript", r"(\bvar\s|\bconst\s|\blet\s|function\s*\(|=>|ee\.(Image|Feature|Filter|Reducer)|Map\.(addLayer|centerObject)|console\.log)"),
    ("python", r"(^\s*import\s|^\s*from\s+\S+\s+import|\bdef\s|print\(|\bee\.Initialize|geemap|np\.|pd\.|\.select\(\[)"),
    ("sql", r"^\s*(SELECT|CREATE|INSERT|WITH)\b"),
    ("bash", r"^\s*(\$\s|pip |conda |git |npm |cd |mkdir |curl |sudo )"),
    ("json", r"^\s*[\[{]\s*\"" ),
    ("yaml", r"^\w[\w-]*:\s"),
]


def guess(code):
    for lang, pat in RULES:
        if re.search(pat, code, flags=re.M | (re.I if lang == "sql" else 0)):
            return lang
    return "text"


def tag(text):
    out, i, lines = [], 0, text.split("\n")
    while i < len(lines):
        m = re.match(r"^(\s*)(`{3,}|~{3,})\s*$", lines[i])
        if m:
            fence = m.group(2)
            j = i + 1
            while j < len(lines) and not re.match(rf"^\s*{re.escape(fence)}\s*$", lines[j]):
                j += 1
            code = "\n".join(lines[i + 1:j])
            out.append(f"{m.group(1)}{fence}{guess(code)}")
            out.extend(lines[i + 1:j + 1])
            i = j + 1
            continue
        m = re.match(r"^(\s*)(`{3,}|~{3,})\s*\S", lines[i])
        if m:  # already has a language: copy through to the closing fence untouched
            fence = m.group(2)
            j = i + 1
            while j < len(lines) and not re.match(rf"^\s*{re.escape(fence)}\s*$", lines[j]):
                j += 1
            out.extend(lines[i:j + 1])
            i = j + 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


files = sys.argv[1:] or (glob.glob("repos/**/*.md", recursive=True) + glob.glob("blog/*.md") + glob.glob("skripsi/*.md"))
n = 0
for f in files:
    s = open(f, encoding="utf8").read()
    t = tag(s)
    if t != s:
        open(f, "w", encoding="utf8").write(t)
        n += 1
print("tagged", n, "files")
