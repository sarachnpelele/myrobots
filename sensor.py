import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy 
from math import pi
import random
import constants as c
class SENSOR:

    def __init__(self, linkName):
        
        self.linkName = linkName
        self.values = numpy.zeros(c.iterations)
        
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Value(self):
        dst = 'data/' + self.linkName + 'Sensor'
        numpy.save(dst, self.values)