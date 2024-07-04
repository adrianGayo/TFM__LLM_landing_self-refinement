def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Dictionary for possible actions
    actions = {'off': 0, 'left': 1, 'up': 2, 'right': 3}

    # Prioritize reducing y_velocity and x_velocity
    action = actions['off']

    # If falling too quickly, engage the main engine
    if y_vel < -0.5:
        action = actions['up']

    # Adjust horizontal movements
    elif x_vel > 0.1:   # Moving right
        action = actions['left']
    elif x_vel < -0.1:  # Moving left
        action = actions['right']

    # Correct angular position
    if angle > 0.1:      # Tilted right
        action = actions['left']
    elif angle < -0.1:   # Tilted left
        action = actions['right']

    return action