def act(observation):    
    # Extract relevant information from the observation
    speed = observation[0]    
    angle = observation[2]    
    horizontal_position = observation[3]    
    vertical_position = observation[4]    
    main_engine = observation[5]    
    side_engine = observation[6]    
    center_engine = observation[7]    
    
    # Initialize action as 0 (no action)
    action = 0    
    
    # Decision-making based on observations
    # Adjust based on speed and angle
    if abs(speed) > 0.01:    
        if speed > 0:    
            action = 3 # Decelerate    
        else:    
            action = 1 # Accelerate    
    elif abs(angle) > 0.1:    
        if angle > 0:    
            action = 2 # Turn right    
        else:    
            action = 3 # Turn left    
    else:    
        # Use the main engine if not moving too fast or tilted too much
        if main_engine == 0:    
            action = 1    
            # Activate side engine to stabilize if tilted
            if side_engine > 0:    
                action = 2    
            elif side_engine < 0:    
                action = 3    
            # Avoid using center engine
            if center_engine == 1:    
                action = 0    
    
    return action