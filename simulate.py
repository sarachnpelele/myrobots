import constants as c
from robot import ROBOT
from simulation import SIMULATION
from world import WORLD
import sys


directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()

world = WORLD()
robot = ROBOT(solutionID)

simulation.Get_Fitness()
