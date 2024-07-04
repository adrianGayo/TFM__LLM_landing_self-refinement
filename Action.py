def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Correct X position using side engines
    if x_pos > 0.1:  # If too far right, move left
        return 1  # Activate left engine
    elif x_pos < -0.1:  # If too far left, move right
        return 3  # Activate right engine

    # If horizontally aligned, focus on Y velocity control
    elif y_vel < -0.5:  # If falling too fast, push upwards
        return 2  # Activate both engines (upwards)

    # Fine adjustments for maintaining near-zero velocity and tilted correction
    elif x_vel > 0.3:  # If moving too fast to the right, counteract
        return 1  # Activate left engine
    elif x_vel < -0.3:  # If moving too fast to the left, counteract
        return 3  # Activate right engine

    elif abs(angle) > 0.4:  # If too tilted, adjust according to angle
        if angle > 0:
            return 1  # Tilt correction
        else:
            return 3  # Tilt correction

    # Minimal engine usage for fine adjustments close to landing
    elif y_pos < 0.2 and y_vel < -0.2:  # If approaching ground too fast at low height
        return 2  # Use central engine to slow down
    elif y_pos < 0.2 and abs(y_vel) < 0.2:  # Hover or near-zero velocity
        return 0  # Switch off engines for small adjustments

    # If no critical changes needed
    return 0  # Default to no engine for stability

