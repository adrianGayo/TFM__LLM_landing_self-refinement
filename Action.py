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
    # Stabilize ship
    angle_threshold = 0.05
    velocity_threshold = 0.1
    target_y_velocity = -0.5
    angle_correction_factor = 10
    position_tolerance = 0.1

    x_position = observation[0]
    y_position = observation[1]
    x_velocity = observation[2]
    y_velocity = observation[3]
    angle = observation[4]
    angular_velocity = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    if left_contact or right_contact:
        return 0

    # Maintain vertical stability
    if abs(angle) > angle_threshold:
        if angle < 0:
            return 1  # Fire left engine to rotate clockwise
        else:
            return 3  # Fire right engine to rotate counter-clockwise

    # Control horizontal and vertical speed
    if abs(x_position) > position_tolerance or abs(x_velocity) > velocity_threshold:
        if x_velocity > 0:
            return 1  # Fire left engine to move left
        else:
            return 3  # Fire right engine to move right

    if y_velocity < target_y_velocity:
        return 2  # Fire main engine to reduce descent speed

    return 0
