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
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation
    # Handle contact sensors, if either are activated, stabilize and turn off engines
    if left_contact == 1 or right_contact == 1:
        return 0
    # Prioritize stabilizing horizontal velocity
    if abs(vx) > 0.1:
        return 1 if vx > 0 else 3
    # Then, stabilize angular velocity
    if abs(angular_velocity) > 0.1:
        return 1 if angular_velocity > 0 else 3
    # Then, stabilize angle
    if abs(angle) > 0.1:
        return 1 if angle > 0 else 3
    # If descending too quickly, apply both engines
    if vy < -0.5:
        return 2
    # Apply gentle thrust upwards if needed
    if y < 1.0:
        return 2
    # If none of the above are critical, turn off engines
    return 0