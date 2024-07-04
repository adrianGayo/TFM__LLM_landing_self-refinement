def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state

    # Constants for simplification and scaling
    X_POS_THRESHOLD = 0.05
    Y_VEL_THRESHOLD = 0.12
    ANGLE_THRESHOLD = 0.1
    X_VEL_THRESHOLD = 0.15

    # Step-by-step state correction
    # 1. Angle correction: Realign quickly
    if angle < -ANGLE_THRESHOLD:  # Angles to the left
        return 3  # Push right engine
    elif angle > ANGLE_THRESHOLD:  # Angles to the right
        return 1  # Push left engine

    # 2. Accelerated vertical velocity correction: Control descent
    if y_vel < -Y_VEL_THRESHOLD:  # Falling too fast
        return 2  # Push both engines to slow descent

    # 3. Horizontal velocity management: Smooth left-right stabilizations
    if x_vel > X_VEL_THRESHOLD:  # Rapid rightward drift
        return 1  # Reduce speed with left engine
    elif x_vel < -X_VEL_THRESHOLD:  # Rapid leftward drift
        return 3  # Reduce speed with right engine

    # 4. Horizontal position leveling: Stay near central line
    if x_pos > X_POS_THRESHOLD:  # Right drift
        return 1  # Push left engine
    elif x_pos < -X_POS_THRESHOLD:  # Left drift
        return 3  # Push right engine

    # Default stabilization
    return 0
