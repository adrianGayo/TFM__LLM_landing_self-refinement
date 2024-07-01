def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    # More proactive stabilization
    if angle < -0.1 or angular_vel < -0.5:
        return 1
    elif angle > 0.1 or angular_vel > 0.5:
        return 3
    
    # More frequent horizontal control checks
    if x_pos < -0.1 or x_vel < -0.5:
        return 3
    elif x_pos > 0.1 or x_vel > 0.5:
        return 1

    # Prioritize vertical stabilization
    if y_vel < -0.2:
        return 2

    # Default action if conditions are met
    return 0