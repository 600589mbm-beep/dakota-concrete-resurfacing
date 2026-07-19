from __future__ import annotations

import base64
import io
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "tools" / "seo-payload"
OUTPUT_DIR = ROOT / "dist"
PART_COUNT = 7

payload = "".join(
    (PARTS_DIR / f"payload.{index:02d}.txt").read_text(encoding="utf-8").strip()
    for index in range(1, PART_COUNT + 1)
)

if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir(parents=True)

archive_bytes = base64.b64decode(payload, validate=True)
with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
    bad_file = archive.testzip()
    if bad_file:
        raise RuntimeError(f"Corrupt SEO payload member: {bad_file}")
    archive.extractall(OUTPUT_DIR)

for public_asset in ("favicon.svg",):
    source = ROOT / public_asset
    if source.is_file():
        shutil.copy2(source, OUTPUT_DIR / public_asset)

(OUTPUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

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
    "404.html",
    "site.webmanifest",
]
missing = [path for path in required_files if not (OUTPUT_DIR / path).is_file()]
if missing:
    raise RuntimeError(f"SEO site generation failed; missing: {', '.join(missing)}")

print(f"Generated SEO-ready Dakota Concrete website in {OUTPUT_DIR}")
