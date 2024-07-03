def act(state):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = state
    
    # Stabilization
    if abs(angle) > 0.1:
        if ang_vel > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine

    # Horizontal Positioning
    if x_pos < -0.1:
        return 3  # Push right engine
    elif x_pos > 0.1:
        return 1  # Push left engine

    # Descent Control
    if y_vel < -0.1:
        return 2  # Push both engines

    # Landing Phase
    if y_pos < 0.1 and abs(y_vel) < 0.1 and abs(x_vel) < 0.1:
        return 0  # Switch off engines

    # Default action
    return 2  # Push both engines
