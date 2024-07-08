def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    # Thresholds
    x_vel_threshold = 0.2
    y_vel_threshold = 0.2
    angle_threshold = 0.1
    
    # Action selection
    if angle > angle_threshold:
        return 1  # Push left engine to correct tilt
    elif angle < -angle_threshold:
        return 3  # Push right engine to correct tilt
    elif y_vel > y_vel_threshold:
        return 2  # Push both engines to reduce vertical speed
    elif x_vel > x_vel_threshold:
        return 1  # Push left engine to reduce rightward speed
    elif x_vel < -x_vel_threshold:
        return 3  # Push right engine to reduce leftward speed
    else:
        return 0  # Switch off engines to conserve fuel and minimize score penalty
