import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Define threshold values
    angle_threshold = 0.1  # Angle threshold
    x_vel_threshold = 0.1  # Horizontal velocity threshold
    y_vel_threshold = -0.5  # Negative Vertical velocity threshold
    y_vel_stabilize = -0.1  # Near zero vertical velocity threshold for stability

    # If we have landed, turn off engines
    if left_contact == 1 and right_contact == 1:
        return 0

    # Stabilize descent speed first
    if y_vel < y_vel_threshold:
        return 2  # Push both engines (upwards) to slow descent

    # Correct angular tilt only if significant
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 3  # Push right engine to counteract positive tilt
        else:
            return 1  # Push left engine to counteract negative tilt

    # Adjust horizontal drift if necessary
    if abs(x_vel) > x_vel_threshold:
        if x_vel > 0:
            return 1  # Push left engine to counteract x_vel to the right
        else:
            return 3  # Push right engine to counteract x_vel to the left

    # Fine descent stabilization if stabilization threshold is met
    if y_vel < y_vel_stabilize:
        return 2  # Push both engines lightly to stabilize descent

    # If all within thresholds, switch off engines to conserve points
    return 0