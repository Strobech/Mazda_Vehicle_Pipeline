from mazdavp.manifest import MSC, Vehicle, VehicleManifest
from mazdavp.validation import ManifestValidator

vehicle = Vehicle(
    msc=MSC("ABCD","123"),
    model_year="2026",
    market="EU",
    trim="Homura",
    colour="Soul Red"
)

manifest = VehicleManifest(vehicle)

report = ManifestValidator().validate(manifest)

assert report.valid
print("Validation engine test passed")
