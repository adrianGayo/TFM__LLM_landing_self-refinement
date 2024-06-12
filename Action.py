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
    x, y, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Define thresholds
    x_vel_threshold = 0.1
    y_vel_threshold = 0.1
    angle_threshold = 0.1
    ang_vel_threshold = 0.1

    # Prioritize reducing y velocity if it's too high (falling too fast)
    if y_vel < -y_vel_threshold:
        return 2  # Main engine on

    # Stabilize angular velocity if needed
    elif abs(ang_vel) > ang_vel_threshold:
        if ang_vel > 0:
            return 3  # Turn right engine on
        else:
            return 1  # Turn left engine on

    # Stabilize angle if needed
    elif abs(angle) > angle_threshold:
        if angle > 0:
            return 3  # Turn right engine on
        else:
            return 1  # Turn left engine on

    # Reduce x velocity if it's too high
    elif abs(x_vel) > x_vel_threshold:
        if x_vel > 0:
            return 1  # Turn left engine on
        else:
            return 3  # Turn right engine on

    # If all is stable, keep main engine off for gentle descent
    return 0