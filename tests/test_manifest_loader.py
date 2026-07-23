import json
import tempfile

from mazdavp.io.manifest_loader import load_manifest

data = {
    "vehicle": {
       "model_code": "ABCD",
        "spec_code": "123",
        "model_year": "2026",
        "market": "EU",
        "trim": "Homura",
        "colour": "Soul Red",
        "options": ["PK1", "SUN"],
    }
}

with tempfile.NamedTemporaryFile(
    mode="w",
    suffix=".json",
    delete=False,
    encoding="utf-8",
) as f:
    json.dump(data, f)
    filename = f.name

manifest = load_manifest(filename)

assert manifest.vehicle.msc.value == "ABCD123"
assert manifest.vehicle.trim == "Homura"
assert manifest.vehicle.options == ["PK1", "SUN"]

print("Manifest loader test passed.")