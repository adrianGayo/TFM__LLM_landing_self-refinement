def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # First, check if the lander has landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable
    
    # Stabilize horizontal position using better tuned thresholds
    if x_pos > 0.1:  # Lander is to the right of target
        if x_vel > -0.3:  # Slightly more tolerant velocity threshold
            return 1  # Push left engine to adjust
    elif x_pos < -0.1:  # Lander is to the left of target
        if x_vel < 0.3:  # Slightly more tolerant velocity threshold
            return 3  # Push right engine to adjust

    # Stabilize vertical velocity with conservative engine usage
    if y_vel < -0.5:
        return 2  # Push both engines upwards to slow descent

    # Correct angle with improved angular thresholds
    if angle > 0.1:  # Tilted to the right
        return 1  # Push left engine to counter
    elif angle < -0.1:  # Tilted to the left
        return 3  # Push right engine to counter

    # If all conditions are satisfactorily met, maintain engine off
    return 0