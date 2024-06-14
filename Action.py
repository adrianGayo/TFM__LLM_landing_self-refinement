import random

def act(observation):
    '''
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
    '''
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation
    # Stabilize angular velocity first
    if angular_velocity > 0.1:
        return 1  # apply left engine
    elif angular_velocity < -0.1:
        return 3  # apply right engine
    # Stabilize angle
    if angle > 0.1:
        return 1  # apply left engine
    elif angle < -0.1:
        return 3  # apply right engine
    # Stabilize horizontal velocity towards zero
    if vx > 0.1:
        return 1  # apply left engine
    elif vx < -0.1:
        return 3  # apply right engine
    # Ensure y velocity is safe for landing
    if vy < -1.0:
        return 2  # apply both engines upwards
    # Safe to turn off engines
    return 0