def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    threshold = 0.05
    angle_threshold = 0.1
    if y_position > 0.1 or y_velocity < -0.1:
        if abs(angle) > angle_threshold:
            if angle > 0:
                return 3  # Push right engine to counteract positive tilt
            else:
                return 1  # Push left engine to counteract negative tilt
        if abs(x_velocity) > threshold:
            if x_velocity > 0:  # Drift to the right
                return 1  # Push left engine to counteract x_velocity to right
            else:  # Drift to the left
                return 3  # Push right engine to counteract x_velocity to left
        return 2  # Push both engines (upwards) to slow descent
    return 0  # If all within thresholds, switch off engines