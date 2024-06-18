def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    
    # Stabilize angle
    if angle < -0.1:
        return 3  # fire right engine
    elif angle > 0.1:
        return 1  # fire left engine

    # Stabilize X speed if too high
    if x_velocity > 0.5:
        return 3  # fire right engine
    elif x_velocity < -0.5:
        return 1  # fire left engine

    # If descending too fast
    if y_velocity < -0.5:
        return 2  # fire main engine to slow down descent

    # If within safe parameters, turn off engines
    return 0