def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, l_contact, r_contact = observation

    x_threshold = 0.05
    vertical_threshold = -0.2
    angle_threshold = 0.1

    if l_contact == 1 and r_contact == 1:
        return 0  # Switch off engines if both sensors indicate landing

    # Correcting horizontal velocity
    if abs(x_vel) > x_threshold:
        if x_vel > 0:
            return 1  # Push left engine to counteract x_vel to right
        else:
            return 3  # Push right engine to counteract x_vel to left

    # Correcting angle
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 1  # Push left engine to counteract positive tilt
        else:
            return 3  # Push right engine to counteract negative tilt

    # Correcting vertical velocity and position
    if y_vel < vertical_threshold or y_pos > 0.1:
        return 2  # Push both engines upwards to slow descent

    return 0  # Default action switches off engines