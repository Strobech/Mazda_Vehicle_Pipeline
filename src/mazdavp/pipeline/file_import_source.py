from __future__ import annotations

from pathlib import Path

from mazdavp.builder import ManifestBuilder
from mazdavp.io import load_manifest
from mazdavp.pipeline.import_source import ImportSource


class FileImportSource(ImportSource):
    """
    Imports vehicle information from an existing manifest file.
    """

    def __init__(self, path: str | Path):
        self._path = Path(path)

    def import_into(self, builder: ManifestBuilder) -> None:
        manifest = load_manifest(self._path)
        vehicle = manifest.vehicle

        builder.set("model_code", vehicle.msc.model_code, "manifest")
        builder.set("spec_code", vehicle.msc.spec_code, "manifest")
        builder.set("model_year", vehicle.model_year, "manifest")
        builder.set("market", vehicle.market, "manifest")
        builder.set("trim", vehicle.trim, "manifest")
        builder.set("colour", vehicle.colour, "manifest")

        for option in vehicle.options:
            builder.add_option(option)