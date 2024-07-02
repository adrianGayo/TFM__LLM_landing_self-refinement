def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    if left_contact or right_contact:  # Already landed
        return 0

    if y_pos < 0.1 and abs(x_pos) < 0.05 and abs(x_vel) < 0.1 and abs(y_vel) < 0.1 and abs(angle) < 0.1 and abs(angular_vel) < 0.1:
        return 0  # Switch off engines for gentle landing

    # 1. Correct angle if angle deviation is significant
    if abs(angle) > 0.1:
        if angle > 0:
            return 1  # Push left engine to correct clockwise angle
        else:
            return 3  # Push right engine to correct counterclockwise angle

    # 2. Correct horizontal velocity (x_vel) for alignment
    if abs(x_vel) > 0.1:
        if x_vel > 0:
            return 1  # Push left engine to reduce rightward velocity
        else:
            return 3  # Push right engine to reduce leftward velocity

    # 3. Gradually reduce vertical velocity for descent control
    if y_vel < -0.5:
        return 2  # Push both engines upwards to slow down fast descent

    if y_pos > 0.1:  # Descend gently if y position is significantly above ground
        return 2  # Push both engines upwards to slow descent

    return 0  # Default action: switch off engines if conditions are stable