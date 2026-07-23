from mazdavp.pipeline import Pipeline
from mazdavp.pipeline.import_source import ImportSource


class TestImporter(ImportSource):
    def import_into(self, builder):
        builder.set("model_code", "ABCD", "test")
        builder.set("spec_code", "123", "test")
        builder.set("model_year", "2026", "test")
        builder.set("market", "EU", "test")
        builder.set("trim", "Homura", "test")
        builder.set("colour", "Soul Red", "test")

        builder.add_option("PK1")
        builder.add_option("SUN")


pipeline = Pipeline()

pipeline.import_source(TestImporter())

manifest = pipeline.build()

assert manifest.vehicle.msc.value == "ABCD123"
assert manifest.vehicle.model_year == "2026"
assert manifest.vehicle.market == "EU"
assert manifest.vehicle.trim == "Homura"
assert manifest.vehicle.colour == "Soul Red"
assert manifest.vehicle.options == ["PK1", "SUN"]

print("ImportSource test passed.")