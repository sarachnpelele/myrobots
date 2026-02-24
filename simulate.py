import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy 
from math import pi
import random
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,c.gravity)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

# Back Leg
targetAnglesBackLeg = numpy.zeros(c.iterations)
# Front Leg
targetAnglesFrontLeg = numpy.zeros(c.iterations)

backLegSensorValues = numpy.zeros(c.iterations)
frontLegSensorValues = numpy.zeros(c.iterations)

# generate vector of sinusoidally varying values
firstVector = numpy.linspace(0, c.two_pi, c.iterations)
# Back Leg
for ind, each in enumerate(firstVector):
    targetAnglesBackLeg[ind] = c.ampBackLeg * numpy.sin(c.freqBackLeg * each + c.phaseOffsetBackLeg)
# Front Leg
for ind, each in enumerate(firstVector):
    targetAnglesFrontLeg[ind] = c.ampFrontLeg * numpy.sin(c.freqFrontLeg * each + c.phaseOffsetFrontLeg)


for i in range(c.iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId ,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBackLeg[i],
        maxForce = c.max_force)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId ,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFrontLeg[i],
        maxForce = c.max_force)
    time.sleep(c.sleep_time)


#numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
#numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save('data/targetanglesbackleg.npy', targetAnglesBackLeg)
numpy.save('data/targetanglesfrontleg.npy', targetAnglesFrontLeg)

#print("back", backLegSensorValues)
#print("front", frontLegSensorValues)
p.disconnect()
