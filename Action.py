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
    '''
    # Extracting the necessary components from the observation
    x_pos = observation[0]
    y_pos = observation[1]
    x_vel = observation[2]
    y_vel = observation[3]
    angle = observation[4]
    angular_vel = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    # Implementing decision logic based on the observed data
    if y_vel < -0.5:  # If the lander is falling quickly
        return 2  # Fire the main engine to slow descent
    if abs(angle) > 0.1:  # If the lander is tilted
        if angle > 0:  # Tilted to the right
            return 0  # Fire left engine to balance
        else:  # Tilted to the left
            return 1  # Fire right engine to balance
    if x_vel > 0.5:  # If moving too fast horizontally right
        return 0  # Fire left engine to slow down
    if x_vel < -0.5:  # If moving too fast horizontally left
        return 1  # Fire right engine to slow down
    if y_vel > -0.3 and y_pos > 0.5:  # If the lander is not falling too fast and is still high
        return 3  # Do nothing or slight adjustments
    return 2  # Otherwise, fire the main engine to have a controlled descent