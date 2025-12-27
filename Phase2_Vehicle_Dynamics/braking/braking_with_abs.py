import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 800          # mass (kg)
mu = 1.2         # friction coefficient
g = 9.81
k_df = 3.0       # downforce coefficient
slip_opt = 0.15  # optimal slip ratio

# Time
t = np.linspace(0, 6, 1000)
dt = t[1] - t[0]

# Initial conditions
v = np.zeros_like(t)
v_wheel = np.zeros_like(t)
slip = np.zeros_like(t)

v[0] = 80 / 3.6
v_wheel[0] = v[0]

# ABS control gain
K_abs = 5.0

for i in range(1, len(t)):
    # Aerodynamic downforce
    downforce = k_df * v[i-1]**2
    normal_force = m * g + downforce

    # Slip calculation
    slip[i-1] = max((v[i-1] - v_wheel[i-1]) / max(v[i-1], 0.1), 0)

    # ABS controller (simple proportional control)
    brake_factor = K_abs * (slip_opt - slip[i-1])
    brake_factor = np.clip(brake_factor, 0, mu)

    # Vehicle deceleration
    a = brake_factor * normal_force / m
    v[i] = max(v[i-1] - a * dt, 0)

    # Wheel dynamics (simplified)
    v_wheel[i] = max(v_wheel[i-1] - 1.2 * a * dt, 0)

slip[-1] = slip[-2]

# Plot results
plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(t, v, label="Vehicle Speed")
plt.plot(t, v_wheel, label="Wheel Speed")
plt.ylabel("Speed (m/s)")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, slip, label="Slip Ratio")
plt.axhline(slip_opt, color='r', linestyle='--', label="Optimal Slip")
plt.xlabel("Time (s)")
plt.ylabel("Slip")
plt.legend()
plt.grid(True)

plt.show()
