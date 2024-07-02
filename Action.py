def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    if left_contact or right_contact:  # Already landed
        return 0

    if y_pos < 0.1 and abs(x_pos) < 0.05 and abs(x_vel) < 0.1 and abs(y_vel) < 0.1 and abs(angle) < 0.1 and abs(angular_vel) < 0.1:
        return 0  # Switch off engines for gentle landing

    # 1. Correct angle if deviation is significant
    if abs(angle) > 0.1:
        if angle > 0:
            return 1  # Push left engine to tilt left
        else:
            return 3  # Push right engine to tilt right

    # 2. Control horizontal velocity (x_vel) for alignment
    if abs(x_vel) > 0.2:
        if x_vel > 0:
            return 1  # Push left engine to correct rightward movement
        else:
            return 3  # Push right engine to correct leftward movement

    # 3. Manage vertical velocity (y_vel) for smoother descent
    if y_vel < -0.5 and y_pos > 0.2:
        return 2  # Push both engines upwards to decelerate descent

    if y_pos > 0.2:  # Continue descent control while above significant altitude
        return 2  # Push both engines upwards for smooth descent

    return 0