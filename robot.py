import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy 
from math import pi
import random
import constants as c
class ROBOT:

    def __init__(self):

       self.sensors = {}
       self.motors = {}
       self.robotId = p.loadURDF("body.urdf")