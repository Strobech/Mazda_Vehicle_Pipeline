from mazdavp.builder import ManifestBuilder

builder = ManifestBuilder()

try:
    builder.set("modelcode", "ABCD", "test")
except ValueError as exc:
    assert str(exc) == "Unknown field: modelcode"
else:
    raise AssertionError("Expected ValueError")

print("Builder field validation test passed.")