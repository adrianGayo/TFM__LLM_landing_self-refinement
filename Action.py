def act(observation):
    X_position, Y_position, X_velocity, Y_velocity, Angle, Angular_velocity, Left_contact, Right_contact = observation
    
    # Vertical and horizontal stabilization
    if Y_velocity < -0.5:  # Descending too fast
        if Angle > 0.1:  # If tilted to the right
            return 1  # Activate left engine to counteract
        elif Angle < -0.1:  # If tilted to the left
            return 3  # Activate right engine to counteract
        return 2  # Otherwise, activate both engines to slow down descent
    
    if X_velocity > 0.25:  # Moving too fast to the right
        return 1  # Activate left engine to counteract
    elif X_velocity < -0.25:  # Moving too fast to the left
        return 3  # Activate right engine to counteract

    # Small adjustments
    if abs(Angle) > 0.1:  # Correct angle if tilted
        if Angle > 0:
            return 1
        else:
            return 3
        
    # If close to safe, switch off engines
    if abs(X_velocity) < 0.1 and abs(Y_velocity) < 0.5 and abs(Angle) < 0.1:
        return 0  # Switch off engines to save fuel
    
    # Otherwise, maintain course
    return 0