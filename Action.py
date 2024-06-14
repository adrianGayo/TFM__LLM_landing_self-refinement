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
    # Extract values from observation
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Decision Making Logic based on observed status
    if left_contact == 1 or right_contact == 1:  # If any landing gear has made contact
        return 0  # Switch off engines for gentle landing

    # Horizontal stabilization
    if abs(x_vel) > 0.2:  # If horizontal speed is significant
        if x_vel > 0:  # Move to the right
            return 1  # Push left engine to reduce rightward movement
        else:  # Move to the left
            return 3  # Push right engine to reduce leftward movement

    # Angular stabilization
    if abs(angle) > 0.1 or abs(ang_vel) > 0.1:  # If angle or angular velocity is significant
        if angle > 0 or ang_vel > 0:  # If angle or angular velocity is to the right
            return 1  # Push left engine
        else:  # If angle or angular velocity is to the left
            return 3  # Push right engine

    # Vertical stabilization
    if y_vel < -0.2:  # If falling too fast
        return 2  # Push both engines (upwards) to slow descent

    # Default case
    return 0
