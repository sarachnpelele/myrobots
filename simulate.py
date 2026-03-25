import constants as c
from robot import ROBOT
from simulation import SIMULATION
from world import WORLD
import sys
import os


directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()

world = WORLD()
robot = ROBOT(solutionID)

os.system("del brain"+str(solutionID)+".nndf")

simulation.Get_Fitness()
