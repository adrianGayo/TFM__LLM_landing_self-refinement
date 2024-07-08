import random

# Define thresholds for decision-making
MIN_ANGLE = -0.1
MAX_ANGLE = 0.1

MAX_Y_VELOCITY = -0.1

MAX_X_VELOCITY = -0.03

# Define decision-making function

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    if left_contact == 1 and right_contact == 1:
        return 0  # The spacecraft has landed

    if y_vel < MAX_Y_VELOCITY:
        return 2  # Apply upward thrust to slow descent

    if abs(angle) > MAX_ANGLE or ang_vel != 0:
        if angle < 0:
            return 3  # Apply thrust to the right engine to correct angle
        else:
            return 1  # Apply thrust to the left engine to correct angle
    
    if abs(x_vel) > MAX_X_VELOCITY:
        if x_vel > 0:
            return 1  # Apply left engine thrust to reduce positive X velocity
        else:
            return 3  # Apply right engine thrust to reduce negative X velocity

    return 0  # Switch off engines to avoid unnecessary thrust