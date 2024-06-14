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
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation

    # Thresholds
    vx_threshold = 0.1
    vy_threshold = 0.1
    angle_threshold = 0.1

    if left_contact or right_contact:
        return 0  # Do nothing if landed

    if abs(vx) > vx_threshold:
        if vx > 0:
            return 3  # Fire left to correct vx
        else:
            return 1  # Fire right to correct vx

    if abs(vy) > vy_threshold:
        return 2  # Fire main engine to correct vy

    if abs(angle) > angle_threshold:
        if angle > 0:
            return 3  # Fire left to correct angle
        else:
            return 1  # Fire right to correct angle

    return 0  # No action needed