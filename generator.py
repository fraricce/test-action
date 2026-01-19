import csv
from pathlib import Path

# Paths
CSV_FILE = Path("data/icecream.csv")
OUTPUT_DIR = Path("site")
OUTPUT_FILE = OUTPUT_DIR / "index.html"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Read CSV
icecreams = []
with CSV_FILE.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        icecreams.append(row)

# HTML template parts
HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ice Cream Menu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
        }
        h1 {
            text-align: center;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px;
        }
        .price {
            font-weight: bold;
            color: #c0392b;
        }
    </style>
</head>
<body>
<h1>🍦 Ice Cream Menu</h1>
<div class="grid">
"""

HTML_FOOT = """
</div>
</body>
</html>
"""

# Build HTML cards
cards_html = ""
for icecream in icecreams:
    cards_html += f"""
    <div class="card">
        <h2>{icecream['name']}</h2>
        <p>{icecream['description']}</p>
        <p class="price">${float(icecream['price']):.2f}</p>
    </div>
    """

# Write final HTML
OUTPUT_FILE.write_text(HTML_HEAD + cards_html + HTML_FOOT, encoding="utf-8")

print(f"✅ Generated {OUTPUT_FILE}")
