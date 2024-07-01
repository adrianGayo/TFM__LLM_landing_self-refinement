def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    # Step 1: Stabilize the Spacecraft
    if angular_vel < -0.5 or angle < -0.1:  # Rotating too fast left or tilted left
        return 1
    if angular_vel > 0.5 or angle > 0.1:  # Rotating too fast right or tilted right
        return 3
    
    # Step 2: Reduce Horizontal Velocity
    if x_vel < -0.5:  # Moving too fast to the left
        return 3
    if x_vel > 0.5:  # Moving too fast to the right
        return 1
    
    # Step 3: Prepare for Landing (Control Vertical Velocity)
    if y_vel < -0.5:  # Falling too fast
        return 2

    return 0