def act(observation):
    X_pos, Y_pos, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are on, keep engines off
    
    # Prioritize angle correction
    if angle < -0.1:
        return 1  # Push left engine
    elif angle > 0.1:
        return 3  # Push right engine

    # Control vertical speed
    if Y_velocity > -0.2:
        return 0  # Turn off engines when ascending or slow descent
    elif Y_velocity < -0.4:
        return 2  # Push both engines to slow descent

    # Control horizontal position
    if X_pos < -0.2:  # Too far left
        return 3
    elif X_pos > 0.2:  # Too far right
        return 1

    return 0  # Default action to conserve fuel and avoid unnecessary thrust