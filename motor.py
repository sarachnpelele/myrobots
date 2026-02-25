import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy 
from math import pi
import random
import constants as c
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.iterations)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.ampBackLeg
        self.frequency = c.freqBackLeg
        self.offset = c.phaseOffsetBackLeg
        self.iterations = c.iterations

        if self.jointName == b'Torso_BackLeg':
            self.frequency = c.freqBackLeg/2
        
        firstVector = numpy.linspace(0, numpy.pi * 2, self.iterations)
        
        for ind, each in enumerate(firstVector):
            self.motorValues[ind] = self.amplitude * \
                numpy.sin(self.frequency * each + self.offset)
    
    def Set_Value(self, i, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[i],
            maxForce=c.max_force)
        
    def Save_Value(self):
        dst = 'data/' + self.jointName + 'Motor'
        numpy.save(dst, self.motorValues)