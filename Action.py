def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Landed condition
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable

    # Correct angle first
    if angle > 0.1:
        return 1  # Push left engine to correct
    elif angle < -0.1:
        return 3  # Push right engine to correct
    
    # Stabilize horizontal position
    if x_pos > 0.05:  # Lander to the right of target
        if x_vel > -0.5:
            return 1  # Push left engine
    elif x_pos < -0.05:  # Lander to the left of target
        if x_vel < 0.5:
            return 3  # Push right engine
    
    # Stabilize vertical velocity
    if y_vel < -0.5:
        return 2  # Push both engines upwards
    
    # Default action
    return 0
