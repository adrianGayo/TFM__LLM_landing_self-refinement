import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    if right_contact or left_contact:
        return 0

    # Reduce vertical speed if falling too fast
    if y_vel < -0.5:
        return 2
    
    # Align horizontally to the landing zone
    if x_pos > 0.1:
        return 1
    elif x_pos < -0.1:
        return 3
    
    # Correct the angle to keep the spacecraft upright
    if angle > 0.1:
        return 1
    elif angle < -0.1:
        return 3
    
    # Reduce angular velocity if rotating too much
    if ang_vel > 0.2:
        return 1
    elif ang_vel < -0.2:
        return 3

    # Switch off engines if relatively stable
    return 0
