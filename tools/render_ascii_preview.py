"""QA helper: rasterizes an ascii .txt file to a PNG so we can eyeball it."""
import sys
from PIL import Image, ImageDraw, ImageFont

path = sys.argv[1] if len(sys.argv) > 1 else "portrait.txt"
out = sys.argv[2] if len(sys.argv) > 2 else "tools/portrait_preview.png"

lines = open(path, encoding="utf-8").read().splitlines()
font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 12)
cell_w, cell_h = 7, 14
width = max(len(l) for l in lines) * cell_w + 20
height = len(lines) * cell_h + 20

img = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(img)
for i, line in enumerate(lines):
    draw.text((10, 10 + i * cell_h), line, font=font, fill=(103, 232, 249))
img.save(out)
print(f"Saved {out} ({width}x{height})")
