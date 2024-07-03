def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state

    # Constants for thresholds
    ANGLE_THRESHOLD = 0.05
    X_POSITION_THRESHOLD = 0.02
    X_VELOCITY_THRESHOLD = 0.02
    Y_VELOCITY_THRESHOLD = 0.05
    Y_POSITION_THRESHOLD = 1

    # 1. Vertical stabilization
    if y_vel < -Y_VELOCITY_THRESHOLD:
        return 2  # Push both engines to reduce descent speed

    # 2. Angular stabilization
    if abs(angle) > ANGLE_THRESHOLD:
        if angle > 0:
            return 3  # Push right engine
        else:
            return 1  # Push left engine

    # 3. Horizontal Positioning
    if abs(x_vel) > X_VELOCITY_THRESHOLD:
        if x_vel > 0:
            return 1  # Push left engine for countering drift
        else:
            return 3  # Push right engine to counter drift

    # 4. Position Centering
    if x_pos < -X_POSITION_THRESHOLD:
        return 3  # Push right engine to move to center
    elif x_pos > X_POSITION_THRESHOLD:
        return 1  # Push left to move to center

    # Default action
    return 0  # Switch off engines
