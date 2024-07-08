import numpy as np

def act(observation):
    x_pos, y_position, x_velocity, y_velocity, angle, ang_vel, left_contact, right_contact = observation
    angle_threshold = 0.1  
    x_velocity_threshold = 0.1  
    y_velocity_threshold = -0.5

    # If both left and right contact sensors indicate landing, turn off engines.
    if left_contact == 1 and right_contact == 1:
        return 0

    # If vertical velocity is too high (descending too fast), push both engines (upwards)
    if y_velocity < y_velocity_threshold:
        return 2  # Push both engines

    # If oriented too far from vertical, correct angular tilt
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 3  # Push right engine to counteract positive tilt
        else:
            return 1  # Push left engine to counteract negative tilt

    # Adjust horizontal drift using side engines
    if abs(x_velocity) > x_velocity_threshold:
        if x_velocity > 0:
            return 1  # Push left engine to counteract right drift
        else:
            return 3  # Push right engine to counteract left drift

    # If all conditions are within acceptable thresholds, switch off engines
    return 0