def act(observation):
    X_pos, Y_pos, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are on, keep engines off

    # Priority angle correction
    if angle < -0.05 or angle > 0.05:
        if angle < 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine

    # Control vertical speed
    if Y_velocity > -0.1:
        return 0  # Turn off engines to allow natural descent when very slow
    elif Y_velocity < -0.3:
        return 2  # Push both engines to slow descent

    # Control horizontal position if significantly off-center
    if X_pos < -0.2:  # Too far left
        return 3
    elif X_pos > 0.2:  # Too far right
        return 1

    return 0  # Default action to conserve fuel and avoid unnecessary thrust