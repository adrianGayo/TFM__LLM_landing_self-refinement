import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    safe_angle = 0.1  # Define safe angle range for landing
    max_safe_speed = -0.2  # Define safe vertical speed range for landing
    max_horizontal_drift = 0.1  # Define safe horizontal speed at landing
    max_ang_vel = 0.1  # Define safe angular velocity at landing

    # If already contacted the ground
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines, we're landed

    # Correct Orientation
    if angle > safe_angle or ang_vel > max_ang_vel:
        return 3  # Push right engine to rotate left
    elif angle < -safe_angle or ang_vel < -max_ang_vel:
        return 1  # Push left engine to rotate right

    # Control horizontal drift
    if x_vel > max_horizontal_drift:
        return 1  # Push left engine to move left
    elif x_vel < -max_horizontal_drift:
        return 3  # Push right engine to move right

    # Control vertical speed
    if y_vel < max_safe_speed:  # If descending too fast
        return 2  # Push both engines to slow down
    else:
        return 0  # Otherwise, turn off engines to save fuel

    return 0  # Default action is doing nothing