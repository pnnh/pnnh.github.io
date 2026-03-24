from pathlib import Path

docs_dir = Path("docs")
posts_dir = Path("_posts")
today = "2026-03-24"

# Tags per category directory
CATEGORY_TAGS = {
    "CPlus":      ["cpp", "cmake"],
    "Database":   ["database", "sql"],
    "Devserver":  ["server", "library", "build"],
    "Docker":     ["docker", "container"],
    "Dotnet":     ["dotnet", "csharp", "nuget"],
    "Flutter":    ["flutter", "dart"],
    "Gentoo":     ["gentoo", "linux"],
    "Git":        ["git"],
    "Java":       ["java"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Linux":      ["linux", "shell"],
    "Macos":      ["macos"],
    "Nodejs":     ["nodejs", "javascript", "npm"],
    "Python":     ["python"],
    "Qt":         ["qt", "cpp", "qml"],
    "Rust":       ["rust"],
    "Swift":      ["swift", "ios"],
    "Ubuntu":     ["ubuntu", "linux", "apt"],
    "VScode":     ["vscode"],
    "Windows":    ["windows"],
    "其它":       ["misc"],
}


def strip_front_matter(content):
    if not content.startswith("---"):
        return content
    end = content.find("\n---", 3)
    if end == -1:
        return content
    return content[end + 4:].strip()


def yaml_str(s):
    if '"' in s:
        return "'" + s.replace("'", "''") + "'"
    return '"' + s + '"'


count = 0

for md_file in sorted(docs_dir.rglob("*.md")):
    if md_file.name == "metadata.md":
        continue

    category = md_file.parent.name
    title = md_file.stem
    content = md_file.read_text(encoding="utf-8")
    body = strip_front_matter(content)

    tags = CATEGORY_TAGS.get(category, [])
    tags_str = ", ".join(tags)

    rel_subdir = md_file.parent.relative_to(docs_dir)
    out_dir = posts_dir / rel_subdir
    out_dir.mkdir(parents=True, exist_ok=True)

    out_name = f"{today}-{md_file.name}"
    out = out_dir / out_name

    new_content = (
        "---\n"
        "layout: post\n"
        f"title: {yaml_str(title)}\n"
        f"date: {today} 00:00:00 +0800\n"
        f"categories: [{category}]\n"
        f"tags: [{tags_str}]\n"
        "---\n\n"
        + body + "\n"
    )

    out.write_text(new_content, encoding="utf-8")
    count += 1

print(f"Done! Created {count} posts in _posts/")

