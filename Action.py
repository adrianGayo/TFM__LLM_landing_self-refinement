import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0  # Default action is to turn off all engines

    # Correct significant tilt first
    if abs(angle) > 0.2:
        action = 1 if angle > 0 else 3

    # Consistent reduction of horizontal speed
    elif abs(x_vel) > 0.2:
        action = 1 if x_vel > 0 else 3

    # Maintain slow descent continuously
    elif y_vel <= -0.1:
        action = 2  # Central engine to manage slow descent

    # Aggressive vertical velocity reduction
    elif y_vel <= -0.5:
        action = 2  # Further central engine consistent vertical control

    return action
