def act(observation):
    X_position, Y_position, X_velocity, Y_velocity, Angle, Angular_velocity, Left_contact, Right_contact = observation

    # If both legs hit the ground with minimal speed and tilt, cut off engines
    if Left_contact and Right_contact:
        return 0
    
    # Correct horizontal drift
    if X_position > 0.1 and X_velocity > -0.1:
        return 1  # Push left engine to move left
    elif X_position < -0.1 and X_velocity < 0.1:
        return 3  # Push right engine to move right
    
    # Correct vertical speed
    if Y_velocity < -0.4:
        return 2  # Push both engines to slow descent
    
    # Correct angle rotation
    if Angle > 0.1 and Angular_velocity > -0.1:
        return 1  # Push left engine to rotate left
    elif Angle < -0.1 and Angular_velocity < 0.1:
        return 3  # Push right engine to rotate right

    # Default action is to stop engines if above conditions are not met
    return 0