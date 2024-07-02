import random

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    if (left_contact or right_contact):
        return 0  # touchdown logic with immediate stoppage 

    # Combo descent and drift correction for balancing initial phase
    if abs(x_vel) > 0.2:
        return 1 if x_vel > 0 else 3  # Corrects drift right-left management 

    if y_vel < -0.1 or y_pos > 1.2: 
        return 2  # Ensures safe vertical drop with consistent control 
    elif y_vel > 0.1:
        return 0  # Manages if unintentional lift-off motion detected 

    if abs(angle) > 0.1:  # Ensuring stable bank angles naturally
        return 3 if angle < 0 else 1 # Ensures proper tilt rectification 

    return 0  # Default stabilization focusing gradual normalized touch 

act_filename = "Action.py"
