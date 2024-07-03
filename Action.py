import numpy as np


def act(observation):
    X_pos, Y_pos, X_vel, Y_vel, angle, ang_vel, left_contact, right_contact = observation

    if left_contact == 1 and right_contact == 1:
        # Landed successfully
        return 0

    # Adjust horizontal movement
    if X_pos > 0.1 or X_vel > 0.1:
        return 1  # Push left engine
    if X_pos < -0.1 or X_vel < -0.1:
        return 3  # Push right engine

    # Maintain vertical control
    if Y_vel < -0.3 or (Y_pos > 0.1 and Y_vel < -0.1):
        return 2  # Push both engines (upwards)

    # Adjust angle during descent
    if angle > 0.1 or ang_vel > 0.1:
        return 1  # Push left engine
    if angle < -0.1 or ang_vel < -0.1:
        return 3  # Push right engine

    # If all conditions are optimal, do nothing
    return 0