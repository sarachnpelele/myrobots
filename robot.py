from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import pybullet as p
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID) -> None:
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.solutionID = solutionID

    def Prepare_To_Sense(self):
        self.sensors = {}

        # store each link and its sensor in self.sensors dict
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, it):
        # loop through dict and run GetValue method on each sensor
        for s in self.sensors:
            self.sensors[s].Get_Value(it)

    def Think(self):
        self.nn.Update()
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
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = xPosition = basePosition[0]
        
        
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("rename tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")

        #print("xcoord: ", xCoordinateOfLinkZero)
        exit()
