from mazdavp.manifest import *

msc=MSC("ABCD","123")
v=Vehicle(msc,"2026","EU","Homura","Soul Red")
m=VehicleManifest(v)
assert m.vehicle.msc.value=="ABCD123"
assert m.validation.valid
print("Engineering manifest tests passed")
