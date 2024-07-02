import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0  # Default action is to turn off all engines

    # Correct large tilt first
    if abs(angle) > 0.3: 
        action = 1 if angle > 0 else 3

    # Reduce horizontal speed if angled
    if abs(x_vel) > 0.2 and abs(angle) < 0.3:
        action = 1 if x_vel > 0.2 else 3

    # Consistent vertical speed correction
    if y_vel <= -0.1:
        action = 2  # Apply central engine to reduce descent speed

    # Violent vertical velocity reduction
    if y_vel <= -0.5:  # Higher thresholds for vertical velocity
        action = 2

    # Balance decision if both horizontal and angle corrected
    if abs(x_vel) < 0.2 and abs(angle) < 0.3 and y_vel <= -0.1:
        action = 2

    return action
