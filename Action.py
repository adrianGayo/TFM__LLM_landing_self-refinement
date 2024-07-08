import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Define threshold values
    pos_threshold = 0.1  # Horizontal position threshold
    x_vel_threshold = 0.05  # Horizontal velocity threshold
    y_vel_threshold = -0.1  # Vertical velocity threshold
    angle_threshold = 0.1  # Angle threshold

    # If we have landed, turn off engines
    if left_contact == 1 and right_contact == 1:
        return 0

    # Prioritize angle correction
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 3 # Push right engine to counteract positive tilt
        else:
            return 1 # Push left engine to counteract negative tilt

    # Correct horizontal position and velocity
    if abs(x_vel) > x_vel_threshold or abs(x_pos) > pos_threshold:
        if x_vel > 0 or x_pos > 0.1:  # Move left if moving or positioned right
            return 1  # Push left engine
        elif x_vel < 0 or x_pos < -0.1:  # Move right if moving or positioned left
            return 3  # Push right engine

    # Adjust vertical descent
    if y_vel < y_vel_threshold or y_pos > 0.1:
        return 2  # Push both engines (upward thrust)

    # Switch off engines when stable
    return 0