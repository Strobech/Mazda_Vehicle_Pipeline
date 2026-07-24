from enum import StrEnum


class ManifestField(StrEnum):
    MODEL_CODE = "model_code"
    SPEC_CODE = "spec_code"
    MODEL_YEAR = "model_year"
    MARKET = "market"
    TRIM = "trim"
    COLOUR = "colour"


VALID_FIELDS = {field.value for field in ManifestField}