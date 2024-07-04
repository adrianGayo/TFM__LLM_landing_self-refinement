def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state

    # Constants for simplification and scaling
    X_POS_THRESHOLD = 0.1
    Y_VEL_THRESHOLD = 0.1
    ANGLE_THRESHOLD = 0.1
    X_VEL_THRESHOLD = 0.1

    # Determine actions based on current state
    
    if angle < -ANGLE_THRESHOLD:  # If angle is to the left
        return 3  # Push right engine to stabilize
    elif angle > ANGLE_THRESHOLD:  # If angle is to the right
        return 1  # Push left engine to stabilize
    
    if x_vel > X_VEL_THRESHOLD:  # If moving too fast to the right
        return 1  # Push left engine to slow down
    elif x_vel < -X_VEL_THRESHOLD:  # If moving too fast to the left
        return 3  # Push right engine to slow down
    
    if y_vel < -Y_VEL_THRESHOLD:  # If falling too fast
        return 2  # Push both engines upwards to slow down descent

    if abs(x_pos) > X_POS_THRESHOLD:  # If the horizontal position is far from center
        if x_pos > 0:  # If too far right
            return 1  # Push left engine to move left
        else:  # If too far left
            return 3  # Push right engine to move right

    # Default to switching off engines when stable
    return 0
