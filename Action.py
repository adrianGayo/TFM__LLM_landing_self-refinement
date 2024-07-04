import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1
    y_position_threshold = 0.1
    x_position_threshold = 0.1

    # combined strategies
    if y_velocity < vertical_speed_threshold and y_position < 0.2:
        return 2  # fire both engines near the ground to reduce vertical velocity

    if abs(x_velocity) > horizontal_speed_threshold:
        if x_velocity > 0:
            return 1  # push left engine to counter right drift
        else:
            return 3  # push right engine to counter left drift

    if abs(angle) > angle_threshold:
        if angle > 0:
            return 1  # push left engine to correct positive angle
        else:
            return 3  # push right engine to correct negative angle

    if y_position > y_position_threshold or abs(x_position) > x_position_threshold:
        return 2  # fire both engines to maintain controlled descent

    if left_contact == 1 and right_contact == 1:
        return 0  # switch off engines on successful touchdown

    return 0  # stable default action
