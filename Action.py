import numpy as np


def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Thresholds
    angle_threshold = 0.1  # We want to keep the angle as small as possible
    x_velocity_threshold = 0.1  # Small horizontal movement
    y_velocity_threshold = -0.5  # Controlled decent

    # Control Angle
    if angle > angle_threshold:
        return 1  # Push left engine to tilt right
    elif angle < -angle_threshold:
        return 3  # Push right engine to tilt left

    # Control Horizontal Movement
    if x_velocity > x_velocity_threshold:
        return 1  # Push left engine to reduce rightward movement
    elif x_velocity < -x_velocity_threshold:
        return 3  # Push right engine to reduce leftward movement

    # Reduce Descent Speed when falling too fast
    if y_velocity < y_velocity_threshold:
        return 2  # Push both engines to slow down descent

    # If everything is stable, shut off engines
    return 0