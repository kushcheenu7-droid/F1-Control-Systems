import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 10, 1000)

# System parameters
tau = 1.5   # time constant
K = 1.0     # gain

# First-order step response
y = K * (1 - np.exp(-t / tau))

plt.figure()
plt.plot(t, y, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.title("First Order System Step Response")
plt.grid(True)
plt.show()
