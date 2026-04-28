import numpy as np
import matplotlib.pyplot as plt

A = np.load("fitness_A.npy")
B = np.load("fitness_B.npy")

mA = np.mean(A, axis=0)
sA = np.std(A, axis=0)

mB = np.mean(B, axis=0)
sB = np.std(B, axis=0)

x = range(len(mA))

plt.plot(x, mA, linewidth=3, label="A Low Frequency")
plt.plot(x, mB, linewidth=3, label="B High Frequency")

plt.fill_between(x, mA-sA, mA+sA, alpha=0.2)
plt.fill_between(x, mB-sB, mB+sB, alpha=0.2)

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("Preliminary A/B Test")
plt.legend()
plt.show()