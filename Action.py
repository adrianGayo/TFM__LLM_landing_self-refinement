def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    
    if left_contact == 1 or right_contact == 1:  # Successful landing
        return 0

    # Stabilize angle
    if angle < -0.1:
        return 3  # fire right engine
    elif angle > 0.1:
        return 1  # fire left engine

    # Stabilize X speed if too high
    if x_velocity > 0.3:
        return 3  # fire right engine
    elif x_velocity < -0.3:
        return 1  # fire left engine

    # If descending too fast
    if y_velocity < -0.3:
        return 2  # fire main engine to slow down descent

    # If within safe parameters, turn off engines
    return 0