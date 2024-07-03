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
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    
    # Initialize default action as switching off engines
    action = 0  

    # Prioritize reducing downward vertical velocity if it exceeds the threshold
    if y_velocity < -0.5:
        action = 2  # Push both engines (upwards)
    
    # Control and stabilize the angle if it exceeds certain range
    elif abs(angle) > 0.1 or abs(angular_velocity) > 0.1:
        if angle < 0 or angular_velocity < 0:
            action = 3  # Push right engine
        else:
            action = 1  # Push left engine
    
    # Control horizontal position and velocity to keep it centered
    elif abs(x_velocity) > 0.5 or abs(x_position) > 0.5:
        if x_velocity > 0 or x_position > 0:
            action = 1  # Push left engine
        else:
            action = 3  # Push right engine

    return action