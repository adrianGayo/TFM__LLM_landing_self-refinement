import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants for decision-making thresholds
    ANGLE_THRESHOLD = 0.1  # radians
    HORIZONTAL_VELOCITY_THRESHOLD = 0.1  # m/s
    VERTICAL_VELOCITY_THRESHOLD = -0.2  # m/s
    POSITION_THRESHOLD = 0.1  # meters

    # If the spacecraft is close to landing and aligned, shut off engines
    if (abs(x_pos) < POSITION_THRESHOLD and abs(x_vel) < HORIZONTAL_VELOCITY_THRESHOLD and 
        abs(y_vel) < VERTICAL_VELOCITY_THRESHOLD and abs(angle) < ANGLE_THRESHOLD):
        return 0  # Switch off engines
    
    # Correct horizontal position if drifting
    if x_pos > POSITION_THRESHOLD:
        return 1  # Push left engine to move right
    elif x_pos < -POSITION_THRESHOLD:
        return 3  # Push right engine to move left
    
    # Reduce horizontal velocity if too high
    if x_vel > HORIZONTAL_VELOCITY_THRESHOLD:
        return 3  # Push right engine to reduce positive x velocity
    elif x_vel < -HORIZONTAL_VELOCITY_THRESHOLD:
        return 1  # Push left engine to reduce negative x velocity
    
    # If descending too quickly, push both engines to slow down
    if y_vel < VERTICAL_VELOCITY_THRESHOLD:
        return 2

    # Correct angle
    if angle > ANGLE_THRESHOLD:
        return 1  # Push left engine to reduce positive angle
    elif angle < -ANGLE_THRESHOLD:
        return 3  # Push right engine to reduce negative angle

    # Default action to push both engines to maintain control
    return 2