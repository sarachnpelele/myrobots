import constants as c
from robot import ROBOT
from simulation import SIMULATION
from world import WORLD
import sys


directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)

simulation.Run()

world = WORLD()
robot = ROBOT()

simulation.Get_Fitness()
