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
    action = 0  # Default to switching off engines
    
    # Stabilize horizontal speed and position (keep the X position within some range around the center)
    if abs(x_velocity) > 0.1:
        if x_velocity > 0:
            action = 1  # Push left engine to counteract rightward velocity
        else:
            action = 3  # Push right engine to counteract leftward velocity
    
    # Stabilize descent speed (vertical speed)
    if y_velocity < -0.1:
        action = 2  # Push both engines (upwards) to counteract downward velocity

    # Stabilize angle
    if abs(angle) > 0.1:
        if angle < 0:
            action = 3  # Push right engine to rotate right
        else:
            action = 1  # Push left engine to rotate left

    return action