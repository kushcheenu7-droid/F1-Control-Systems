import numpy as np
import matplotlib.pyplot as plt

# Vehicle parameters
m = 800          # mass (kg)
mu = 1.2         # tire-road friction coefficient
g = 9.81         # gravity (m/s^2)

# Aerodynamic parameters
k_df = 3.0       # downforce coefficient (simplified)

# Initial conditions
v0 = 80 / 3.6    # initial speed (m/s)
t = np.linspace(0, 6, 1000)
dt = t[1] - t[0]

# Velocity arrays
v_no_aero = np.zeros_like(t)
v_aero = np.zeros_like(t)

v_no_aero[0] = v0
v_aero[0] = v0

# Simulation loop
for i in range(1, len(t)):
    # No aerodynamic downforce
    a_no = mu * g
    v_no_aero[i] = max(v_no_aero[i-1] - a_no * dt, 0)

    # With aerodynamic downforce
    downforce = k_df * v_aero[i-1]**2
    normal_force = m * g + downforce
    a_aero = mu * normal_force / m
    v_aero[i] = max(v_aero[i-1] - a_aero * dt, 0)

# Plot comparison
plt.figure()
plt.plot(t, v_no_aero, label="No Aerodynamics", linewidth=2)
plt.plot(t, v_aero, label="With Aerodynamics", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Effect of Aerodynamic Downforce on Braking")
plt.grid(True)
plt.legend()
plt.show()
