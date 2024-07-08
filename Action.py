def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Landed condition
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable

    # Stabilize horizontal position with dynamic thresholds
    if x_pos > 0.1:  # Lander to the right of target
        if x_vel > -0.3:  # Allow smoother adjustment
            return 1  # Push left engine
    elif x_pos < -0.1:  # Lander to the left of target
        if x_vel < 0.3:  # Allow smoother adjustment
            return 3  # Push right engine

    # Moderate vertical velocity
    if y_vel < -0.5:
        return 2  # Push both engines upwards

    # Correct angle deviation
    if angle > 0.1:
        return 1  # Push left engine to correct
    elif angle < -0.1:
        return 3  # Push right engine to correct

    # Default state management
    return 0  # Maintain engine off when conditions are stable
