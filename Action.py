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
    x, y, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    # If the lander is tilted significantly, prioritize stabilizing
    if abs(angle) > 0.1:
        if angle < 0:
            return 1  # fire right engine to balance
        else:
            return 3  # fire left engine to balance
    
    # If the vertical velocity is too high, fire main engine
    if y_vel < -0.3:
        return 2

    # If the horizontal velocity is significant, adjust accordingly
    if x_vel > 0.3:
        return 3  # too much rightward velocity, fire left engine
    elif x_vel < -0.3:
        return 1  # too much leftward velocity, fire right engine
    
    # If very close to the ground, slow down slightly
    if y < 0.1:
        return 0

    # by default, fire main engine to descend softly
    return 2