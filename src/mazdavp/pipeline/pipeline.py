from __future__ import annotations

from typing import Any

from mazdavp.builder import ManifestBuilder
from mazdavp.manifest import VehicleManifest

from .import_source import ImportSource


class Pipeline:
    """
    Coordinates the construction of a VehicleManifest.
    """

    def __init__(self) -> None:
        self._builder = ManifestBuilder()

    def set(self, field: str, value: Any, source: str = "unknown") -> None:
        self._builder.set(field, value, source)

    def add_option(self, option: str) -> None:
        self._builder.add_option(option)

    def import_source(self, source: ImportSource) -> None:
        """
        Import vehicle data from an ImportSource.
        """
        source.import_into(self._builder)

    def build(self) -> VehicleManifest:
        return self._builder.build()