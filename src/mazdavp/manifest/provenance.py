from dataclasses import dataclass
from enum import Enum

class Source(Enum):
    MAYA="maya"
    MEL="mel"
    ORDER_FORM="order_form"
    MANUAL="manual"
    UNKNOWN="unknown"

@dataclass
class Provenance:
    field:str
    source:Source
