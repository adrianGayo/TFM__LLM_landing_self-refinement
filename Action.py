import numpy as np

def act(observation):
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation

    # Constants for thresholds and actions
    ANGLE_THRESHOLD = 0.1
    ANGLE_CORRECTION = 0.05
    VELOCITY_THRESHOLD = -0.5
    X_VELOCITY_THRESHOLD = 0.2
    X_POSITION_THRESHOLD = 0.2

    # Stabilize Angle
    if angle < -ANGLE_THRESHOLD or angular_velocity < -ANGLE_CORRECTION:
        return 3  # Correct to the right
    elif angle > ANGLE_THRESHOLD or angular_velocity > ANGLE_CORRECTION:
        return 1  # Correct to the left

    # Correct Vertical Velocity
    if vy < VELOCITY_THRESHOLD:
        return 2  # Apply engines to slow down descent

    # Correct X Position and Velocity
    if x > X_POSITION_THRESHOLD or vx > X_VELOCITY_THRESHOLD:
        return 1  # Adjust left
    elif x < -X_POSITION_THRESHOLD or vx < -X_VELOCITY_THRESHOLD:
        return 3  # Adjust right

    # If left and right contact detected, we have safely landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Switch off engines and maintain position

    return 0  # Default case to switch off engines to avoid unnecessary corrections