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
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0  # Default action is to switch off engines

    # Stabilize angle and angular velocity
    if angle < -0.1 or ang_vel < -0.1:
        action = 1  # Push left engine
    elif angle > 0.1 or ang_vel > 0.1:
        action = 3  # Push right engine
    # Control descent rate
    elif y_vel < -0.4:
        action = 2  # Push both engines (upwards)
    # When position is in the lower range, act to reduce velocities
    elif y_pos <= 0.5 and y_vel < -0.2:
        action = 2  # Push both engines (upwards)
    elif y_pos <= 0.5 and x_pos < -0.1:
        action = 3  # Push right engine
    elif y_pos <= 0.5 and x_pos > 0.1:
        action = 1  # Push left engine
    return action