import numpy as np


def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Parameter thresholds
    X_LIMIT = 0.5
    VERTICAL_VELOCITY_LIMIT = -0.5
    X_VELOCITY_LIMIT = 0.5
    ANGLE_LIMIT = 0.1
    ANGULAR_VELOCITY_LIMIT = 0.1

    # Prioritize stabilization as landing approaches
    if y_position < 0.5:
        # Slow down descent if falling too fast
        if y_velocity < VERTICAL_VELOCITY_LIMIT:
            return 2
        # Correct horizontal drift
        if abs(x_velocity) > X_VELOCITY_LIMIT and abs(x_position) > X_LIMIT:
            return 1 if x_velocity > 0 else 3
        # Minimize tilt
        if abs(angle) > ANGLE_LIMIT or abs(angular_velocity) > ANGULAR_VELOCITY_LIMIT:
            return 1 if angle > 0 else 3

    # General control for early descent
    if y_velocity < VERTICAL_VELOCITY_LIMIT:
        return 2
    if abs(angle) > ANGLE_LIMIT or abs(angular_velocity) > ANGULAR_VELOCITY_LIMIT:
        return 1 if angle > 0 else 3
    if abs(x_position) > X_LIMIT:
        return 1 if x_position > 0 else 3

    return 0