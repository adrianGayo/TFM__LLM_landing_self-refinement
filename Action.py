import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    # Action priorities based on observed values 
    if left_contact > 0 or right_contact > 0: 
        return 0  # When contact is made, keep engines off, assume stable landing
    if y_vel < -0.3:  # Control descent speed
        return 2  # Push both engines to slow descent
    if np.abs(angle) > 0.1:  # Stabilize tilt
        if angle > 0: 
            return 1  # Use left engine to counteract right tilt
        else: 
            return 3  # Use right engine to counteract left tilt
    if np.abs(x_vel) > 0.5:  # Correct horizontal movement
        if x_vel > 0:
            return 1  # Use left engine to push left, counteract right movement
        else:
            return 3  # Use right engine to push right, counteract left movement
    return 0  # Default to turning off engines when relatively stable