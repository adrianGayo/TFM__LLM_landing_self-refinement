def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Define thresholds
    x_pos_threshold = 0.02
    x_vel_threshold = 0.1
    y_vel_threshold = 0.5
    angle_threshold = 0.1
    ang_vel_threshold = 0.1

    # First, check if the lander has landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off all engines to stay stable
    
    # Stabilize horizontal position
    if x_pos > x_pos_threshold:  # Lander is to the right of target
        if x_vel > -x_vel_threshold:
            return 1  # Push left engine
    elif x_pos < -x_pos_threshold:  # Lander is to the left of target
        if x_vel < x_vel_threshold:
            return 3  # Push right engine

    # Stabilize vertical velocity and angular velocity
    if y_vel < -y_vel_threshold:
        return 2  # Push both engines upwards
    elif angle > angle_threshold:  # Tilted to the right
        return 1  # Push left to correct
    elif angle < -angle_threshold:  # Tilted to the left
        return 3  # Push right to correct
    elif ang_vel > ang_vel_threshold:  # Rotating too fast clockwise
        return 1  # Push left to correct rotation
    elif ang_vel < -ang_vel_threshold:  # Rotating too fast counterclockwise
        return 3  # Push right to correct rotation

    # If all conditions are met, keep engines off
    return 0
