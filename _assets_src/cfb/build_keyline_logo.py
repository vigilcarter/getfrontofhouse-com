"""Bake the cream keyline onto the Far Bella badge and package it for the web.

House rule (memory feedback_logo_on_colour_keyline): separation comes from a cream
keyline dilated off the badge's own alpha so it hugs the silhouette. Never a plate.

This does packaging only, no retouching of the artwork:
  trim transparent margin -> dilate alpha -> fill cream halo -> composite original
  -> neutralise RGB of fully-transparent pixels (kills resize fringe) -> resize -> WebP
"""
import sys
from PIL import Image, ImageFilter

SRC = sys.argv[1]
OUT = sys.argv[2]
OUT_W = int(sys.argv[3])          # delivered width in px
CREAM = (251, 246, 226)           # #FBF6E2

im = Image.open(SRC).convert("RGBA")

# 1. trim the transparent margin so displayed height maps to the badge, not padding
bbox = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
im = im.crop(bbox)
print(f"trimmed to {im.size}")

# 2. keyline width: ~4px at 620px logo width, scaled to this asset
key = max(3, round(4 * im.width / 620))
pad = key + 6                     # margin the halo never reaches, even after lossy encode
print(f"keyline {key}px at {im.width}px wide")

canvas = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), CREAM + (0,))
canvas.alpha_composite(im, (pad, pad))

# 3. dilate the alpha to make the halo. MaxFilter size N dilates by (N-1)/2.
alpha = canvas.getchannel("A")
halo = alpha.filter(ImageFilter.MaxFilter(2 * key + 1))

# 4. cream layer at halo alpha, original badge composited on top
out = Image.new("RGBA", canvas.size, CREAM + (0,))
out.putalpha(halo)
out.alpha_composite(canvas)

# 5. transparent pixels keep stray RGB from the generator; on downscale that bleeds
#    a fringe into the keyline. Repaint them cream. No visible pixel changes.
px = out.load()
w, h = out.size
for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        if a == 0:
            px[x, y] = CREAM + (0,)

# 6. deliver
if OUT_W != out.width:
    out = out.resize((OUT_W, round(out.height * OUT_W / out.width)), Image.LANCZOS)
out.save(OUT, "WEBP", quality=92, alpha_quality=100, method=6, exact=True)
print(f"wrote {OUT} {out.size}")
