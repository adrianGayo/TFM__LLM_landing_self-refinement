import numpy as np

def act(observation):
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation

    # Constants
    ANGLE_THRESHOLD = 0.05
    MAX_Y_VELOCITY = -0.3
    SAFE_X_VELOCITY = 0.2
    MAX_ANGULAR_VELOCITY = 0.1

    # Successful landing conditions
    if left_contact == 1 and right_contact == 1:
        return 0  # The spacecraft has landed

    # Correct y_velocity
    if vy < MAX_Y_VELOCITY:
        return 2  # Apply upward thrust to control descent speed

    # Correct angular position
    if abs(angle) > ANGLE_THRESHOLD:
        if angle > 0:
            return 3  # Thrust right engine to correct left
        else:
            return 1  # Thrust left to correct right tilt

    # Correct horizontal velocity
    if abs(vx) > SAFE_X_VELOCITY:
        if vx > 0:
            return 1  # Apply thrust to left engine to reduce positive X velocity
        else:
            return 3  # Apply thrust to right engine to reduce negative X velocity

    # Correct angular velocity
    if abs(angular_velocity) > MAX_ANGULAR_VELOCITY:
        if angular_velocity > 0: 
            return 1  # Apply thrust to left engine to counteract rightward spin
        else:
            return 3  # Apply thrust to right engine to counteract leftward spin

    # Default action - engines off
    return 0