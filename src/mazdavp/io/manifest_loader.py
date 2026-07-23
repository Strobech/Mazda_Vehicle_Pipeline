import json
from pathlib import Path

from mazdavp.manifest import MSC, Vehicle, VehicleManifest


def load_manifest(path: str | Path) -> VehicleManifest:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    vehicle = data["vehicle"]

    return VehicleManifest(
        vehicle=Vehicle(
           msc=MSC(
    vehicle["model_code"],
    vehicle["spec_code"],
),
            model_year=vehicle["model_year"],
            market=vehicle["market"],
            trim=vehicle["trim"],
            colour=vehicle["colour"],
            options=vehicle.get("options", []),
        )
    )