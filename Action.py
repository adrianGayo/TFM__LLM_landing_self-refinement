def act(observation):
    # Extract observation parameters
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
    
    # Angle control
    if abs(angle) > 0.1:
        if angle > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine
    
    # Horizontal and vertical velocity control
    if abs(x_velocity) > 0.3:
        if x_velocity > 0:
            return 1  # Push left engine to counteract right drift
        else:
            return 3  # Push right engine to counteract left drift
    
    if y_velocity < -0.3:
        return 2  # Push both engines upwards to slow down descent
    
    return 0  # Switch off engines and drift if close to stationary