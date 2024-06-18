import random

# This helper function normalizes the angle between -pi and pi
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

    # Stabilize large angles first
    if abs(angle) > 0.1:
        if angle > 0:
            return 3  # Push right engine to rotate counterclockwise
        else:
            return 1  # Push left engine to rotate clockwise

    # Control horizontal velocity if angle is stabilized and horizontal speed is high
    if abs(X_v) > 0.5:
        if X_v > 0:
            return 1  # Push left to reduce positive horizontal velocity
        else:
            return 3  # Push right to reduce negative horizontal velocity

    # Use main engine to control vertical speed if the descent is high
    if Y_v < -0.5:
        return 2  # Push up to reduce falling speed

    # Fine adjustments when close to the ground
    if Y < 0.2 and abs(X_v) < 0.1 and abs(Y_v) < 0.1 and abs(angle) < 0.1:
        return 0  # Switch off engines to ensure smooth landing

    if abs(X_v) < 0.1 and abs(Y_v) < 0.1 and abs(angle) < 0.1:
        return 0  # Switch off engines as default action to save fuel and points

    return 2  # Default action: Push both engines for controlled descent
