import numpy
import matplotlib.pyplot as plt

#backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
#frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAnglesBackLeg = numpy.load("./data/targetanglesbackleg.npy")
targetAnglesFrontLeg = numpy.load("./data/targetanglesfrontleg.npy")

#plt.plot(backLegSensorValues, label="Back Leg", linewidth=2)
#plt.plot(frontLegSensorValues, label="Front Leg", lw= 0.8)
plt.plot(targetAnglesBackLeg, label="backLeg Target Angles", linewidth=1.6)
plt.plot(targetAnglesFrontLeg, label="frontLeg Target Angles", lw= 0.8)
plt.legend()
plt.show()

print(backLegSensorValues)
print(frontLegSensorValues)