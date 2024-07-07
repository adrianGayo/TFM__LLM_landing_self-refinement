def act(current_status):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_sensor, right_sensor = current_status
    score = 0
    
    # Adjust actions based on current status for optimal landing
    if y_pos > 1.0:
        # Apply actions to correct position for Y axis
        score -= 0.3
        action = 1
    elif y_pos < -0.5:
        # Apply actions to correct position for Y axis
        score -= 0.3
        action = 3
    else:
        if x_pos > 0.1:
            # Apply actions to adjust position for X axis
            score -= 0.2
            action = 3
        elif x_pos < -0.1:
            # Apply actions to adjust position for X axis
            score -= 0.2
            action = 1
        else:
            action = 0  # Switch off engines when close to the landing zone
    
    return action, score
