from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mazdavp.manifest import MSC, Vehicle, VehicleManifest


class ManifestConflictError(Exception):
    """Raised when two different values are assigned to the same field."""


@dataclass(slots=True)
class Assignment:
    value: Any
    source: str


class ManifestBuilder:
    """
    Collects vehicle information from one or more importers and
    builds a VehicleManifest.
    """

    def __init__(self) -> None:
        self._fields: dict[str, Assignment] = {}
        self._options: list[str] = []

    def set(self, field: str, value: Any, source: str = "unknown") -> None:
        """
        Assign a field.

        If the field already has a different value,
        a ManifestConflictError is raised.
        """

        current = self._fields.get(field)

        if current is None:
            self._fields[field] = Assignment(value, source)
            return

        if current.value != value:
            raise ManifestConflictError(
                f"{field}: '{current.value}' ({current.source}) "
                f"conflicts with '{value}' ({source})"
            )

    def add_option(self, option: str) -> None:
        if option not in self._options:
            self._options.append(option)

    def get(self, field: str, default=None):
        assignment = self._fields.get(field)
        return default if assignment is None else assignment.value

    def build(self) -> VehicleManifest:

        msc = MSC(
            self.get("model_code"),
            self.get("spec_code"),
        )

        vehicle = Vehicle(
            msc=msc,
            model_year=self.get("model_year"),
            market=self.get("market"),
            trim=self.get("trim"),
            colour=self.get("colour"),
            options=self._options,
        )

        return VehicleManifest(vehicle)