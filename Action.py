import numpy as np

def act(observation):
    '''
    The function that codifies the action to be taken in each instant of time.

    Args:
        observation (list):
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
    X_pos, Y_pos, X_vel, Y_vel, angle, ang_vel, left_contact, right_contact = observation

    if left_contact == 1 and right_contact == 1:
        # Landed successfully
        return 0
    
    # Adjust horizontal movement
    if X_pos > 0.1 and X_vel > 0.1:
        return 1  # Push left engine
    if X_pos < -0.1 and X_vel < -0.1:
        return 3  # Push right engine
    
    # Maintain vertical control
    if Y_vel < -0.3 or (Y_pos > 0.1 and Y_vel < -0.1):
        return 2  # Push both engines (upwards)
    
    # Adjust angle during descent
    if angle > 0.1 and ang_vel > 0.1:
        return 1  # Push left engine
    if angle < -0.1 and ang_vel < -0.1:
        return 3  # Push right engine
    
    # If all conditions are optimal, do nothing
    return 0