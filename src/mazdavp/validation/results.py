from dataclasses import dataclass, field

@dataclass
class Issue:
    level:str
    field:str
    message:str

@dataclass
class ValidationReport:
    issues:list[Issue]=field(default_factory=list)

    def add_error(self, field, message):
        self.issues.append(Issue("ERROR", field, message))

    def add_warning(self, field, message):
        self.issues.append(Issue("WARNING", field, message))

    @property
    def valid(self):
        return not any(i.level=="ERROR" for i in self.issues)
