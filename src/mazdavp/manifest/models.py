from dataclasses import dataclass, field, asdict
from typing import List

@dataclass
class Option:
    code: str
    description: str = ""

@dataclass
class VehicleManifest:
    model: str
    trim: str
    colour: str
    options: List[Option] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        opts=[Option(**o) for o in data.get("options",[])]
        return cls(
            model=data["model"],
            trim=data["trim"],
            colour=data["colour"],
            options=opts,
        )
