def act(obs):
    # Extract required values from observations
    speed_x = obs[0]
    speed_y = obs[1]
    position_x = obs[2]
    position_y = obs[3]
    angle = obs[4]
    landing_x = obs[5]
    landing_y = obs[6]
    side_engine = obs[7]
    center_engine = obs[8]
    # Decide action based on observations
    if position_y < 1.2:
        return 3  # Turn off all engines
    if speed_y < -0.15:
        return 1  # Fire the main engine
    if angle < -0.25 or angle > 0.25:
        return 0  # Turn off all engines
    if side_engine == 1:
        return 0
    return 2  # Fire the side engines