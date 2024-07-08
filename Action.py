def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Check if the lander has landed and halt all engines.
    if left_contact == 1 and right_contact == 1:
        return 0
    
    # Stabilize horizontal positioning.
    if x_pos > 0.1:
        if x_vel > -0.3:  # Allowable velocity threshold via left engine.
            return 1
    elif x_pos < -0.1:
        if x_vel < 0.3:  # Allowable velocity threshold via right engine.
            return 3
    
    # Apply engine thrust to control descent speed vertically.
    if y_vel < -0.5:
        return 2

    # Correct moderate angular deviations maintaining stability (reduction via thresholds).
    if angle > 0.1:
        return 1
    elif angle < -0.1:
        return 3

    # Default engine-off if conditions appear stable.
    return 0