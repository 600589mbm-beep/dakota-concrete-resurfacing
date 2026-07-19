from __future__ import annotations

import base64
import hashlib
import io
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "tools" / "seo-payload"
OUTPUT_DIR = ROOT / "dist"
PART_COUNT = 7
EXPECTED_PAYLOAD_SHA256 = "21da5255bbe5341d895e1d80e2851ab4a14ed7af3b7b42cb9571202bda14c7b1"
EXPECTED_ARCHIVE_SHA256 = "fbc23ab7e47ac0a4be7527ef710e76664c5d21c1aa10851bb335fe474cb7edeb"

payload = "".join(
    (PARTS_DIR / f"payload.{index:02d}.txt").read_text(encoding="utf-8").strip()
    for index in range(1, PART_COUNT + 1)
)

payload_sha256 = hashlib.sha256(payload.encode("utf-8")).hexdigest()
if payload_sha256 != EXPECTED_PAYLOAD_SHA256:
    raise RuntimeError(
        f"SEO payload checksum mismatch: {payload_sha256} != {EXPECTED_PAYLOAD_SHA256}"
    )

archive_bytes = base64.b64decode(payload, validate=True)
archive_sha256 = hashlib.sha256(archive_bytes).hexdigest()
if archive_sha256 != EXPECTED_ARCHIVE_SHA256:
    raise RuntimeError(
        f"SEO archive checksum mismatch: {archive_sha256} != {EXPECTED_ARCHIVE_SHA256}"
    )

if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir(parents=True)

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
