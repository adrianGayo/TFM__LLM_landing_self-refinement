import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Constants for decision making
    X_LIMIT = 0.5
    VERTICAL_VELOCITY_LIMIT = -0.5
    ANGLE_LIMIT = 0.1
    HORIZONTAL_VELOCITY_LIMIT = 0.1
    ANGULAR_VELOCITY_LIMIT = 0.1

    # If we are close to landing, consider precision controlling
    if y_position < 0.5:
        # Stabilize downward speed
        if y_velocity < VERTICAL_VELOCITY_LIMIT:
            return 2  # Push both engines to slow descent
        if np.abs(x_velocity) > HORIZONTAL_VELOCITY_LIMIT and np.abs(x_position) > X_LIMIT:
            return 1 if x_velocity > 0 else 3  # Correct horizontal drift
        # Correct angle if it's tilted
        if np.abs(angle) > ANGLE_LIMIT or np.abs(angular_velocity) > ANGULAR_VELOCITY_LIMIT:
            return 1 if angle > 0 else 3

    # Default actions for general control considering priority
    if y_velocity < VERTICAL_VELOCITY_LIMIT:
        return 2  # Slow descent generally
    if np.abs(angle) > ANGLE_LIMIT or np.abs(angular_velocity) > ANGULAR_VELOCITY_LIMIT:
        return 1 if angle > 0 else 3  # Correct angle
    if np.abs(x_position) > X_LIMIT:
        return 1 if x_position > 0 else 3  # Correct horizontal position

    return 0  # Switch off engines if everything is within controlled limits