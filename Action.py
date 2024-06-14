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
    
    # Stabilizing Angles first
    if abs(angle) > 0.1 or abs(angular_vel) > 0.1:
        if angle > 0.1:
            return 1  # Fire right engine
        elif angle < -0.1:
            return 3  # Fire left engine
        elif angular_vel > 0.1:
            return 1  # Fire right engine
        else:
            return 3  # Fire left engine
    
    # Stabilize vertical speed
    if y_vel < -1.0:
        return 2  # Fire main engine to reduce speed
    
    # Stabilize horizontal position and speed
    if abs(x_vel) > 0.5:
        if x_vel > 0.5:
            return 3  # Fire left engine to reduce right drift
        else:
            return 1  # Fire right engine to reduce left drift
    
    # If already stable
    if y_pos > 0.1:
        return 2  # Fire main engine to gently descend
    
    return 0  # No action if everything is stable
