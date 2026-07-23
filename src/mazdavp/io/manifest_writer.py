import json
from pathlib import Path

from mazdavp.manifest import VehicleManifest


def save_manifest(
    manifest: VehicleManifest,
    path: str | Path,
) -> None:
    vehicle = manifest.vehicle

    data = {
        "vehicle": {
            "model_code": vehicle.msc.model_code,
            "spec_code": vehicle.msc.spec_code,
            "model_year": vehicle.model_year,
            "market": vehicle.market,
            "trim": vehicle.trim,
            "colour": vehicle.colour,
            "options": vehicle.options,
        }
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)