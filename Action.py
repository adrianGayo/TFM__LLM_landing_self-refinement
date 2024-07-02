def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Correct horizontal position if far from center
    if abs(x_pos) > 0.1:
        if x_pos > 0:
            return 1  # Push left engine to move left
        else:
            return 3  # Push right engine to move right
    
    # Correct angle if too tilted
    if abs(angle) > 0.1:
        if angle > 0:
            return 3  # Push right engine to tilt left
        else:
            return 1  # Push left engine to tilt right
    
    # Correct vertical velocity
    if y_vel < -0.2:
        return 2  # Push both engines upwards to decelerate
    
    # If all conditions are satisfactory, switch off engines
    return 0