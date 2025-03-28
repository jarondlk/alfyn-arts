import os
from pathlib import Path

base_dir = Path("assets")
image_exts = [".png", ".jpg", ".jpeg", ".gif"]
folders = sorted(
    [f for f in base_dir.iterdir() if f.is_dir() and f.name[:4].isdigit()],
    reverse=True
)

html = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
    "  <title>Alfyn Art Archive</title>",
    "  <link href='https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/css/lightbox.min.css' rel='stylesheet'>",
    "  <style>",
    "    body { font-family: sans-serif; max-width: 900px; margin: auto; padding: 2rem; }",
    "    h1 { text-align: center; margin-bottom: 1rem; }",
    "    nav { margin-bottom: 1.5rem; }",
    "    nav a { margin-right: 0.5rem; text-decoration: none; color: #0077cc; font-weight: bold; }",
    "    .date-section {",
    "      position: sticky;",
    "      top: 0;",
    "      background: white;",
    "      padding: 0.5rem 0;",
    "      z-index: 10;",
    "      border-bottom: 1px solid #eee;",
    "    }",
    "    .img-grid {",
    "      display: grid;",
    "      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));",
    "      gap: 1rem;",
    "      margin-bottom: 2rem;",
    "    }",
    "    .img-grid img {",
    "      width: 100%;",
    "      border-radius: 8px;",
    "      box-shadow: 0 2px 6px rgba(0,0,0,0.1);",
    "      cursor: pointer;",
    "    }",
    "  </style>",
    "</head>",
    "<body>",
    "  <h1>Alfyn Art Archive</h1>",
]

# Jump-to nav
html.extend([
    "<nav><strong>Jump to:</strong><br>",
    *[f"<a href='#{f.name}'>{f.name}</a>" for f in folders],
    "</nav><hr>"
])

# Image sections
for folder in folders:
    images = [f for f in folder.iterdir() if f.suffix.lower() in image_exts]
    if images:
        html.append(f"<h2 class='date-section' id='{folder.name}'>{folder.name}</h2>")
        html.append("<div class='img-grid'>")
        for image in images:
            src = f"{folder.parent.name}/{folder.name}/{image.name}"
            html.append(f"<a href='{src}' data-lightbox='{folder.name}' data-title='{image.name}'>")
            html.append(f"<img src='{src}' alt='{image.name}' loading='lazy'>")
            html.append("</a>")
        html.append("</div>")

# Close it out
html.extend([
    "<script src='https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js'></script>",
    "</body>",
    "</html>"
])

with open("index.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html))
