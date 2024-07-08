def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    angle_threshold = 0.1
    velocity_threshold = 0.1
    y_velocity_threshold = -0.5

    # Stabilize descent speed first
    if y_velocity < y_velocity_threshold:
        return 2  # Push both engines (upwards) to slow descent

    # Correct angular tilt only if significant
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 3  # Push right engine to counteract positive tilt
        else:
            return 1  # Push left engine to counteract negative tilt

    # Adjust horizontal drift if necessary
    if abs(x_velocity) > velocity_threshold:
        if x_velocity > 0:
            return 1  # Push left engine to counteract x_velocity to right
        else:
            return 3  # Push right engine to counteract x_velocity to left

    # If all within thresholds, switch off engines
    return 0