def act(observation):
    # Extracting the necessary observations
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Goal is to balance out velocities and position smoothly as we approach the surface
    # Correcting horizontal velocity if needed
    if x_vel > 0.1 and angle > -0.1:  # Moving to right, slight left tilt
        return 1  # Fire left engine
    elif x_vel < -0.1 and angle < 0.1:  # Moving to left, slight right tilt
        return 3  # Fire right engine
    # Tilt correction
    elif angle > 0.1:  # Correct rightward angle tilt
        return 1  # Fire left engine
    elif angle < -0.1:  # Correct leftward angle tilt
        return 3  # Fire right engine
    # Correcting vertical velocity if falling too fast or need final descent stabilizing force
    elif y_vel < -0.1:
        return 2  # Fire upward engine, adjust y-velocity
    # If stable enough (all params optimal), engines off to let graceful descent
    return 0