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
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Rule 1: If the craft is too tilted and in air, correct the tilt by firing side engines
    if abs(angle) > 0.15:  # Increased threshold for robustness
        if angle < 0:
            return 3  # Fire left engine to tilt right
        else:
            return 1  # Fire right engine to tilt left

    # Rule 2: If descending too fast, slow descent
    if y_vel < -0.3:
        return 2  # Fire main engine to reduce descent rate
    
    # Rule 3: If moving horizontally too fast, reduce horizontal speed
    if abs(x_vel) > 0.3:
        if x_vel > 0:
            return 3  # Fire left engine to move left
        else:
            return 1  # Fire right engine to move right

    # Rule 4: If already landed, stop firing engines
    if left_contact == 1 and right_contact == 1:
        return 0

    # Rule 5: Favor main engine for fine control near landing zone
    if left_contact == 1 or right_contact == 1:
        return 2  # Fire main engine to stabilize descent

    # Default action - Do nothing to save fuel
    return 0