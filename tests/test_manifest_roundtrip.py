import tempfile

from mazdavp.builder import ManifestBuilder
from mazdavp.io.manifest_loader import load_manifest
from mazdavp.io.manifest_writer import save_manifest


builder = ManifestBuilder()

builder.set("model_code", "ABCD", "test")
builder.set("spec_code", "123", "test")
builder.set("model_year", "2026", "test")
builder.set("market", "EU", "test")
builder.set("trim", "Homura", "test")
builder.set("colour", "Soul Red", "test")
builder.add_option("PK1")
builder.add_option("SUN")

manifest = builder.build()

with tempfile.NamedTemporaryFile(
    suffix=".json",
    delete=False,
) as f:
    filename = f.name

save_manifest(manifest, filename)

loaded = load_manifest(filename)

assert loaded.vehicle.msc.value == manifest.vehicle.msc.value
assert loaded.vehicle.model_year == manifest.vehicle.model_year
assert loaded.vehicle.market == manifest.vehicle.market
assert loaded.vehicle.trim == manifest.vehicle.trim
assert loaded.vehicle.colour == manifest.vehicle.colour
assert loaded.vehicle.options == manifest.vehicle.options

print("Manifest round-trip test passed.")