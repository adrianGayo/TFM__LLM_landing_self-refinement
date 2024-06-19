def act(observation):
    if observation[2] < 0.1:
        return 1  # Fire the main engine to slow down
    elif observation[2] > 0.1 and observation[3] > -0.3:
        return 2  # Keep using the main engine to maintain altitude
    else:
        return 3  # Use side engines to adjust the position and prepare for landing