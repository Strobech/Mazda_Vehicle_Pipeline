from mazdavp.manifest import VehicleManifest, Option

m=VehicleManifest(
    model="MX-5",
    trim="Homura",
    colour="Soul Red",
    options=[Option("PK1","Example")]
)

d=m.to_dict()
m2=VehicleManifest.from_dict(d)
assert m2.model=="MX-5"
assert len(m2.options)==1
print("Manifest test passed")
