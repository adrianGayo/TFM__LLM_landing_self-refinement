import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Threshold values for decision making
    MAX_VERTICAL_SPEED = -0.5
    MAX_HORIZONTAL_SPEED = 0.5
    MAX_TILT = 0.1

    # Correct vertical descent speed if too high
    if y_velocity < MAX_VERTICAL_SPEED:
        return 2

    # Minimize horizontal movement
    if x_velocity < -MAX_HORIZONTAL_SPEED or x_position > 0.1:
        return 1
    if x_velocity > MAX_HORIZONTAL_SPEED or x_position < -0.1:
        return 3

    # Correct tilt to be as upright as possible
    if angle > MAX_TILT:
        return 1
    if angle < -MAX_TILT:
        return 3

    # If everything is within safe limits, switch off engines
    return 0
