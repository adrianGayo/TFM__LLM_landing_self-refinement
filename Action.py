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
    """
    The function that codifies the action to be taken in each instant of time.

    Args:
        observation (numpy.array):
            "description": "The state of the environment after the action is taken.",
            "positions": { 
                "0": "X position",
                "1": "Y position",
                "2": "X velocity",
                "3": "Y velocity",
                "4": "Angle",
                "5": "Angular velocity",
                "6": "Left contact sensor",
                "7": "Right contact sensor"
            },
            "min_values": [-1.5, -1.5, -5.0, -5.0, -3.14, -5.0, 0, 0],
            "max_values": [1.5, 1.5, 5.0, 5.0, 3.14, 5.0, 1, 1]

    Returns:
        Integer  : The action to be taken.
        "options": {
                '0' : "Switch off engines",
                '1' : "Push left engine",
                '2' : "Push both engines (upwards)",
                '3' : "Push right engine"
            }
    """

    X, Y, X_v, Y_v, angle, ang_v, left_contact, right_contact = observation

    # Normalize the angle
    angle = normalize_angle(angle)

    # Stabilize angle first
    if abs(angle) > 0.1:
        if angle > 0:
            return 3  # Push right engine to rotate counterclockwise
        else:
            return 1  # Push left engine to rotate clockwise

    # Control horizontal velocity if angle is stabilized
    if abs(X_v) > 0.1:
        if X_v > 0:
            return 1  # Push left to reduce positive horizontal velocity
        else:
            return 3  # Push right to reduce negative horizontal velocity

    # Only use main engine if vertical speed is too high or near ground
    if abs(Y_v) > 0.1 and Y > 0.2:
        return 2  # Push up to reduce falling speed

    # Fine adjustments when close to the ground
    if Y < 0.1 and abs(X_v) < 0.1 and abs(Y_v) < 0.1 and abs(angle) < 0.1:
        return 0  # Switch off engines to ensure smooth landing

    return 0  # Default action: Switch off engines
