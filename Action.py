def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state

    # Constants for simplification and scaling
    X_POS_THRESHOLD = 0.05
    Y_VEL_THRESHOLD = 0.15
    ANGLE_THRESHOLD = 0.1
    X_VEL_THRESHOLD = 0.2

    # Determine actions based on current state
    # 1. Correct the angle first
    if angle < -ANGLE_THRESHOLD:  # If angle is to the left, push right engine
        return 3
    elif angle > ANGLE_THRESHOLD:  # If angle is to the right, push left engine
        return 1

    # 2. Correct horizontal velocity
    if x_vel > X_VEL_THRESHOLD:  # If moving too fast to the right
        return 1  # Push left engine to slow down
    elif x_vel < -X_VEL_THRESHOLD:  # If moving too fast to the left
        return 3  # Push right engine to slow down
    
    # 3. Correct horizontal position
    if x_pos > X_POS_THRESHOLD:  # If too far right
        return 1  # Push left engine
    elif x_pos < -X_POS_THRESHOLD:  # If too far left
        return 3  # Push right engine

    # 4. Correct vertical velocity for safe descent
    if y_vel < -Y_VEL_THRESHOLD:  # If falling too fast
        return 2  # Push both engines upwards to slow descent

    # Default: Stabilize
    return 0
