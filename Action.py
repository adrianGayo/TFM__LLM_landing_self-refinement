import random

# Define thresholds for decision-making
MIN_ANGLE = -0.1
MAX_ANGLE = 0.1
MAX_ANGULAR_VELOCITY = 0.1
SAFE_Y_VELOCITY = -0.3
SAFE_X_VELOCITY = 0.03
SAFE_Y_POSITION = 1.0


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Successful landing conditions
    if left_contact == 1 and right_contact == 1:
        return 0  # The spacecraft has landed

    # Manage angular conditions first
    if abs(angle) > MAX_ANGLE or abs(ang_vel) > MAX_ANGULAR_VELOCITY:
        if angle > 0 or ang_vel > 0:
            return 3  # Thrust right engine to correct to the left or counter right spin
        elif angle < 0 or ang_vel < 0:
            return 1  # Thrust left engine to correct to the right or counter left spin

    # Control vertical descent speed
    if y_vel < SAFE_Y_VELOCITY:
        return 2  # Apply upward thrust to manage descent

    # Fine-tune lateral movements minimally
    if abs(x_vel) > SAFE_X_VELOCITY:
        if x_vel > 0:  # Apply left engine thrust to reduce positive X velocity
            return 1
        elif x_vel < 0:  # Apply right engine thrust to reduce negative X velocity
            return 3

    return 0  # Default action is to switch off engines
