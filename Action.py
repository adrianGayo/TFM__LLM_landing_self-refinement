def act(observation):
    # Extract relevant information from the observation
    speed_x = observation[0]
    speed_y = observation[1]
    pos_x = observation[2]
    pos_y = observation[3]
    angle = observation[4]
    base_action = 0
    side_engine_penalty = 0.03
    center_engine_penalty = 0.3
    score = 0

    # Implement the decision-making process
    if pos_y > 0.5:
        if angle > 0.05 or angle < -0.05:
            base_action = 3  # Rotate to stabilize
            score -= center_engine_penalty
        elif pos_y > 1:
            if speed_y < -0.1:
                base_action = 1  # Slow down the descent
                score -= side_engine_penalty
        else:
            if abs(speed_x) > 0.05:
                base_action = 1  # Correct horizontal speed
                score -= side_engine_penalty
        score -= side_engine_penalty  # Continuous stabilization
    else:
        if abs(speed_x) > 0.01:
            base_action = 1  # Correct horizontal speed
            score -= side_engine_penalty
        if angle > 0.05 or angle < -0.05:
            base_action = 3  # Rotate to stabilize
            score -= center_engine_penalty

    return base_action, score