def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    # Prioritize stabilization
    if angle < -0.1 or angular_vel < -0.5:  # Too tilted to the left, apply right thrust
        return 1
    elif angle > 0.1 or angular_vel > 0.5:  # Too tilted to the right, apply left thrust
        return 3
    
    # Manage horizontal position and velocity
    if x_pos < -0.1 or x_vel < -0.5:  # Too far left, apply right thrust
        return 3
    elif x_pos > 0.1 or x_vel > 0.5:  # Too far right, apply left thrust
        return 1

    # Control descent speed
    if y_vel < -0.5:  # Falling too fast, apply main engine
        return 2

    # Default action if all parameters are in acceptable range
    return 0