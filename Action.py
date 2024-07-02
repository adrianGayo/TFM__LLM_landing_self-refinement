def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    if left_contact or right_contact:  # Already landed
        return 0
    
    if y_pos < 0.1 and abs(x_pos) < 0.05 and abs(x_vel) < 0.1 and abs(y_vel) < 0.1 and abs(angle) < 0.1 and abs(angular_vel) < 0.1:
        return 0  # Switch off engines for gentle landing
    
    if abs(angle) > 0.1:  # Correct angle
        if angle > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine
    
    if y_pos > 0.1:  # Control descent
        return 2  # Push both engines upwards to slow down descent
    
    if abs(x_vel) > 0.1:  # Control horizontal speed
        if x_vel > 0:
            return 1  # Push left engine to reduce rightward velocity
        else:
            return 3  # Push right engine to reduce leftward velocity

    if abs(angular_vel) > 0.1:  # Correct angular velocity
        if angular_vel > 0:
            return 1  # Push left engine to counter clockwise spin
        else:
            return 3  # Push right engine to counter clockwise spin

    return 0  # Default action: switch off engines