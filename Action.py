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
    # Unpack the observation values
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0

    # Stabilizing the ship: reduce horizontal speed and angle
    if abs(angle) > 0.1 or abs(ang_vel) > 0.1:
        if angle > 0:
            action = 1  # Push left engine
        else:
            action = 3  # Push right engine
    elif abs(x_vel) > 0.5:
        if x_vel > 0:
            action = 1  # Push left engine to counter rightwards movement
        else:
            action = 3  # Push right engine to counter leftwards movement
    else:
        # Control descent speed
        if y_vel < -0.3:
            action = 2
        if abs(y_vel) < 0.1 and not left_contact and not right_contact:
            action = 2

    return action
