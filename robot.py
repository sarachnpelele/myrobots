"""
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import pybullet as p
import os
import constants as c
import numpy as np
import constants as c

class ROBOT:
    def __init__(self, solutionID) -> None:
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.solutionID = solutionID
        self.x = c.frequency

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
        #np.savetxt("cpg_signal_" + str(self.solutionID) + ".txt", self.cpg_log)
        #exit()
"""
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
        self.x = c.frequency
        # Initialize a variable to store the starting X position
        self.initialX = None 

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, it):
        # CAPTURE INITIAL POSITION: 
        # We do this at the very first step to know where we started.
        if it == 0:
            basePositionAndOrientation = p.getBasePositionAndOrientation(1) # robotId is usually 1
            self.initialX = basePositionAndOrientation[0][0]

        for s in self.sensors:
            self.sensors[s].Get_Value(it)

        # CPG Logic
        cpg_value = np.sin(self.x * it)
        if "BackLowerLeg" in self.sensors:
            self.sensors["BackLowerLeg"].values[it] = cpg_value

    def Think(self, it):
        self.nn.Update(it, self.x)

    def Prepare_To_Act(self):
        self.motors = {}
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
        currentX = basePosition[0]
        
        # CALCULATE DISPLACEMENT:
        # Distance = current position - starting position
        displacement = currentX - self.initialX
        
        # Use a context manager to handle file closing automatically
        with open("tmp" + str(self.solutionID) + ".txt", "w") as f:
            f.write(str(displacement))
        
        # Windows command to rename
        os.system("rename tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")