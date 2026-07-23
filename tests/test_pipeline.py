from mazdavp.pipeline import Pipeline

pipeline = Pipeline()

pipeline.set("model_code", "ABCD", "test")
pipeline.set("spec_code", "123", "test")
pipeline.set("model_year", "2026", "test")
pipeline.set("market", "EU", "test")
pipeline.set("trim", "Homura", "test")
pipeline.set("colour", "Soul Red", "test")

pipeline.add_option("PK1")
pipeline.add_option("SUN")

manifest = pipeline.build()

assert manifest.vehicle.msc.value == "ABCD123"
assert manifest.vehicle.model_year == "2026"
assert manifest.vehicle.market == "EU"
assert manifest.vehicle.trim == "Homura"
assert manifest.vehicle.colour == "Soul Red"
assert manifest.vehicle.options == ["PK1", "SUN"]

print("Pipeline test passed.")