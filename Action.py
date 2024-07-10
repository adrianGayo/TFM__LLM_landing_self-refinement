import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    safe_angle = 0.1  # Define what is considered a safe angle range for landing
    max_safe_speed = -0.1  # Define what is considered a safe vertical speed range for landing
    max_horizontal_drift = 0.02  # Define what is considered a safe horizontal speed at landing

    # If already contacted the ground
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines, we're landed

    # If the spacecraft is tilting too much to the left or right, correct it by using side thrusters
    if angle > safe_angle:
        return 3  # Push right engine to rotate left
    elif angle < -safe_angle:
        return 1  # Push left engine to rotate right

    # If horizontal velocity is too high, counteract it:
    if x_vel > max_horizontal_drift:
        return 1  # Push left engine to move left
    elif x_vel < -max_horizontal_drift:
        return 3  # Push right engine to move right

    # Control the vertical speed
    if y_vel < max_safe_speed:  # If descending too fast
        return 2  # Push both engines to slow down
    else:
        return 0  # Otherwise, turn off engines to save fuel

    return 0  # Default action is doing nothing