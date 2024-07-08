def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Parameters
    max_horizontal_speed = 0.1
    max_vertical_speed = 0.5
    max_tilt_angle = 0.1
    max_tilt_speed = 0.1

    # Correct tilt
    if angle > max_tilt_angle:
        return 1  # push left engine to tilt right
    elif angle < -max_tilt_angle:
        return 3  # push right engine to tilt left

    # Reduce horizontal speed
    if x_velocity > max_horizontal_speed:
        return 1  # push left engine to move left
    elif x_velocity < -max_horizontal_speed:
        return 3  # push right engine to move right

    # Reduce vertical speed
    if y_velocity > max_vertical_speed:
        return 2  # push both engines (upwards) to slow down descent

    # If already near land and stably oriented, switch off engines for smooth landing
    if y_position < 0.1 and abs(y_velocity) < max_vertical_speed and abs(x_velocity) < max_horizontal_speed:
        return 0  # switch off engines

    # Default action: small adjustments to maintain stability
    return 2  # default action to push both engines (upwards) to control descent
