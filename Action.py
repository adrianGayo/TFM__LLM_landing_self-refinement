def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Check if the lander has landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable

    # Prioritize angle correction
    if angle > 0.1:  # Tilted to the right
        return 1  # Push left to correct
    elif angle < -0.1:  # Tilted to the left
        return 3  # Push right to correct

    # Stabilize vertical velocity to control descent speed
    if y_vel < -0.5:
        return 2  # Push both engines upwards

    # Stabilize horizontal position
    if x_pos > 0.05:  # Lander is to the right of target
        if x_vel > -0.5:
            return 1  # Push left engine
    elif x_pos < -0.05:  # Lander is to the left of target
        if x_vel < 0.5:
            return 3  # Push right engine

    # If all conditions are met, keep engines off
    return 0