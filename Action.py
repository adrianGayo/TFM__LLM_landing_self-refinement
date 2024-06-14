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

    # Steps for landing stabilization
    # 1. Angle Stabilization
    if abs(angle) > 0.1 or abs(angular_vel) > 0.1:
        if angle > 0.1 or angular_vel > 0.1:
            return 2  # Fire main engine
        elif angle < -0.1 or angular_vel < -0.1:
            return 2  # Fire main engine

    # 2. Vertical Speed Stabilization
    if y_vel < -0.5:
        return 3  # Fire left engine to reduce vertical speed

    # 3. Horizontal Speed Stabilization
    if abs(x_vel) > 0.2:
        if x_vel > 0.2:
            return 1  # Fire right engine to reduce horizontal speed
        elif x_vel < -0.2:
            return 0  # Fire no engine

    # 4. Gentle Descent with Vertical Positioning
    if y_pos > 0.2:
        return 2  # Fire main engine to gently descend

    return 0  # No action needed if everything is stable