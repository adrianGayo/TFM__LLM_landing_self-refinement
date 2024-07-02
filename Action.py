def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    if left_contact or right_contact:  # Already landed
        return 0

    if y_pos < 0.1 and abs(x_pos) < 0.05 and abs(x_vel) < 0.1 and abs(y_vel) < 0.1 and abs(angle) < 0.1 and abs(angular_vel) < 0.1:
        return 0  # Switch off engines for gentle landing

    # Correct significant angle deviation first
    if abs(angle) >= 0.2:  # Adjusted angle threshold
        if angle > 0:
            return 1  # Push left engine to correct clockwise tilt
        else:
            return 3  # Push right engine to correct counterclockwise tilt

    # Correct horizontal velocity for alignment
    if abs(x_vel) >= 0.2:  # Lower threshold for smoother horizontal control
        if x_vel > 0:
            return 1  # Push left engine to mitigate rightward movement
        else:
            return 3  # Push right engine to mitigate leftward movement

    # Control vertical descent velocity for smoother descent
    if y_vel <= -0.5 and y_pos >= 0.3:  # Manage descent speed based on altitude
        return 2  # Use both engines to slow down

    if y_pos > 0.2 and y_vel < 0:  # Use vertical thrust for controlled descent
        return 2  # Push both engines upwards

    return 0  # Default action: switch off engines if stable
