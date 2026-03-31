import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random as r
import time
import constants as c
tester = True

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        
    def Start_Simulation(self, directOrGUI):
        if tester == False or self.myID == 0:
            self.Create_Body()        
            self.Create_World()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(1/100)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()

        os.system("del fitness"+str(self.myID)+".txt")

    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube( name="Block",pos=[-3, 3, 0.5],size=[1, 1, 1] )
        pyrosim.End()



    def Create_Body(self):
 


        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()
        
    def Create_Brain(self):
 
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = c.numMotorNeurons, linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = c.numSensorNeurons , weight = -1.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = c.numSensorNeurons , weight = -1.5)
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = -1.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.5 )

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons, weight =  self.weights[currentRow][currentColumn] )
    
        pyrosim.End()
        

    def Mutate(self):
        randomRow = r.randint(0,2)
        randomColumn = r.randint(0,1)
        self.weights[randomRow][randomColumn] = r.random() * 2 - 1 

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID