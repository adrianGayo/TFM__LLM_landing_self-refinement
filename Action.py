import random

# Thresholds for decision-making
MIN_ANGLE = -0.1
MAX_ANGLE = 0.1
SAFE_Y_VELOCITY = -0.5
SAFE_X_VELOCITY = 0.1
MAX_X_VELOCITY = 0.03
MAX_ANGULAR_VELOCITY = 0.1

# Define improved decision-making function

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Successful landing conditions
    if left_contact == 1 and right_contact == 1:
        return 0  # The spacecraft has landed

    # Control vertical descent
    if y_vel < SAFE_Y_VELOCITY:
        return 2  # Apply upward thrust to control descent speed

    # Angle correction should be done gradually to avoid overcorrection
    if abs(angle) > MAX_ANGLE:
        if angle > 0:
            return 3  # Thrust right engine to correct to the left
        else:
            return 1  # Thrust left engine to correct to the right

    # Horizontal velocity adjustments also need to be gradual
    if abs(x_vel) > SAFE_X_VELOCITY:
        if x_vel > 0:
            return 1  # Apply thrust to the left engine to reduce positive X velocity
        else:
            return 3  # Apply thrust to the right engine to reduce negative X velocity

    # Control angular velocity, but do so gently
    if abs(ang_vel) > MAX_ANGULAR_VELOCITY:
        if ang_vel > 0:
            return 1  # Apply thrust to the left engine to counter the right spin
        else:
            return 3  # Apply thrust to the right engine to counter the left spin
    
    # Default action is to switch off engines when stable
    return 0