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
    x_pos = observation[0]
    y_pos = observation[1]
    x_vel = observation[2]
    y_vel = observation[3]
    angle = observation[4]
    angular_vel = observation[5]

    # Stabilization
    if abs(angle) > 0.1:
        return 1 if angle < 0 else 3  # Fire left or right engine to counteract angle

    # Slowing descent
    if y_vel < -0.5:
        return 2  # Fire both engines to control descent

    # Centering horizontally
    if abs(x_pos) > 0.1:
        return 1 if x_pos > 0 else 3  # Fire engines to move towards the center

    # If everything is stable, do nothing or minor adjustments
    if abs(angular_vel) > 0.1:
        return 1 if angular_vel > 0 else 3

    return 0