import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy 
from math import pi
import random
import constants as c
from sensor import SENSOR
from motor import MOTOR
class ROBOT:

    def __init__(self):
        pass
    
    def Prepare_To_Sense(self):

        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, i):
        for s in self.sensors:
            self.sensors[s].Get_Value(i)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,i,robotId):
        for m in self.motors:
            self.motors[m].Set_Value(i, robotId)