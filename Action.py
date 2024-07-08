def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # First, check if the lander has landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable 
    
    # Stabilize horizontal position to fine-grain
    if x_pos > 0.1:  # Lander is to the right of target
        if x_vel > -0.1:  # Fine-tuned tolerant velocity
            return 1  # Push left engine to adjust
    elif x_pos < -0.1:  # Lander is to the left of target
        if x_vel < 0.1:  # Fine-tuned tolerant velocity
            return 3  # Push right engine to adjust

    # Stabilize vertical velocity with balance and fine tuning
    if y_vel < -0.5:
        return 2  # Push both engines upwards to slow descent

    # Correct moderate angles
    if angle > 0.1:  # Tilted to the right within moderate
        return 1  # Push left to correct
    elif angle < -0.1:  # Tilted to the left within moderate
        return 3  # Push right to correct
    
    return 0