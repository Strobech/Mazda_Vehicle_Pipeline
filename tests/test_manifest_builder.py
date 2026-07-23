from mazdavp.builder import ManifestBuilder

b = ManifestBuilder()
b.set_model_code("ABCD")
b.set_spec_code("123")
b.set_model_year("2026")
b.set_market("EU")
b.set_trim("Homura")
b.set_colour("Soul Red")
b.add_option("PK1")

manifest = b.build()

assert manifest.vehicle.msc.value == "ABCD123"
assert manifest.vehicle.options == ["PK1"]
print("ManifestBuilder test passed")
