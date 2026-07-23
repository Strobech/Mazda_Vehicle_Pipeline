from pathlib import Path

from mazdavp.pipeline import Pipeline
from mazdavp.io import load_manifest


output = Path("pipeline_save_test.json")

pipeline = Pipeline()

pipeline.set("model_code", "ABCD", "test")
pipeline.set("spec_code", "123", "test")
pipeline.set("model_year", "2026", "test")
pipeline.set("market", "EU", "test")
pipeline.set("trim", "Homura", "test")
pipeline.set("colour", "Soul Red", "test")

pipeline.add_option("PK1")
pipeline.add_option("SUN")

pipeline.save(output)

manifest = load_manifest(output)

assert manifest.vehicle.msc.value == "ABCD123"
assert manifest.vehicle.model_year == "2026"
assert manifest.vehicle.market == "EU"
assert manifest.vehicle.trim == "Homura"
assert manifest.vehicle.colour == "Soul Red"
assert manifest.vehicle.options == ["PK1", "SUN"]

output.unlink()

print("Pipeline save test passed.")