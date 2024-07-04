def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    if left_contact == 1 and right_contact == 1:
        # Landed successfully
        return 0

    if abs(angle) > 0.1:
        if angle > 0:
            return 1  # Push left engine to correct angle
        else:
            return 3  # Push right engine to correct angle
    
    if abs(x_vel) > 0.5:
        if x_vel > 0:
            return 1  # Push left engine to reduce right drift
        else:
            return 3  # Push right engine to reduce left drift

    if y_vel < -0.5:
        return 2  # Push both engines to slow descent
    
    if y_pos < 0.1 and abs(x_vel) < 0.5 and abs(y_vel) < 0.5 and abs(angle) < 0.1:
        return 0  # Switch off engines to prepare for landing
    
    return 2  # Default action is to push both engines for stability and control