def act(observation):
    # Unpacking observation elements
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Control strategy based on observations
    # Control angle and angular velocity first
    if angle > 0.1:  # If tilted to the right
        return 1  # Fire left engine to rotate left
    elif angle < -0.1:  # If tilted to the left
        return 3  # Fire right engine to rotate right
    elif ang_vel > 0.5:  # If rotating clockwise fast
        return 1  # Fire left engine to reduce rotation to left
    elif ang_vel < -0.5:  # If rotating counter-clockwise fast
        return 3  # Fire right engine to reduce rotation to right
    
    # Control horizontal velocity next
    if x_vel > 0.5:  # Moving too fast to the right
        return 1  # Fire left engine to reduce horizontal velocity to right
    elif x_vel < -0.5:  # Moving too fast to the left
        return 3  # Fire right engine to reduce horizontal velocity to left
    
    # Finally, control vertical descent
    if y_vel < -1.0:  # Descending too fast
        return 2  # Fire both engines to slow descent
    
    # Default action is to switch off engines to preserve fuel (scores)
    return 0
