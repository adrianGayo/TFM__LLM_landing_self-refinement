import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Threshold values for decision making
    x_vel_threshold = 0.05
    angle_threshold = 0.05
    y_vel_threshold = -0.5
    close_to_ground = 0.1

    # If we have landed, turn off engines
    if left_contact == 1 and right_contact == 1:
        return 0
    
    # Correct horizontal velocity
    if abs(x_vel) > x_vel_threshold:
        if x_vel > 0:
            return 1  # push left engine to move left
        else:
            return 3  # push right engine to move right
    
    # Correct angle to upright
    if abs(angle) > angle_threshold:
        if angle > 0:
            return 1  # push left engine to tilt left
        else:
            return 3  # push right engine to tilt right
    
    # Use central engine to control descent speed and height
    if y_vel < y_vel_threshold or y_pos > close_to_ground:
        return 2  # push central engine to slow down descent
    
    # If everything is nominal, turn off engines
    return 0