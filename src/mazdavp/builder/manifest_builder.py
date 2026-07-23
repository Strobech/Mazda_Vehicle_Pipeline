from mazdavp.manifest import MSC, Vehicle, VehicleManifest

class ManifestBuilder:
    def __init__(self):
        self._data = {
            "model_code": None,
            "spec_code": None,
            "model_year": None,
            "market": None,
            "trim": None,
            "colour": None,
            "options": [],
        }

    def set_model_code(self, value): self._data["model_code"] = value
    def set_spec_code(self, value): self._data["spec_code"] = value
    def set_model_year(self, value): self._data["model_year"] = value
    def set_market(self, value): self._data["market"] = value
    def set_trim(self, value): self._data["trim"] = value
    def set_colour(self, value): self._data["colour"] = value

    def add_option(self, option):
        self._data["options"].append(option)

    def build(self):
        msc = MSC(self._data["model_code"], self._data["spec_code"])
        vehicle = Vehicle(
            msc=msc,
            model_year=self._data["model_year"],
            market=self._data["market"],
            trim=self._data["trim"],
            colour=self._data["colour"],
            options=self._data["options"],
        )
        return VehicleManifest(vehicle)
