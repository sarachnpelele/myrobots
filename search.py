import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np
import constants as c

"""for i in range(5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
"""
"""
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
"""

# A: lower frequency
c.frequency = 0.01
phcA = PARALLEL_HILL_CLIMBER()
phcA.Evolve()

np.savetxt("fitness_A.txt", phcA.fitnessMatrix)
np.save("fitness_A.npy", phcA.fitnessMatrix)

print("A variant saved.")
# B: higher frequency
c.frequency = 0.1
phcB = PARALLEL_HILL_CLIMBER()
phcB.Evolve()

np.savetxt("fitness_B.txt", phcB.fitnessMatrix)
np.save("fitness_B.npy", phcB.fitnessMatrix)

print("B variant saved.")
print("A/B testing data saved.")