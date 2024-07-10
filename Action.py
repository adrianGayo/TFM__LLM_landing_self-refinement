import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    safe_angle = 0.1  # Safe angle range for landing
    max_safe_vertical_speed = -0.15  # Safe vertical speed range for landing
    max_horizontal_drift = 0.05  # Safe horizontal speed range
    max_ang_vel = 0.1  # Safe angular velocity

    # Ensure the spacecraft has landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines

    # Correct Orientation if out of safe angle/ang_vel
    if abs(angle) > safe_angle or abs(ang_vel) > max_ang_vel:
        if angle > safe_angle or ang_vel > max_ang_vel:
            return 3  # Push right engine
        elif angle < -safe_angle or ang_vel < -max_ang_vel:
            return 1  # Push left engine

    # Control vertical speed
    if y_vel < max_safe_vertical_speed:
        return 2  # Push both engines to slow down

    # Control horizontal drift
    if abs(angle) < safe_angle and abs(ang_vel) < max_ang_vel:
        if x_vel > max_horizontal_drift:
            return 1  # Push left engine to move left
        elif x_vel < -max_horizontal_drift:
            return 3  # Push right engine to move right

    return 0  # Default action is doing nothing