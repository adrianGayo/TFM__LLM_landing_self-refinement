import random

# This helper function normalizes the angle
import numpy as np

def normalize_angle(angle):
    while angle < -np.pi:
        angle += 2 * np.pi
    while angle > np.pi:
        angle -= 2 * np.pi
    return angle

# Main act function

def act(observation):
    X, Y, X_v, Y_v, angle, ang_v, left_contact, right_contact = observation

    # Normalize the angle
    angle = normalize_angle(angle)

    # Prioritize stabilizing the angle
    if abs(angle) > 0.1:
        if angle > 0:
            return 3  # Push right engine to rotate counterclockwise
        else:
            return 1  # Push left engine to rotate clockwise

    # Control horizontal velocity
    if abs(X_v) > 0.5:
        if X_v > 0:
            return 1  # Push left to reduce positive horizontal velocity
        else:
            return 3  # Push right to reduce negative horizontal velocity

    # Manage descent speed
    if Y_v < -0.5:
        return 2  # Push both engines to reduce falling speed
    elif Y_v > 0.5:
        return 0  # Switch off engines if moving upwards too fast

    # Fine adjustments near the ground
    if Y < 0.2 and abs(X_v) < 0.1 and abs(Y_v) < 0.1 and abs(angle) < 0.1:
        return 0  # Switch off engines to ensure smooth landing

    # If all else fails, default to pushing both engines
    return 2
