import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Thresholds for decision making
    X_LIMIT = 0.5
    VERTICAL_SPEED_LIMIT = -0.5
    HORIZONTAL_SPEED_LIMIT = 0.3
    ANGLE_LIMIT = 0.1
    ANGULAR_SPEED_LIMIT = 0.1

    # Prioritize safe landing when close to ground
    if y_position < 0.5:
        if y_velocity < VERTICAL_SPEED_LIMIT:
            return 2  # Push both engines for upward thrust
        if abs(x_velocity) > HORIZONTAL_SPEED_LIMIT and abs(x_position) > X_LIMIT:
            return 1 if x_velocity > 0 else 3  # Adjust horizontal position
        if abs(angle) > ANGLE_LIMIT or abs(angular_velocity) > ANGULAR_SPEED_LIMIT:
            return 1 if angle > 0 else 3  # Stabilize tilt

    # Default control when not near ground
    if y_velocity < VERTICAL_SPEED_LIMIT:
        return 2  # Slow vertical descent
    if abs(angle) > ANGLE_LIMIT or abs(angular_velocity) > ANGULAR_SPEED_LIMIT:
        return 1 if angle > 0 else 3  # Correct tilt
    if abs(x_position) > X_LIMIT:
        return 1 if x_position > 0 else 3  # Correct horizontal drift

    return 0  # Switch off engines when stable