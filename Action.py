def act(observation):
    x_vel = observation[4]
    if x_vel > 0.5:
        return 1
    elif x_vel < -0.5:
        return 3
    else:
        return 2