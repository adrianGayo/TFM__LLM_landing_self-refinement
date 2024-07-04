import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1
    y_position_threshold = 0.1
    x_position_threshold = 0.1

    if y_velocity < vertical_speed_threshold and y_position < 0.2:
        return 2  # Fire both engines when vertical speed is too high and close to ground

    if abs(x_velocity) > horizontal_speed_threshold:
        if x_velocity > 0:
            return 1  # Push left engine to reduce right drift
        else:
            return 3  # Push right engine to reduce left drift

    if abs(angle) > angle_threshold:
        if angle > 0:
            return 1  # Push left engine to correct angle
        else:
            return 3  # Push right engine to correct angle

    if y_position > y_position_threshold or abs(x_position) > x_position_threshold:
        return 2  # Push both engines to maintain descent within constraints
    
    if left_contact == 1 and right_contact == 1:
        return 0  # Landed successfully

    return 0  # Default action is for stability without firing engines
