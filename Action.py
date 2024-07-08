def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Check if the lander has landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable

    # Prioritize angle correction immediately to achieve stability
    if angle > 0.1:  # Tilted to the right
        return 1  # Push left
    elif angle < -0.1:  # Tilted to the left
        return 3  # Push right
    
    # Stabilize horizontal position, correct positioning before focusing on speeds
    if x_pos > 0.05:  # Lander right of target
        return 1 if x_vel > -0.5 else 0  # Push left for counter
    elif x_pos < -0.05:  # Lander left of target
        return 3 if x_vel < 0.5 else 0  # Push right to balance

    # Correct descent speed post stabilization of angles and position
    if y_vel < -0.5:
        return 2  # Use the main engine to slow vertical descent, reducing impact

    # Keep engines turned off if all conditions are stable
    return 0