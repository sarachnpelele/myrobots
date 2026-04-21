from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import pybullet as p
import os
import constants as c
import numpy as np

class ROBOT:
    def __init__(self, solutionID) -> None:
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.solutionID = solutionID
        self.x = 0.1

    def Prepare_To_Sense(self):
        self.sensors = {}

        # store each link and its sensor in self.sensors dict
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, it):
        # loop through dict and run GetValue method on each sensor
        for s in self.sensors:
            self.sensors[s].Get_Value(it)

        #CPG
        #Overwriting the BackLowerLeg sensor
        cpg_value = np.sin(self.x * it)
        self.sensors["BackLowerLeg"].values[it] = cpg_value
        
        #Logging the signal
        if not hasattr(self, "cpg_log"):
            self.cpg_log = []

        self.cpg_log.append(cpg_value)

    def Think(self,it):
        self.nn.Update(it, self.x)
        #self.nn.Print()

    def Prepare_To_Act(self):
        self.motors = {}

        # store each link and its sensor in self.sensors dict
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, it, robotId):

        for neuronName in self.nn.Get_Neuron_Names():

            if self.nn.Is_Motor_Neuron(neuronName):

                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("ascii")

                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(c.motorJointRange * desiredAngle, robotId)
        
    def Get_Fitness(self, robotId):
        basePositionAndOrientation = p.getBasePositionAndOrientation(robotId)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = xPosition = basePosition[0]
        
        
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("rename tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")

        #Saving the CPG signal to a file
        np.savetxt("cpg_signal_" + str(self.solutionID) + ".txt", self.cpg_log)
        #exit()
