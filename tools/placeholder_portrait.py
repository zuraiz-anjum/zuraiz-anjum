"""
Generates a placeholder ASCII silhouette (used until a real photo is converted).
"""
import math
from pathlib import Path

WIDTH = 90
HEIGHT = 42
RAMP = " .:-=+*#%@"


def silhouette():
    lines = []
    cx, cy = WIDTH / 2, HEIGHT * 0.36
    head_r = HEIGHT * 0.30
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            nx = (x - cx) / (WIDTH / 2)
            ny = (y - cy) / HEIGHT
            head = ((x - cx) ** 2) / (head_r * 1.15) ** 2 + ((y - cy) ** 2) / (head_r * 1.35) ** 2
            shoulder_top = HEIGHT * 0.62
            body = 0
            if y > shoulder_top:
                spread = (y - shoulder_top) / (HEIGHT - shoulder_top)
                half_w = (WIDTH * 0.20) + spread * (WIDTH * 0.28)
                body = abs(x - cx) / half_w if half_w else 2
            inside_head = head <= 1
            inside_body = y > shoulder_top and body <= 1
            if inside_head or inside_body:
                edge = min(abs(head - 1), abs(body - 1)) if inside_body else abs(head - 1)
                shade = 8 if edge < 0.06 else (5 if edge < 0.18 else 3)
                row.append(RAMP[shade])
            else:
                row.append(" ")
        lines.append("".join(row).rstrip())
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


if __name__ == "__main__":
    Path("portrait.txt").write_text("\n".join(silhouette()), encoding="utf-8")
    print(f"Generated {len(silhouette())} placeholder lines -> portrait.txt")
