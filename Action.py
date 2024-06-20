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
    # Unpack the observation vector
    x_position = observation[0]
    y_position = observation[1]
    x_velocity = observation[2]
    y_velocity = observation[3]
    angle = observation[4]
    angular_velocity = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    # Parameters
    angle_threshold = 0.1
    angular_velocity_threshold = 0.3
    velocity_threshold = 0.1
    critical_y_velocity_threshold = -0.2
    stable_y_velocity_threshold = -0.5
    position_tolerance = 0.1
    critical_height = 0.3

    if left_contact or right_contact:
        return 0

    # Step 1: Maintain vertical orientation
    if abs(angle) > angle_threshold or abs(angular_velocity) > angular_velocity_threshold:
        if angle < 0 or angular_velocity < -angular_velocity_threshold:
            return 1
        else:
            return 3

    # Step 2: Slow down horizontal movement
    if abs(x_velocity) > velocity_threshold:
        if x_velocity > 0:
            return 1
        else:
            return 3

    # Step 3: Control descent speed
    if y_velocity < critical_y_velocity_threshold and y_position < critical_height:
        return 2
    elif y_velocity < stable_y_velocity_threshold:
        return 2

    # Step 4: Minor adjustments - based on height and x position
    if y_position < critical_height and abs(x_position) > position_tolerance:
        if x_position > 0:
            return 1
        else:
            return 3

    return 0
