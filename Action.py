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
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    if left_contact or right_contact:
        return 3  # Do nothing if we are in contact with lander.
    
    # Combining some threshold values
    THRESHOLD_ANGLE = 0.1
    THRESHOLD_VELOCITY_X = 0.5
    THRESHOLD_VELOCITY_Y = -0.5  # descending threshold

    # Maintain stability; avoid large angles
    if abs(angle) > THRESHOLD_ANGLE:
        if angle > 0:
            return 0  # Fire left engine to balance right tilt
        else:
            return 1  # Fire right engine to balance left tilt
    
    # Control Horizontal Velocity
    if x_vel > THRESHOLD_VELOCITY_X:
        return 0  # Move left to reduce rightward velocity
    if x_vel < -THRESHOLD_VELOCITY_X:
        return 1  # Move right to reduce leftward velocity
    
    # Ensure the craft descends under controlled speed
    if y_vel < THRESHOLD_VELOCITY_Y:
        return 2  # Fire main engine to slow descent

    # Controlled descent part - reduce engine fires
    if y_vel > -0.3 and y_pos > 0.5: 
        return 3  # Glide down when there's enough height
    
    # Default action to control descent rate
    return 2  # Fire main engine
