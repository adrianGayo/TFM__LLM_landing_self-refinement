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

    # Handle contact sensors, if either is activated, stabilize and turn off engines
    if left_contact == 1 or right_contact == 1:
        return 0

    # Combine checks for horizontal and vertical stabilization with priority
    if abs(vx) > 0.1:
        if vx > 0 and abs(angle) < 0.1 and abs(angular_velocity) < 0.1: 
            return 1  # Push left engine to counteract rightward velocity
        elif vx < 0 and abs(angle) < 0.1 and abs(angular_velocity) < 0.1:
            return 3  # Push right engine to counteract leftward velocity

    if abs(angle) > 0.1 or abs(angular_velocity) > 0.1:
        if angle > 0 or angular_velocity > 0:
            return 1  # Stabilize by using left engine
        elif angle < 0 or angular_velocity < 0:
            return 3  # Stabilize by using right engine

    # Provide upward thrust if descending too quickly or at low altitude
    if vy < -1.0 or y < 1.0:
        return 2

    # Main priority for ensuring a gentle descent, keep slight thrust upwards if needed
    if vy < -0.5:
        return 2

    # If no critical condition, turn off engines
    return 0