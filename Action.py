import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Decision thresholds
    X_LIMIT = 0.5
    Y_VELOCITY_LIMIT = -0.5
    X_VELOCITY_LIMIT = 0.5
    ANGLE_LIMIT = 0.1
    ANGULAR_VELOCITY_LIMIT = 0.1

    # Close to landing, emphasize precision control
    if y_position < 0.5:
        if y_velocity < Y_VELOCITY_LIMIT:
            return 2  # Push both engines to slow descent
        if abs(x_velocity) > X_VELOCITY_LIMIT and abs(x_position) > X_LIMIT:
            return 1 if x_velocity > 0 else 3  # Correct horizontal drift
        if abs(angle) > ANGLE_LIMIT or abs(angular_velocity) > ANGULAR_VELOCITY_LIMIT:
            return 1 if angle > 0 else 3  # Correct tilt

    # General control
    if y_velocity < Y_VELOCITY_LIMIT:
        return 2  # Slow descent with both engines
    if abs(angle) > ANGLE_LIMIT or abs(angular_velocity) > ANGULAR_VELOCITY_LIMIT:
        return 1 if angle > 0 else 3  # Correct angle
    if abs(x_position) > X_LIMIT:
        return 1 if x_position > 0 else 3  # Adjust horizontal position

    return 0  # Switch off engines if within controlled limits