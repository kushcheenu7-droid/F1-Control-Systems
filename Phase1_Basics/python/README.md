# Python – Control System Simulations

This folder contains Python-based simulations developed to understand
and apply fundamental control system concepts to physical systems.

The focus is on **time-domain analysis**, **system dynamics**, and
connecting mathematical models with real-world engineering behavior.

---

## Implemented Models

### 1. First-Order System
File: `first_order_system.py`

- Simulates step response of a first-order system
- Parameters:
  - `tau` – time constant (system speed)
  - `K` – system gain
- Concepts studied:
  - Transient response
  - Rise time
  - Physical interpretation of system parameters

This model represents dynamics seen in actuators, sensors, and basic
vehicle subsystems.

---

### 2. Second-Order System
File: `second_order_system.py`

- Simulates underdamped second-order step response
- Parameters:
  - `wn` – natural frequency
  - `zeta` – damping ratio
- Concepts studied:
  - Oscillatory behavior
  - Damping effects
  - Stability and transient performance

This model is relevant to suspension systems, steering dynamics, and
attitude control systems.

---

## Tools & Libraries
- Python
- NumPy
- Matplotlib

---

## Learning Outcome
- Translate control theory into executable simulations
- Visualize and interpret dynamic system behavior
- Build foundations for vehicle dynamics and control-oriented modeling
