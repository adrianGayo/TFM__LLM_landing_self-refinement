def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state

    # Constants for simplification and scaling
    X_POS_THRESHOLD = 0.05
    Y_VEL_THRESHOLD = 0.15
    ANGLE_THRESHOLD = 0.1
    X_VEL_THRESHOLD = 0.2

    # 1. Correction of the angle: Stabilize nconfiguration early.
    if angle < -ANGLE_THRESHOLD:  # Angles to the left
        return 3  # Push right engine
    elif angle > ANGLE_THRESHOLD:  # Angles to the right
        return 1  # Push left engine

    # 2. Priority correction of vertical descent velocity.
    if y_vel < -Y_VEL_THRESHOLD:  # Falling too fast
        return 2  # Push both engines to slow descent

    # 3. Correction of horizontal velocity.
    if x_vel > X_VEL_THRESHOLD:  # Rightward movement
        return 1  # Push left engine to slow
    elif x_vel < -X_VEL_THRESHOLD:  # Leftward movement
        return 3  # Push right engine slow

    # 4. Horizontal positional adjustments.
    if x_pos > X_POS_THRESHOLD:  # Rightwards drift
        return 1  # Push left engine
    elif x_pos < -X_POS_THRESHOLD:  # Leftwards drift
        return 3  # Push right engine

    # Default stabilization
    return 0
