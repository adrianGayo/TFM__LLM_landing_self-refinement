def act(observation):
    X_pos, Y_pos, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are on, keep engines off
    
    # Control horizontal position
    if X_pos < -0.1:  # Move right
        return 3
    elif X_pos > 0.1:  # Move left
        return 1

    # Control angle
    if angle < -0.1:
        return 1  # Push left engine
    elif angle > 0.1:
        return 3  # Push right engine

    # Control vertical speed
    if Y_velocity > -0.3:
        return 2  # Push both engines
    elif Y_velocity < -0.5:
        return 0  # Turn off engines, if falling fast, coast to slow down

    return 0  # Default action