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
    X_position, Y_position, X_velocity, Y_velocity, Angle, Angular_velocity, Left_contact, Right_contact = observation
    # Initial descent control
    if Y_position > 1.3 and Y_velocity < -0.3:
        return 2
    # Horizontal drift management
    if abs(X_position) > 0.1:
        if X_position > 0 and X_velocity > 0:
            return 1
        if X_position < 0 and X_velocity < 0:
            return 3
    # Angle stabilization
    if abs(Angle) > 0.1:
        if Angle > 0 and Angular_velocity > 0:
            return 1
        if Angle < 0 and Angular_velocity < 0:
            return 3
    # Final approach and soft landing
    if Y_position < 0.3:
        if Y_velocity < -0.1:
            return 2
        else:
            return 0
    return random.randint(0, 3)
