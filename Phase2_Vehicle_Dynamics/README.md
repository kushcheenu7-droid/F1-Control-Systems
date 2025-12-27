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

## Aerodynamic Braking Effect

File: `braking_with_aero.py`

This model extends baseline braking dynamics by including aerodynamic
downforce proportional to velocity squared.

### Observations
- Increased downforce improves braking capability at high speeds
- Braking performance degrades as speed reduces
- Demonstrates why aerodynamics are critical in motorsport braking

This analysis explains late braking capability in Formula 1 cars.

## ABS-Style Control Logic

File: `braking_with_abs.py`

This model introduces a simplified anti-lock braking system (ABS)
controller using feedback control principles.

### Control Strategy
- Slip ratio is used as the feedback variable
- A proportional controller regulates braking force
- Braking force is limited to avoid wheel lock

### Control Concepts Applied
- Feedback control
- Error computation
- Gain tuning
- Actuator saturation

This model demonstrates how control theory is applied directly in
automotive safety systems.
