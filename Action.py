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
    X_position, Y_position, X_velocity, Y_velocity, Angle, Angular_velocity, Left_contact, Right_contact = observation
    if abs(Angle) > 0.1:
        if Angle < 0:
            return 1
        else:
            return 3
    elif abs(X_velocity) > 0.2:
        if X_velocity < 0:
            return 3
        else:
            return 1
    elif Y_velocity < -0.3 or Y_position > 0.2:
        return 2
    else:
        return 0
