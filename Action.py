def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1
    critical_angle_threshold = 0.5
    critical_speed_threshold = -2.0

    # Extreme conditions
    if y_velocity < critical_speed_threshold or abs(angle) > critical_angle_threshold:
        return 2  # fire both engines to stabilize
    
    # Correcting vertical speed
    if y_velocity < vertical_speed_threshold:
        return 2  # fire both engines to slow descent
    
    # Correcting horizontal speed
    if x_velocity > horizontal_speed_threshold:
        return 1  # fire left engine to reduce rightward velocity
    elif x_velocity < -horizontal_speed_threshold:
        return 3  # fire right engine to reduce leftward velocity
    
    # Correcting angles
    if angle < -angle_threshold:
        return 1  # fire left engine to correct angle left
    elif angle > angle_threshold:
        return 3  # fire right engine to correct angle right
    
    return 0  # switch off engines when stable
