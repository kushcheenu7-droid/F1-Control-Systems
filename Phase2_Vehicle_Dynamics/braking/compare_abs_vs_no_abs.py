import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(0, 6, 1000)
dt = t[1] - t[0]

# Parameters
m = 800
mu = 1.2
g = 9.81
k_df = 3.0
slip_opt = 0.15
K_abs = 5.0

# Initial conditions
v0 = 80 / 3.6

v_no_abs = np.zeros_like(t)
v_abs = np.zeros_like(t)
v_wheel = np.zeros_like(t)

v_no_abs[0] = v0
v_abs[0] = v0
v_wheel[0] = v0

for i in range(1, len(t)):
    # Common downforce
    downforce = k_df * v_abs[i-1]**2
    normal_force = m * g + downforce

    # No ABS (full braking)
    a_no_abs = mu * normal_force / m
    v_no_abs[i] = max(v_no_abs[i-1] - a_no_abs * dt, 0)

    # ABS braking
    slip = max((v_abs[i-1] - v_wheel[i-1]) / max(v_abs[i-1], 0.1), 0)
    brake_factor = np.clip(K_abs * (slip_opt - slip), 0, mu)
    a_abs = brake_factor * normal_force / m

    v_abs[i] = max(v_abs[i-1] - a_abs * dt, 0)
    v_wheel[i] = max(v_wheel[i-1] - 1.2 * a_abs * dt, 0)

plt.figure()
plt.plot(t, v_no_abs, label="No ABS", linewidth=2)
plt.plot(t, v_abs, label="With ABS", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Braking Comparison: ABS vs No ABS")
plt.legend()
plt.grid(True)
plt.show()
