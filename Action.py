def act(env_logs):
    for log in env_logs:
        if log['current status'][0] < 0:
            return 3  # Fire right engine
        elif log['current status'][0] > 0:
            return 1  # Fire left engine
        elif log['current status'][3] > -0.35:
            return 2  # Fire both engines (upwards)
        else:
            return 0  # Switch off engines