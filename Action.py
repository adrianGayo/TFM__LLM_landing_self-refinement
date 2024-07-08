def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    # Define thresholds
    angle_threshold = 0.05
    velocity_threshold = 0.05
    y_velocity_threshold = -0.5  # Max safe downward velocity
    
    # Adjust angle first
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 1  # Push left engine to counteract positive tilt
        else:
            return 3  # Push right engine to counteract negative tilt

    # Adjust horizontal velocity
    if abs(x_velocity) > velocity_threshold:
        if x_velocity > 0:
            return 1  # Push left engine to counteract x_velocity to right
        else:
            return 3  # Push right engine to counteract x_velocity to left

    # Adjust vertical velocity
    if y_velocity < y_velocity_threshold or y_position > 0.1:
        return 2  # Push upward to slow descent

    # If all within thresholds, switch off engines
    return 0