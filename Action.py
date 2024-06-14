import random

PUSH_OFF = 0
PUSH_LEFT = 1
PUSH_BOTH = 2
PUSH_RIGHT = 3

thresholds = {
    "x_velocity": 0.1,
    "y_velocity": 0.1,
    "angle": 0.1,
    "angular_velocity": 0.1,
}


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
    xpos, ypos, xvel, yvel, angle, angvel, lcontact, rcontact = observation

    # Stabilize x-velocity
    if abs(xvel) > thresholds["x_velocity"]:
        return PUSH_LEFT if xvel > 0 else PUSH_RIGHT

    # Stabilize angular velocity
    if abs(angvel) > thresholds["angular_velocity"]:
        return PUSH_LEFT if angvel > 0 else PUSH_RIGHT

    # Stabilize angle
    if abs(angle) > thresholds["angle"]:
        return PUSH_LEFT if angle > 0 else PUSH_RIGHT

    # Stabilize y-velocity
    if abs(yvel) > thresholds["y_velocity"]:
        return PUSH_BOTH if yvel > 0 else PUSH_OFF

    return PUSH_OFF
