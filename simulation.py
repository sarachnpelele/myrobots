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

        self.world = WORLD()
        self.robot = ROBOT()

        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        
        p.setGravity(0,0,c.gravity)
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(c.iterations):
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i,self.robotId)
            time.sleep(c.sleep_time)
    
    def __del__(self):

        p.disconnect()        