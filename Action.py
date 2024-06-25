def act(observation):
    if observation[2] < 0:
        return 3
    elif observation[2] < 0.15:
        return 2
    else:
        return 1