"""Official Deyron Labs cube (raised lid, gap, #1a1a1a outline) as a pasted asset.

RULE (7 Nov 2026, claude/REGULA-LOGO-OFICIAL.md): never draw the cube with polygons. Load the official file
(public/brand/cube-official.png, rendered from public/brand/deyron-labs-logo.svg) and paste it.
"""
import os
from PIL import Image

ASSET = os.environ.get("CUBE_PNG") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "public", "brand", "cube-official.png")
_cache = {}


def cube(height):
    """RGBA cube image, `height` px tall (width follows the asset aspect 1204:1508)."""
    if height not in _cache:
        im = Image.open(ASSET).convert("RGBA")
        w = round(im.width * height / im.height)
        _cache[height] = im.resize((w, height), Image.LANCZOS)
    return _cache[height]
