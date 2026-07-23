from __future__ import annotations

from abc import ABC, abstractmethod

from mazdavp.builder import ManifestBuilder


class ImportSource(ABC):
    """
    Base class for any source that contributes vehicle data
    to a ManifestBuilder.
    """

    @abstractmethod
    def import_into(self, builder: ManifestBuilder) -> None:
        """
        Populate the supplied ManifestBuilder.

        Implementations should call builder.set() and
        builder.add_option() as appropriate.
        """
        raise NotImplementedError