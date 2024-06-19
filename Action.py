def act(obs):
    # Analyzing observations
    speed_x = obs[0]
    speed_y = obs[1]
    pos_x = obs[2]
    pos_y = obs[3]
    angle = obs[4]
    left_engine = obs[5]
    main_engine = obs[6]
    right_engine = obs[7]
    score = obs[8]
    # Decision-making
    if pos_x < 0:
        return 3  # Fire left engine to correct position
    elif pos_x > 0:
        return 1  # Fire right engine to correct position
    else:
        return 2  # Fire main engine to stabilize
