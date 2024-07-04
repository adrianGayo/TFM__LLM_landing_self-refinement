def act(data):
    if data['logs'][-1]['current status'][1] > 0:  # Check if Y position is above landing zone
        return 3  # Apply right engine
    elif data['logs'][-1]['current status'][1] < 0:  # Check if Y position is below landing zone
        return 2  # Apply both engines upwards
    else:
        return 0  # Switch off engines