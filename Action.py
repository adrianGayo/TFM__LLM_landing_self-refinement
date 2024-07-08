def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, l_contact, r_contact = observation

    angle_threshold = 0.1
    velocity_threshold = 0.1
    y_velocity_threshold = -0.5

    # Stabilize descent speed first
    if y_vel < y_velocity_threshold:
        return 2  # Push both engines (upwards) to slow descent

    # Correct angular tilt only if significant
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 3  # Push right engine to counteract positive tilt
        else:
            return 1  # Push left engine to counteract negative tilt

    # Adjust horizontal drift if necessary
    if abs(x_vel) > velocity_threshold:
        if x_vel > 0:
            return 1  # Push left engine to counteract x_velocity to the right
        else:
            return 3  # Push right engine to counteract x_velocity to the left

    # If all within thresholds, switch off engines
    return 0