from mazdavp.builder import ManifestBuilder

builder = ManifestBuilder()

builder.set("model_code", "ABCD", "test")
builder.set("spec_code", "123", "test")
builder.set("model_year", "2026", "test")
builder.set("market", "EU", "test")
builder.set("trim", "Homura", "test")
builder.set("colour", "Soul Red", "test")

builder.add_option("PK1")

manifest = builder.build()

assert manifest.vehicle.msc.value == "ABCD123"
assert manifest.vehicle.trim == "Homura"
assert manifest.vehicle.options == ["PK1"]

conflict = ManifestBuilder()

conflict.set("trim", "Homura", "OrderForm")

try:
    conflict.set("trim", "Takumi", "Maya")
    raise AssertionError("Expected ManifestConflictError")
except Exception:
    pass

print("All tests passed.")