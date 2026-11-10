"""Cut sprites out of a magenta asset sheet.

usage: python extract.py <raw_dir> <out_dir>
raw_dir holds sheet.png and ground.png; out_dir gets one PNG per sprite.
Sheet layout (row-major): run1, run2, boxes, barrier, envelope, puddle.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

NAMES = ["run1", "run2", "boxes", "barrier", "envelope", "puddle"]
SPRITE_MAX = 320  # px, about 2x the largest on-screen size
GROUND_W = 720


def key_magenta(rgb):
    r, g, b = (rgb[..., i].astype(np.int32) for i in range(3))
    # magenta: red and blue high, green low
    magenta = (r - g > 90) & (b - g > 90) & (np.abs(r - b) < 110)
    alpha = np.where(magenta, 0, 255).astype(np.uint8)
    # despill: pull pink fringe toward neutral
    spill = np.minimum(r, b) - g
    fringe = (~magenta) & (spill > 40)
    out = rgb.copy()
    out[fringe, 0] = np.clip(r[fringe] - spill[fringe] // 2, 0, 255)
    out[fringe, 2] = np.clip(b[fringe] - spill[fringe] // 2, 0, 255)
    return out, alpha


def shrink(img, longest, pixel):
    scale = longest / max(img.size)
    if scale >= 1:
        return img
    size = (round(img.width * scale), round(img.height * scale))
    return img.resize(size, Image.NEAREST if pixel else Image.LANCZOS)


def main(raw_dir, out_dir):
    raw_dir, out_dir = Path(raw_dir), Path(out_dir)
    pixel = out_dir.name == "pixel"
    out_dir.mkdir(parents=True, exist_ok=True)
    rgb = np.array(Image.open(raw_dir / "sheet.png").convert("RGB"))
    rgb, alpha = key_magenta(rgb)
    solid = ndimage.binary_opening(alpha > 0, iterations=2)
    # merge sparkles, droplets and cone+barrier into their parent item
    merged = ndimage.binary_dilation(solid, iterations=45)
    labels, n = ndimage.label(merged)
    boxes = ndimage.find_objects(labels)
    items = []
    for i, sl in enumerate(boxes, start=1):
        area = (solid[sl] & (labels[sl] == i)).sum()
        if area < 2000:
            continue
        cy = (sl[0].start + sl[0].stop) / 2
        cx = (sl[1].start + sl[1].stop) / 2
        items.append((area, cy, cx, i, sl))
    # some models print item labels under the art; keep the six largest shapes
    items = [t[1:] for t in sorted(items, reverse=True)[:len(NAMES)]]
    h = rgb.shape[0]
    items.sort(key=lambda t: (round(t[0] / (h / 4)), t[1]))
    if len(items) != len(NAMES):
        print(f"warning: found {len(items)} items, expected {len(NAMES)}")
    for name, (_, _, i, sl) in zip(NAMES, items):
        mask = solid[sl] & (labels[sl] == i)
        ys, xs = np.nonzero(mask)
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        crop = np.dstack([rgb[sl][y0:y1, x0:x1], np.where(mask, alpha[sl], 0)[y0:y1, x0:x1]])
        sprite = shrink(Image.fromarray(crop, "RGBA"), SPRITE_MAX, pixel)
        sprite.save(out_dir / f"{name}.png", optimize=True)
        print(name, *sprite.size)
    ground = Image.open(raw_dir / "ground.png").convert("RGB")
    ground = shrink(ground, GROUND_W * ground.height / ground.width, pixel)
    ground.save(out_dir / "ground.jpg", quality=88)
    print("ground", *ground.size)


if __name__ == "__main__":
    main(*sys.argv[1:3])
