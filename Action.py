def act(observation):
    if observation[4] > 0.02:
        return 3  # Fire main engine
    elif observation[2] < -0.25:
        return 2  # Fire side engine left
    elif observation[2] > 0.25:
        return 1  # Fire side engine right
    else:
        return 0  # Do nothing