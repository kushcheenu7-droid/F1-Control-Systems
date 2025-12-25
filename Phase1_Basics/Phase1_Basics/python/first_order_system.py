import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 10, 1000)

# First-order system parameters
tau = 1.5   # time constant
K = 1.0     # system gain

# Step response of first-order system
y = K * (1 - np.exp(-t / tau))

# Plot
plt.figure()
plt.plot(t, y, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.title("First Order System Step Response")
plt.grid(True)
plt.show()
