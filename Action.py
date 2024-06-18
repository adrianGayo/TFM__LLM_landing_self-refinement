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
    # Unpack the state vector for easier comprehension
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # If contact sensors are active, no action is required.
    if left_contact or right_contact:
        return 0
    
    # Stabilize angle first
    if angle < -0.1:
        return 1  # Push left engine to rotate right
    elif angle > 0.1:
        return 3  # Push right engine to rotate left
    
    # Control vertical speed
    if y_vel < -0.5:
        return 2  # Push both engines (upwards) to slow descent
    
    # Control horizontal position and speed
    if x_vel < -0.5:
        return 3  # Push right engine to move left
    elif x_vel > 0.5:
        return 1  # Push left engine to move right
    
    # If everything is stable, keep engines off
    return 0