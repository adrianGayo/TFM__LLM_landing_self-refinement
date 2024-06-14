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
    vx_threshold_high = 0.1
    vy_threshold_high = 0.1
    angle_threshold_high = 0.1
    vx_threshold_low = 0.01
    vy_threshold_low = 0.01
    angle_threshold_low = 0.01

    if left_contact or right_contact:
        return 0  # Do nothing if landed

    if abs(vx) > vx_threshold_high or abs(vy) > vy_threshold_high or abs(angle) > angle_threshold_high:
        # If any critical parameter is too high, control it strictly
        if abs(vx) > vx_threshold_high:
            if vx > 0:
                return 3  # Fire left to correct vx
            else:
                return 1  # Fire right to correct vx
        if abs(vy) > vy_threshold_high:
            return 2  # Fire main engine to correct vy
        if abs(angle) > angle_threshold_high:
            if angle > 0:
                return 3  # Fire left to correct angle
            else:
                return 1  # Fire right to correct angle
    else:
        # Fine control
        if abs(vx) > vx_threshold_low:
            if vx > 0:
                return 1  # Fire right to slightly correct vx
            else:
                return 3  # Fire left to slightly correct vx
        if abs(vy) > vy_threshold_low:
            return 2  # Fire main engine to slightly correct vy
        if abs(angle) > angle_threshold_low:
            if angle > 0:
                return 1  # Fire right to slightly correct angle
            else:
                return 3  # Fire left to slightly correct angle

    return 0  # No action needed