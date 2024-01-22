from rainnet import rainnet

model = rainnet()
model.load_weights("rainnet_weights.h5")
model.summary()