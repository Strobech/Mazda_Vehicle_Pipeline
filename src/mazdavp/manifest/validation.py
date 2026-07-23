from dataclasses import dataclass, field

@dataclass
class ValidationResult:
    errors:list[str]=field(default_factory=list)
    warnings:list[str]=field(default_factory=list)

    @property
    def valid(self):
        return not self.errors
