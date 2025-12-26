import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 10, 1000)

# Second-order system parameters
wn = 2.0        # natural frequency
zeta = 0.3      # damping ratio

# Step response
y = 1 - np.exp(-zeta*wn*t) * (
    np.cos(wn*np.sqrt(1 - zeta**2)*t) +
    (zeta/np.sqrt(1 - zeta**2)) *
    np.sin(wn*np.sqrt(1 - zeta**2)*t)
)

plt.figure()
plt.plot(t, y, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.title("Second Order System Step Response")
plt.grid(True)
plt.show()
