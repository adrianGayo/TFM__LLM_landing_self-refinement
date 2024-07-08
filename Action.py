def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Check if landed
    if left_contact == 1 and right_contact == 1:
        return 0

    # Correct angle first
    if angle > 0.1:
        return 1
    elif angle < -0.1:
        return 3

    # Stabilize horizontal position
    if x_pos > 0.05:  # Lander to the right
        if x_vel > -0.3:
            return 1
    elif x_pos < -0.05:  # Lander to the left
        if x_vel < 0.3:
            return 3

    # Control vertical speed more actively
    if y_vel < -0.75:
        return 2

    # Default action is to have engines off if under control
    return 0
