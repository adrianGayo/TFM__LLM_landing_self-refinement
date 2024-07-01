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
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation

    # Stabilizing horizontal position
    if abs(x) > 0.1:
        if x > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine

    # Stabilizing angular position
    if abs(angle) > 0.1:
        if angle > 0:
            return 1  # Push left engine to counteract right tilt
        else:
            return 3  # Push right engine to counteract left tilt

    # Stabilizing horizontal velocity
    if abs(vx) > 0.2:
        if vx > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine

    # Reduce vertical velocity softly
    if vy < -0.5:
        return 2  # Push both engines upwards

    # Final gentle landing
    if y < 0.1:
        return 2  # Push both engines upwards for gentle touch

    return 0  # Default action: switch off engines
