import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Decision rules based on observation criteria
    if y_pos > 1.0 or (y_vel < -0.3 and x_pos > 0.05):
        return 2  # Push both engines to gain height or reduce descent speed
    elif x_pos < -0.05 and angle < 0.1:
        return 1  # Push left engine to move right
    elif x_pos > 0.05 and angle > -0.1:
        return 3  # Push right engine to move left
    elif angle > 0.1:
        return 1  # Push left engine to stabilize angle
    elif angle < -0.1:
        return 3  # Push right engine to stabilize angle
    else:
        return 0  # Switch off engines

    return action