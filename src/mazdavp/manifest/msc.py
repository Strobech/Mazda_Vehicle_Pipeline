from dataclasses import dataclass

@dataclass(frozen=True)
class MSC:
    model_code:str
    spec_code:str

    def __post_init__(self):
        if len(self.model_code)!=4 or self.model_code!=self.model_code.upper():
            raise ValueError("ModelCode must be 4 uppercase characters.")
        if len(self.spec_code)!=3 or self.spec_code!=self.spec_code.upper():
            raise ValueError("SpecCode must be 3 uppercase characters.")

    @property
    def value(self)->str:
        return self.model_code+self.spec_code
