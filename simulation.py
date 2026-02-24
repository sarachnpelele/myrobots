import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy 
from math import pi
import random
import constants as c

from world import WORLD
from robot import ROBOT
class SIMULATION:

    def __init__(self):
        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for i in range(c.iterations):
            print(i)
            
            p.stepSimulation()
            #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #pyrosim.Set_Motor_For_Joint(
                #bodyIndex = robotId ,
                #jointName = b'Torso_BackLeg',
                #controlMode = p.POSITION_CONTROL,
                #targetPosition = targetAnglesBackLeg[i],
                #maxForce = c.max_force)
            #pyrosim.Set_Motor_For_Joint(
                #bodyIndex = robotId ,
                #jointName = b'Torso_FrontLeg',
                #controlMode = p.POSITION_CONTROL,
                #targetPosition = targetAnglesFrontLeg[i],
                #maxForce = c.max_force)
            time.sleep(c.sleep_time)
            