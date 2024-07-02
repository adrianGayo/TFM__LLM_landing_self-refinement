import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    # If any contact sensor is triggered, assume landed
    if left_contact == 1 or right_contact == 1:
        return 0
    
    # Adjust vertical speed
    if y_vel < -0.3:
        return 2
    
    # Adjust horizontal speed
    if x_vel > 0.5:
        return 1
    elif x_vel < -0.5:
        return 3
    
    # Adjust angle
    if angle > 0.1:
        return 1
    elif angle < -0.1:
        return 3
    
    return 0