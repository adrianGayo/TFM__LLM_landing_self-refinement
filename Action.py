import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1
    high_vertical_speed_threshold = 0.6  # new threshold for high vertical speed
    high_horizontal_speed_threshold = 0.3  # new threshold for high horizontal speed
    high_angle_threshold = 0.2  # new threshold for high angle

    if abs(y_velocity) > high_vertical_speed_threshold or abs(x_velocity) > high_horizontal_speed_threshold:
        return 2  # fire both engines to slow down
    elif angle < -high_angle_threshold:
        return 1  # fire the left engine to correct a significant left tilt
    elif angle > high_angle_threshold:
        return 3  # fire the right engine to correct a significant right tilt
    elif y_velocity < vertical_speed_threshold:
        return 2  # fire both engines to control descent speed
    elif abs(x_velocity) > horizontal_speed_threshold:
        if x_velocity > 0:
            return 1  # fire the left engine if moving too fast to the right
        else:
            return 3  # fire the right engine if moving too fast to the left
    elif angle < -angle_threshold:
        return 1  # fire the left engine to correct a small left tilt
    elif angle > angle_threshold:
        return 3  # fire the right engine to correct a small right tilt
    else:
        return 0  # switch off engines for stable descent
