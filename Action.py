def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state
    
    # Constants for thresholds
    ANGLE_THRESHOLD = 0.1
    X_POSITION_THRESHOLD = 0.1
    X_VELOCITY_THRESHOLD = 0.1
    Y_VELOCITY_THRESHOLD = 0.1
    Y_POSITION_THRESHOLD = 0.1

    # Priority based decision making
    # 1. Angular stabilization
    if abs(angle) > ANGLE_THRESHOLD:
        if angle > 0:
            return 1 # Push left engine
        else:
            return 3 # Push right engine

    # 2. Vertical stabilization
    if y_vel < -Y_VELOCITY_THRESHOLD or y_pos < Y_POSITION_THRESHOLD:
        return 2 # Push both engines
    
    # 3. Horizontal positioning
    if x_pos < -X_POSITION_THRESHOLD:
        return 3 # Push right engine
    elif x_pos > X_POSITION_THRESHOLD:
        return 1 # Push left engine
    elif abs(x_vel) > X_VELOCITY_THRESHOLD:
        if x_vel > 0:
            return 1 # Push left engine
        else:
            return 3 # Push right engine

    # Default action
    return 0 # Switch off engines
