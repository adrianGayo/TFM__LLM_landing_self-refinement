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
    '''
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    THRESHOLD_ANGLE = 0.2
    THRESHOLD_VELOCITY_X = 0.3
    THRESHOLD_VELOCITY_Y = -0.5
    HOVER_HEIGHT = 0.5

    if left_contact or right_contact:
        return 3

    if abs(angle) > THRESHOLD_ANGLE:
        if angle > 0:
            return 0
        else:
            return 1

    if abs(x_vel) > THRESHOLD_VELOCITY_X:
        if x_vel > 0:
            return 0
        else:
            return 1

    if y_pos > HOVER_HEIGHT and y_vel > THRESHOLD_VELOCITY_Y:
        return 3

    if y_vel < THRESHOLD_VELOCITY_Y:
        return 2

    if y_vel < -0.1:
        return 2

    return 3
