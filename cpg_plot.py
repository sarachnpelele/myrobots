import numpy as np
import matplotlib.pyplot as plt

#Loading the file from one simulation
data = np.loadtxt("cpg_signal_0.txt")  

#Plotting the signal
plt.plot(data[::10])
plt.title("CPG Signal (Sin Wave)")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.grid(True)
plt.show()