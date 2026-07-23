from dataclasses import dataclass, field
from .msc import MSC

@dataclass
class Vehicle:
    msc:MSC
    model_year:str
    market:str
    trim:str
    colour:str
    options:list[str]=field(default_factory=list)
