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
    X_position = observation[0]
    Y_position = observation[1]
    X_velocity = observation[2]
    Y_velocity = observation[3]
    Angle = observation[4]
    Angular_velocity = observation[5]
    Left_contact_sensor = observation[6]
    Right_contact_sensor = observation[7]
    # Example improvement: consider the X velocity in the decision making
    if X_velocity > 0.5:
        return 1  # Move left
    elif X_velocity < -0.5:
        return 3  # Move right
    else:
        return 2  # Move forward
