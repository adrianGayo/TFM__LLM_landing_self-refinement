def act(observation):
    # Extract relevant information from the observation
    current_status = observation['current status']
    speed_x, speed_y, position_x, position_y, rotation, speed_rotation, main_engine, side_engine = current_status
    score = observation['score']
    action = 0  # Default action to do nothing
    
    # Modify the action based on the current_status
    if speed_y < 0.0:
        action = 3  # Fire the main engine to slow down the descent
    elif rotation < 0.0:
        action = 1  # Fire the right side engine to rotate counterclockwise
    elif rotation > 0.0:
        action = 2  # Fire the left side engine to rotate clockwise
    
    return action