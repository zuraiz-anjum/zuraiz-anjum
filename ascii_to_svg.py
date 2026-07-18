from pathlib import Path
from html import escape

INPUT = "portrait.txt"
OUTPUT = "portrait_tspan.txt"

# SVG placement
START_X = -10
START_Y = -30
LINE_HEIGHT = 9

lines = Path(INPUT).read_text(encoding="utf-8", errors="ignore").splitlines()
lines = [l.rstrip() for l in lines]

y = START_Y
svg = []
for line in lines:
    svg.append(f'<tspan x="{START_X}" y="{y}">{escape(line)}</tspan>')
    y += LINE_HEIGHT

Path(OUTPUT).write_text("\n".join(svg), encoding="utf-8")
print(f"Generated {len(svg)} tspans.")
