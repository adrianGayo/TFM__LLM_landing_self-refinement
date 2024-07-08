def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    if y_vel < -0.5 and y_pos > 0.2:  # Fast descent, high altitude
        return 2  # Engage upward thrust
    if abs(x_vel) > 0.2:  # Large horizontal velocity
        if x_vel < 0:
            return 3  # Thrust right (counteract leftward movement)
        else:
            return 1  # Thrust left (counteract rightward movement)
    if abs(angle) > 0.1:  # Tilted
        if angle < 0:
            return 3  # Correct counter-clockwise tilt
        else:
            return 1  # Correct clockwise tilt
    if y_pos > 0.1 and y_vel < -0.2:  # Moderate descent below safe velocity
        return 2  # Engage upward thrust
    return 0  # Switch off engines for minor corrections