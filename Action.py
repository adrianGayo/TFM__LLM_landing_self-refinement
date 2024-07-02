import numpy as np

def act(observation):
    x_pos = observation[0]
    y_pos = observation[1]
    x_vel = observation[2]
    y_vel = observation[3]
    angle = observation[4]
    ang_vel = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    # Define thresholds for better control
    VELOCITY_THRESHOLD = 0.1
    ALTITUDE_THRESHOLD = 0.1

    # If already landed, switch off engines
    if left_contact and right_contact:
        return 0

    # Main descent control
    if y_vel < -VELOCITY_THRESHOLD:  # Falling too fast
        return 2
    elif ang_vel > VELOCITY_THRESHOLD:  # Rotating too fast clockwise
        return 1
    elif ang_vel < -VELOCITY_THRESHOLD:  # Rotating too fast counterclockwise
        return 3
    if abs(x_vel) > VELOCITY_THRESHOLD:  # Moving horizontally too fast
        if x_vel > 0:
            return 1
        else:
            return 3
    if abs(angle) > 0.1:  # Angle is off-centered
        if angle > 0:
            return 3
        else:
            return 1
    # Safe descending
    if y_vel > -0.1 and y_pos > ALTITUDE_THRESHOLD:  # Slightly pushing up for controlled descent
        return 2
    # Rest
    return 0
