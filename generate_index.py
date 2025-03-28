import os
from pathlib import Path

image_exts = [".png", ".jpg", ".jpeg"]
folders = sorted([f for f in Path(".").iterdir() if f.is_dir() and f.name[:4].isdigit()])

html = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
    "  <title>Alfyn Art Archive</title>",
    "  <style>",
    "    body { font-family: sans-serif; max-width: 800px; margin: auto; padding: 2rem; }",
    "    .img-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem; }",
    "    img { width: 100%; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }",
    "    h2 { margin-top: 2rem; }",
    "  </style>",
    "</head><body>",
    "  <h1>Alfyn Art Archive</h1>",
]

for folder in folders:
    images = [f for f in folder.iterdir() if f.suffix.lower() in image_exts]
    if images:
        html.append(f"<h2>{folder.name}</h2>")
        html.append("<div class='img-grid'>")
        for image in images:
            src = f"{folder.name}/{image.name}"
            html.append(f"<img src='{src}' alt='{image.name}'>")
        html.append("</div>")

html.extend(["</body>", "</html>"])

with open("index.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html))
