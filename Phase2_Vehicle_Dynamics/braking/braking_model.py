import numpy as np
import matplotlib.pyplot as plt

# Vehicle parameters
m = 800        # mass (kg)
mu = 1.2       # tire-road friction coefficient
g = 9.81       # gravity (m/s^2)

# Initial conditions
v0 = 80 / 3.6  # initial speed (m/s)
t = np.linspace(0, 6, 1000)

# Braking acceleration
a = mu * g

# Velocity and distance
v = v0 - a * t
v[v < 0] = 0

x = np.cumsum(v) * (t[1] - t[0])

# Plot
plt.figure()
plt.plot(t, v, label="Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Vehicle Braking Dynamics")
plt.grid(True)
plt.legend()
plt.show()
