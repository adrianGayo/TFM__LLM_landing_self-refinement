import numpy as np

# Constants
MAX_HORIZONTAL_SPEED = 0.1
MAX_VERTICAL_SPEED = 0.5
MAX_ANGLE = 0.1
MAX_ANGULAR_VELOCITY = 0.1
CENTRAL_ENGINE_PENALTY = 0.3
SIDE_ENGINE_PENALTY = 0.03
SUCCESSFUL_LANDING_SCORE_THRESHOLD = 200


def act(observation):
    # Unpack observations
    x, y, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Prioritize vertical speed correction if descending rapidly
    if y_vel < -MAX_VERTICAL_SPEED:
        return 2

    # Balance horizontal velocity correction and angle correction
    if abs(x_vel) > MAX_HORIZONTAL_SPEED or abs(angle) > MAX_ANGLE:
        # If the angle is significant, prioritize angle correction
        if abs(angle) > MAX_ANGLE:
            if angle > 0:  # Tilted right
                return 1  # Push left engine
            else:  # Tilted left
                return 3  # Push right engine
        else:
            if x_vel > 0:  # Moving right
                return 3  # Push right engine
            else:  # Moving left
                return 1  # Push left engine

    # Correct angular velocity if needed
    if abs(ang_vel) > MAX_ANGULAR_VELOCITY:
        if ang_vel > 0:
            return 1  # Push left engine
        else:
            return 3  # Push right engine
    
    # Default action: switch off engines
    return 0
