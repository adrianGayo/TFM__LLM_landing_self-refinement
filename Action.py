def act(observation):
    X_pos, Y_pos, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are on, keep engines off
    
    # Angle correction
    if abs(angle) > 0.1:
        return 1 if angle < 0 else 3  # Adjust tilt

    # Vertical speed stabilization
    if Y_velocity < -0.5:
        return 2  # Push both engines to slow descent
    elif Y_velocity > -0.2:
        return 0  # Turn off engines if descent too slow or ascending

    # Horizontal position control
    if X_pos < -0.2:
        return 3  # Push right engine
    elif X_pos > 0.2:
        return 1  # Push left engine

    return 0  # Default action to conserve fuel