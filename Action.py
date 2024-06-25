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
        Integer : The action to be taken.
        "options": {
                '0' : "Switch off engines",
                '1' : "Push left engine",
                '2' : "Push both engines (upwards)",
                '3' : "Push right engine"
            }
    '''
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_cont, right_cont = observation

    # Thresholds
    angle_threshold = 0.1
    angular_velocity_threshold = 0.1
    horizontal_distance_threshold = 0.2
    horizontal_velocity_threshold = 0.2
    vertical_velocity_threshold = -0.3
    stabilization_threshold = 0.1

    # Stabilize angle first if it is too tilted or rotating too fast
    if angle < -angle_threshold:  # Tilting too much left or rotating too fast counterclockwise
        return 1
    if angle > angle_threshold:  # Tilting too much right or rotating too fast clockwise
        return 3

    # Use main engine to reduce vertical speed if falling too fast
    if y_vel < vertical_velocity_threshold:  # Falling too fast
        return 2

    # Correct horizontal position if too far from the center
    if x_pos < -horizontal_distance_threshold or x_vel < -horizontal_velocity_threshold:  # Too far left or moving too fast to the left
        return 3
    if x_pos > horizontal_distance_threshold or x_vel > horizontal_velocity_threshold:  # Too far right or moving too fast to the right
        return 1

    # If the velocity and angle are small, turn off engines to stabilize
    if abs(y_vel) < stabilization_threshold and abs(x_vel) < stabilization_threshold and abs(angle) < stabilization_threshold:
        return 0

    # In other cases, do nothing
    return 0