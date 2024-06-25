import numpy as np


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
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_cont, right_cont = observation
    
    # Stabilize angle first if it is too tilted
    if angle < -0.1 or angular_vel < -0.1:  # Tilting too much left or rotating too fast counterclockwise
        return 1
    if angle > 0.1 or angular_vel > 0.1:  # Tilting too much right or rotating too fast clockwise
        return 3

    # Correct horizontal position
    if x_pos < -0.2:  # Too far left
        return 3
    if x_pos > 0.2:  # Too far right
        return 1

    # Use main engine to reduce vertical speed if falling too fast
    if y_vel < -0.3:  # Falling too fast
        return 2

    # If the velocity is small in both directions and the angle is small, turn off engines
    if abs(y_vel) < 0.1 and abs(x_vel) < 0.1 and abs(angle) < 0.1:
        return 0 

    # In other cases do nothing
    return 0