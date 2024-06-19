def act(observation):
    
    # Extract relevant information from the observation
    position_x = observation[0]
    position_y = observation[1]
    speed_x = observation[2]
    speed_y = observation[3]
    angle = observation[4]
    angular_speed = observation[5]
    side_engine_1 = observation[6]
    side_engine_2 = observation[7]
    
    score = 0
    action = 0  # Default: Do nothing
    
    # Custom logic for landing
    if position_y > 1.4:  # Ship is too high, reduce height
        if speed_y > 0.1:  # Ship is moving upward, slow it down
            action = 3  # Fire the main engine upwards
        else:
            action = 0  # Do nothing
    else:
        if angle > 0.1 or angle < -0.1:  # Ship is tilted, adjust angle
            if angle > 0.1:
                action = 1  # Rotate counter-clockwise
            else:
                action = 2  # Rotate clockwise
        else:
            action = 2  # Maintain stability while landing
        
    return action