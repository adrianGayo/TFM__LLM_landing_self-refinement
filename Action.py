import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Safety check: if landed, turn off engines
    if left_contact or right_contact:
        return 0

    # Manage vertical velocity first
    if y_vel < -0.5:
        return 2
    
    # Stabilize horizontal velocity
    if np.abs(x_vel) > 0.2:
        if x_vel > 0:
            return 1
        else:
            return 3

    # Neutralize rotation if angle is not zero
    if np.abs(angle) > 0.1:
        if angle > 0:
            return 1
        else:
            return 3

    # If all conditions are met, keep engines off
    return 0