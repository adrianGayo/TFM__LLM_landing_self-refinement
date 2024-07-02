import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0  # Default action is to turn off all engines
    if y_vel < -0.2:  # Too fast horizontal
        action = 2 # Trigger both engines to slow down
        if x_vel > 0.3:  # Drifting to the right
            action = 1 # Correct drifting to the right using left engine
        elif x_vel < -0.3:  # Drifting to the left
            action = 3 # Correct drifting to the left using right engine
    elif abs(angle) > 0.5:  # Large angle deviation
        if angle > 0:
            action = 1 # Correct angle if tilted to the right
        else:
            action = 3 # Correct angle if tilted to the left
    elif y_vel < -1.0:  # Too fast vertical
        action = 2 # Trigger both engines to slow down
    return action
