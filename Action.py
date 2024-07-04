def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state

    # Constants for simplification and scaling
    X_POS_THRESHOLD = 0.05
    Y_VEL_THRESHOLD = 0.05
    ANGLE_THRESHOLD = 0.1

    # Determine actions based on current state
    if angle < -ANGLE_THRESHOLD:  # If angle is to the left
        return 3  # Push right engine to stabilize
    elif angle > ANGLE_THRESHOLD:  # If angle is to the right
        return 1  # Push left engine to stabilize
    elif abs(x_pos) > X_POS_THRESHOLD:  # If the horizontal position is far from center
        if x_pos > 0:  # If too far right
            return 1  # Push left engine to move left
        else:  # If too far left
            return 3  # Push right engine to move right
    elif abs(x_vel) > X_POS_THRESHOLD:  # If horizontal velocity is high
        if x_vel > 0:  # If moving too fast to the right
            return 1  # Push left engine to slow down
        else:  # If moving too fast to the left
            return 3  # Push right engine to slow down
    elif y_vel < -Y_VEL_THRESHOLD:  # If falling too fast
        return 2  # Push both engines upwards to slow down descent
    else:  # Default to switching off engines
        return 0
