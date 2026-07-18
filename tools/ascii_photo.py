"""
Converts a portrait photo into ASCII art (no external binary required).
Usage: python tools/ascii_photo.py <input_image> <output_txt> [--width 90]
"""
import sys
import argparse
from PIL import Image, ImageOps, ImageEnhance

# Dense-to-sparse ramp; index scales with brightness (0=black -> len-1=white)
RAMP = "@%#*+=-:. "


def image_to_ascii(path, width=90, contrast=1.1, sharpness=1.8, gamma=0.8, char_aspect=2.15):
    img = Image.open(path).convert("RGB")
    img = ImageOps.exif_transpose(img)
    img = ImageOps.autocontrast(img, cutoff=0.5)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Sharpness(img).enhance(sharpness)

    gray = img.convert("L")
    w, h = gray.size
    new_h = max(1, int((h / w) * width / char_aspect))
    gray = gray.resize((width, new_h), Image.LANCZOS)

    # gamma-correct so midtones (skin, facial features) separate from
    # near-black hair/clothing instead of all clumping at the dense end
    gamma_lut = [int((v / 255) ** gamma * 255) for v in range(256)]
    gray = gray.point(gamma_lut)

    pixels = gray.load()
    ramp_len = len(RAMP)
    lines = []
    for y in range(new_h):
        row = []
        for x in range(width):
            lum = pixels[x, y]
            idx = min(ramp_len - 1, lum * ramp_len // 256)
            row.append(RAMP[idx])
        lines.append("".join(row).rstrip())

    # trim fully-blank rows from top/bottom to keep the portrait centered
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--width", type=int, default=90)
    parser.add_argument("--char-aspect", type=float, default=2.15)
    args = parser.parse_args()

    lines = image_to_ascii(args.input, width=args.width, char_aspect=args.char_aspect)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Generated {len(lines)} lines -> {args.output}")
