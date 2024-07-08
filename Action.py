def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    angle_threshold = 0.1
    velocity_threshold = 0.1
    max_y_velocity_threshold = -0.3
    min_y_velocity_threshold = -1.0
    max_angle_threshold = 0.2

    # Prioritize descent stabilization
    if y_velocity < max_y_velocity_threshold:
        return 2  # Push both engines to ensure slowing down descent speed
    if y_velocity > min_y_velocity_threshold and right_contact == 0:
        return 2  # Use both engines to keep safe descent

    # Angular stability second
    if abs(angle) > max_angle_threshold:
        if angle > 0:
            return 3  # Push right engine to correct tilting positively
        else:
            return 1  # Push left engine to correct tilting negatively

    # Adjust horizontal drift
    if abs(x_velocity) > velocity_threshold:
        if x_velocity > 0:
            return 1  # Adjust drift by left engine to correct rightward movement
        else:
            return 3  # Adjust drift by right engine to correct leftward movement

    # Stabilize everything else by switching off all engines
    return 0