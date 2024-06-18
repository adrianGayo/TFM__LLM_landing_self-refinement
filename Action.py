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
    action = 0
    
    # Normalize the angle
    angle = normalize_angle(angle)

    # Attempt to stabilize the spacecraft's orientation first
    if abs(angle) > 0.1:
        if angle > 0:
            action = 1
        else:
            action = 3
    
    # If orientation is stabilized, control the horizontal velocity
    elif abs(X_v) > 0.1:
        if X_v > 0:
            action = 1
        else:
            action = 3
    
    # If both orientation and horizontal velocity are controlled, manage descent with center engine
    elif Y_v < -0.1:
        action = 2
    elif Y_v > 0.1:
        action = 0
    
    # Fine adjustments to make smoother landing when close to the ground
    if Y < 0.1 and abs(X_v) < 0.1 and abs(Y_v) < 0.1 and abs(angle) < 0.1:
        action = 0

    return action
