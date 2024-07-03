import numpy as np


def act(observation):
    X_pos, Y_pos, X_vel, Y_vel, angle, ang_vel, left_contact, right_contact = observation

    if left_contact == 1 and right_contact == 1:
        # Landed successfully
        return 0

    # Priority: Control Horizontal Movement
    if abs(X_pos) > 0.1 or abs(X_vel) > 0.1:
        if X_pos > 0 or X_vel > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine

    # Priority: Control Vertical Movement
    if Y_vel < -0.5:
        return 2  # Push both engines (upwards)

    # Priority: Control Angle
    if abs(angle) > 0.1 or abs(ang_vel) > 0.1:
        if angle > 0 or ang_vel > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine

    # If all conditions optimal, freeze actions
    return 0