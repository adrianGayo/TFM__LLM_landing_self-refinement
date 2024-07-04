import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1
    high_vertical_speed_threshold = -1.0  # higher threshold for high vertical speed
    high_horizontal_speed_threshold = 0.3  # higher threshold for high horizontal speed
    high_angle_threshold = 0.2  # higher threshold for high angle

    if y_velocity < high_vertical_speed_threshold:
        return 2  # fire both engines to slow down significantly
    elif abs(x_velocity) > high_horizontal_speed_threshold:
        return 2  # fire both engines to slow down significantly
    elif y_velocity < vertical_speed_threshold:
        return 2  # fire both engines to control descent speed
    elif angle < -high_angle_threshold:
        return 1  # fire the left engine to correct a significant left tilt
    elif angle > high_angle_threshold:
        return 3  # fire the right engine to correct a significant right tilt
    elif abs(angle) > angle_threshold:
        if angle < 0:
            return 1  # fire the left engine for minor left tilt
        else:
            return 3  # fire the right engine for minor right tilt
    else:
        return 0  # switch off engines for stable descent
