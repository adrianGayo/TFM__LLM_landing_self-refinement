def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    threshold = 0.05
    angle_threshold = 0.05  # tighter angle correction
    y_velocity_threshold = -0.1  # max safe velocity for descent
    
    # Stage 1: Correct angle first
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 1  # Push left engine to counteract positive tilt
        else:
            return 3  # Push right engine to counteract negative tilt

    # Stage 2: Adjust horizontal velocity
    if abs(x_velocity) > threshold:
        if x_velocity > 0:
            return 1  # Push left engine to slow right drift
        else:
            return 3  # Push right engine to slow left drift

    # Stage 3: Adjust vertical velocity, if descent is too quick
    if y_velocity < y_velocity_threshold or y_position > 0.1:
        return 2  # Use central engine to slow descent

    # If within acceptable range, switch off engines
    return 0