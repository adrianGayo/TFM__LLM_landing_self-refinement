def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Thresholds for safe landing
    safe_angle_threshold = 0.1
    safe_vertical_speed = -0.1
    safe_horizontal_speed = 0.02

    # Landed already
    if left_contact == 1 and right_contact == 1:
        return 0

    # Angle correction
    if angle > safe_angle_threshold:
        return 3
    elif angle < -safe_angle_threshold:
        return 1

    # Horizontal velocity correction
    if x_vel > safe_horizontal_speed:
        return 1
    elif x_vel < -safe_horizontal_speed:
        return 3

    # Vertical speed control
    if y_vel < safe_vertical_speed:
        return 2
    else:
        return 0

    return 0