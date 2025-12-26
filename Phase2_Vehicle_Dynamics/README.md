# Vehicle Braking Dynamics

This module models longitudinal vehicle braking dynamics with a focus on
motorsport and high-performance automotive applications.

The goal is to understand how physical parameters and external forces
affect braking performance and stopping distance.

---

## Baseline Model (No Aerodynamics)

File: `braking_model.py`

### Assumptions
- Flat road surface
- Constant tire–road friction coefficient
- No aerodynamic downforce
- Straight-line braking

### Parameters
- Vehicle mass
- Initial velocity
- Tire–road friction coefficient

### Concepts Studied
- Friction-limited braking
- Velocity decay during braking
- Stopping distance estimation

---

## Relevance
This model represents the baseline braking physics used before adding
aerodynamic and control effects such as downforce and ABS logic.
