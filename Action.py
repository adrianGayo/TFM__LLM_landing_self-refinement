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
    x, y, x_vel, y_vel, angle, angle_vel, left_contact, right_contact = observation
    if left_contact or right_contact: 
        return 0  # turn off engines if landed
    # Angle correction
    if angle < -0.1:
        return 3  # Push right engine
    elif angle > 0.1:
        return 1  # Push left engine
    # Speed correction (X axis)
    if x_vel < -0.1:
        return 3  # Push right engine
    elif x_vel > 0.1:
        return 1  # Push left engine
    # Speed correction (Y axis)
    if y_vel < -0.5:
        return 2  # Push both engines
    # General corrections for stable landing
    if y < 0.3 and abs(x_vel) > 0.05:
        if x_vel < 0:
            return 3  # Push right engine
        else:
            return 1  # Push left engine
    if y < 0.3 and y_vel < -0.2:
        return 2  # Push both engines
    return 0  # Switch off engines
