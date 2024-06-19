def act(observations):
    if observations[6] == 1.0 and observations[7] == 0.0:
        return 0
    elif observations[6] == 1.0 and observations[7] == 1.0:
        return 3
    elif observations[2] <= 0.15 and observations[3] >= -0.25 and observations[4] <= 0.1:
        return 2
    elif observations[2] <= 0.15 and observations[3] < -0.25 and observations[3] >= -0.3:
        return 1
    elif observations[2] >= 0.15:
        return 0
    else:
        return 3