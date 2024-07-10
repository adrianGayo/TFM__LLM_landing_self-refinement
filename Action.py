def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Thresholds for a safe landing
    safe_angle_threshold = 0.1
    safe_vertical_speed = -0.2
    safe_horizontal_speed = 0.2

    # Landed already
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines, we're landed

    # Correct Orientation
    if angle > safe_angle_threshold:
        return 3  # Push right engine to rotate left
    elif angle < -safe_angle_threshold:
        return 1  # Push left engine to rotate right

    # Vertical speed control
    if y_vel < safe_vertical_speed:  # If descending too fast
        return 2  # Push both engines to slow down

    # Horizontal velocity correction
    if x_vel > safe_horizontal_speed:
        return 1  # Push left engine to move left
    elif x_vel < -safe_horizontal_speed:
        return 3  # Push right engine to move right

    # Default to doing nothing if all within safe thresholds
    return 0