def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    threshold = 0.05
    if abs(x_velocity) > threshold:
        if x_velocity > 0:
            return 1  # Push left engine to counteract x_velocity to right
        else:
            return 3  # Push right engine to counteract x_velocity to left
    
    if abs(angle) > threshold:
        if angle > 0:
            return 1  # Push left engine to counteract positive tilt
        else:
            return 3  # Push right engine to counteract negative tilt

    if y_velocity < -threshold or y_position > 0.1:
        return 2  # Push upward to slow descent
    
    return 0  # If all within thresholds, switch off engines