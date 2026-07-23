from dataclasses import dataclass, field, asdict
from .vehicle import Vehicle
from .provenance import Provenance
from .validation import ValidationResult

@dataclass
class VehicleManifest:
    vehicle:Vehicle
    provenance:list[Provenance]=field(default_factory=list)
    validation:ValidationResult=field(default_factory=ValidationResult)

    def to_dict(self):
        return asdict(self)
