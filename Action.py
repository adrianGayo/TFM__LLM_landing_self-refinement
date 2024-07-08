def act(observation):
    X_pos, Y_pos, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are on, keep engines off

    # Priority angle correction more dynamically
    if angle < -0.05 or angle > 0.05:
        if angle < 0:
            return 1  # Push left engine for angle correction
        else:
            return 3  # Push right engine for angle correction

    # Control vertical speed more precisely
    if Y_velocity > -0.1:
        return 2  # Use both engines to steady descent
    elif Y_velocity < -0.3:
        return 0  # Excess thrust off for gradual descent

    # Control horizontal position if needed dynamically
    if X_pos < -0.2:  # Too left; balance right
        return 3
    elif X_pos > 0.2:  # Too right; balance left
        return 1

    return 0  # Default to static if within stable bounds