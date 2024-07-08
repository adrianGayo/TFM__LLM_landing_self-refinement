import numpy as np

# Constants
MAX_HORIZONTAL_SPEED = 0.1
MAX_VERTICAL_SPEED = 0.5
MAX_ANGLE = 0.1
MAX_ANGULAR_VELOCITY = 0.1

def act(observation):
    # Unpack observations
    x, y, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Use both engines if descending too fast
    if y_vel < -MAX_VERTICAL_SPEED:
        return 2
    
    # Correct horizontal velocity
    if abs(x_vel) > MAX_HORIZONTAL_SPEED:
        if x_vel > 0:
            return 3  # Push right engine
        else:
            return 1  # Push left engine
    
    # Correct angle
    if abs(angle) > MAX_ANGLE:
        if angle > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine
    
    # Correct angular velocity
    if abs(ang_vel) > MAX_ANGULAR_VELOCITY:
        if ang_vel > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine
    
    # Default action: switch off engines
    return 0
