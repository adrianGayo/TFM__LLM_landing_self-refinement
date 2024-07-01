def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    # Balance correction effectively for combined actions on vectors.
    # Adjust angles first if significantly deviated:
    if angle < -0.1 or angular_vel < -0.5:
        return 1  # correct tilt left
    elif angle > 0.1 or angular_vel > 0.5:
        return 3  # correct tilt right

    # Control horizontal position and velocity together
    if x_pos < -0.1 or x_vel < -0.5:
        return 3  # redirect right
    elif x_pos > 0.1 or x_vel > 0.5:
        return 1  # redirect left

    # Control descent speed more actively
    if y_vel < -0.2:
        return 2  # Main engine burst to slow fast downward speed

    # Default fallback ensuring balanced no-action if compounded vectors within allowed range
    return 0