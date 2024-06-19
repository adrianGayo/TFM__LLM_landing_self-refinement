def act(observation):
    # Extract relevant information from the observation
    position_x = observation[0]
    position_y = observation[1]
    speed_x = observation[2]
    speed_y = observation[3]
    angle = observation[4]
    angular_speed = observation[5]
    left_engine = observation[6]
    right_engine = observation[7]
    # Initialize action to 0
    action = 0
    # Logic for the decision-making process
    if angle > 0.05 or angle < -0.05:
        # If the spacecraft is tilted, correct the angle with the left or right engine
        if angle > 0.05:
            action = 2  # Fire left engine
        else:
            action = 1  # Fire right engine
    elif speed_y < 0:
        # If the spacecraft is moving upwards, fire the main engine
        action = 3
    elif speed_y < -1:
        # If the spacecraft is moving downwards too quickly, fire the main engine
        action = 3
    else:
        # Otherwise, keep the action as 0 (no engine firing)
        action = 0
    return action