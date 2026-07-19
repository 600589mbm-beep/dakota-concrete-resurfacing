from __future__ import annotations

import base64
import io
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "tools" / "seo-payload"
PART_COUNT = 7

payload = "".join(
    (PARTS_DIR / f"payload.{index:02d}.txt").read_text(encoding="utf-8").strip()
    for index in range(1, PART_COUNT + 1)
)

archive_bytes = base64.b64decode(payload, validate=True)
with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
    archive.testzip()
    archive.extractall(ROOT)

required_files = [
    "index.html",
    "styles.css",
    "script.js",
    "robots.txt",
    "sitemap.xml",
    "driveway-resurfacing.html",
    "patio-resurfacing.html",
    "pool-deck-resurfacing.html",
    "sidewalk-walkway-resurfacing.html",
    "front-entry-steps-resurfacing.html",
]
missing = [path for path in required_files if not (ROOT / path).is_file()]
if missing:
    raise RuntimeError(f"SEO site generation failed; missing: {', '.join(missing)}")

print("Generated SEO-ready Dakota Concrete website")
