def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Landed condition
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable

    # Horizontal control with moderate thresholds
    if x_pos > 0.1 and x_vel > -0.3:
        return 1  # Slight thrust to left
    elif x_pos < -0.1 and x_vel < 0.3:
        return 3  # Slight thrust to right

    # Vertical velocity control
    if y_vel < -0.5:
        return 2  # Both engines thrust upward

    # Angular correction
    if angle > 0.1:
        return 1  # Correct tilt to the left
    elif angle < -0.1:
        return 3  # Correct tilt to the right

    return 0  # Default to no action
