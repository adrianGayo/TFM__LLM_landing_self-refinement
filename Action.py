import numpy as np

# Constants
MAX_HORIZONTAL_SPEED = 0.1
MAX_VERTICAL_SPEED = 0.5
MAX_ANGLE = 0.1
MAX_ANGULAR_VELOCITY = 0.1


def act(observation):
    # Unpack observations
    x, y, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Prioritize vertical speed correction
    if y_vel < -MAX_VERTICAL_SPEED:
        return 2

    # Correct horizontal velocity and angle jointly
    if abs(x_vel) > MAX_HORIZONTAL_SPEED or abs(angle) > MAX_ANGLE:
        if x_vel > 0 and angle > 0:
            return 1  # Push left engine
        elif x_vel > 0 and angle <= 0:
            return 3  # Push right engine
        elif x_vel <= 0 and angle > 0:
            return 3  # Push right engine
        else:
            return 1  # Push left engine

    # Correct angular velocity
    if abs(ang_vel) > MAX_ANGULAR_VELOCITY:
        if ang_vel > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine
    
    # Default action: switch off engines
    return 0
