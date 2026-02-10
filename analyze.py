import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

plt.plot(backLegSensorValues, label="Back Leg", linewidth=2)
plt.plot(frontLegSensorValues, label="Front Leg", lw= 0.8)
plt.legend()
plt.show()

print(backLegSensorValues)
print(frontLegSensorValues)