import random

# Define thresholds for decision-making
MIN_ANGLE = -0.1
MAX_ANGLE = 0.1
MAX_Y_VELOCITY = -0.1
SAFE_Y_VELOCITY = -0.5
SAFE_X_VELOCITY = 0.1
MAX_X_VELOCITY = 0.03
MAX_ANGULAR_VELOCITY = 0.1

# Define decision-making function

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Successful landing conditions
    if left_contact == 1 and right_contact == 1:
        return 0  # The spacecraft has landed

    # Urgent corrective actions for high descent velocity
    if y_vel < SAFE_Y_VELOCITY:
        return 2  # Apply upward thrust to control descent speed

    # Correct significant angles
    if abs(angle) > MAX_ANGLE:
        if angle > 0:
            return 3  # Thrust right engine to correct to the left
        else:
            return 1  # Thrust left engine to correct to the right
    
    # Correct high horizontal velocities
    if abs(x_vel) > SAFE_X_VELOCITY:
        if x_vel > 0:
            return 1  # Apply thrust to the left engine to reduce positive X velocity
        else:
            return 3  # Apply thrust to the right engine to reduce negative X velocity

    # Correct angular velocity exceeding the safe threshold
    if abs(ang_vel) > MAX_ANGULAR_VELOCITY:
        if ang_vel > 0:
            return 1  # Apply thrust to the left engine to counteract the right spin
        else:
            return 3  # Apply thrust to the right engine to counteract the left spin

    return 0  # Switch off engines to conserve fuel and minimize sudden movements