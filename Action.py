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
    # Stabilize angle first
    if angle < -0.1:
        return 3  # Push right engine
    elif angle > 0.1:
        return 1  # Push left engine
    # If angle is stable, manage velocities
    elif abs(x_vel) > 0.1:
        if x_vel < 0:
            return 3  # Push right engine
        else:
            return 1  # Push left engine
    elif y_vel < -0.2:
        return 2  # Push both engines upwards
    # If almost landed, careful adjustments
    if y < 0.3:
        if abs(x_vel) > 0.05:
            if x_vel < 0:
                return 3
            else:
                return 1
    return 0  # Switch off engines