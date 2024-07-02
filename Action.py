import math

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
    X_pos, Y_pos, X_vel, Y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Define thresholds for decision making
    angle_threshold = 0.1  # Near vertical
    velocity_threshold = 0.1  # Near zero velocity
    position_threshold = 0.1  # Near landing area

    # Determine actions based on current state
    # Maintain vertical orientation (angle near zero)
    if angle < -angle_threshold:
        return 1  # Push left engine to rotate right
    elif angle > angle_threshold:
        return 3  # Push right engine to rotate left

    # Control horizontal position (X velocity near zero)
    if X_pos < -position_threshold or X_vel < -velocity_threshold:
        return 3  # Push right engine to move left
    elif X_pos > position_threshold or X_vel > velocity_threshold:
        return 1  # Push left engine to move right

    # Control vertical descent (Y velocity near zero)
    if Y_vel < -velocity_threshold:
        return 2  # Push both engines (upwards) to slow descent

    # Maintain current status (engines off)
    return 0