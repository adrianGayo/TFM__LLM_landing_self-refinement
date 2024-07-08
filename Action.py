import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    # Conditions to fire both engines
    if y_vel < -0.8 or (y_pos < 1.0 and y_vel < -0.1):
        return 2  # Fire both engines to decrease descent speed
    
    # Correct angle if spacecraft is tilted
    if angle > 0.1:
        return 1  # Fire left engine to correct tilt to the left
    elif angle < -0.1:
        return 3  # Fire right engine to correct tilt to the right
    
    # Maintain position if horizontal velocity is non-zero
    if x_vel > 0.2:
        return 1  # Move left to correct rightward drift
    elif x_vel < -0.2:
        return 3  # Move right to correct leftward drift
    
    # Default action is to switch off engines if conditions are stable
    return 0