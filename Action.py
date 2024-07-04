import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1

    if y_velocity < vertical_speed_threshold or abs(x_velocity) > horizontal_speed_threshold:
        return 2  # fire both engines
    elif angle < -angle_threshold:
        return 1  # fire the left engine to correct the angle
    elif angle > angle_threshold:
        return 3  # fire the right engine to correct the angle
    else:
        return 0  # switch off engines
