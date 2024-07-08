import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # If we have landed, turn off engines
    if left_contact == 1 and right_contact == 1:
        return 0
    
    # Correct horizontal velocity
    if x_vel > 0.1:
        return 1  # push left engine to move left
    elif x_vel < -0.1:
        return 3  # push right engine to move right
    
    # Correct angle to upright
    if angle > 0.1:
        return 1  # tilt left using left engine
    elif angle < -0.1:
        return 3  # tilt right using right engine
    
    # Use central engine to control descent speed
    if y_vel < -0.5:
        return 2  # push central engine to slow down
    
    # If everything is nominal, turn off engines
    return 0