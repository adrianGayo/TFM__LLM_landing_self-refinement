import random

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    if left_contact or right_contact:  # If contact sensors are triggered, we assume landing
        return 0  # Idle to stop engines
    
    if abs(x_vel) > 0.2:  # Stabilize horizontal velocity
        if x_vel > 0:
            return 3  # Fire left engine to reduce x velocity
        else:
            return 1  # Fire right engine to reduce x velocity
    
    if abs(angle) > 0.1 or abs(angular_vel) > 0.1:  # Stabilize orientation
        if angle > 0 or angular_vel > 0:
            return 1  # Fire right engine to rotate counter-clockwise
        else:
            return 3  # Fire left engine to rotate clockwise
            
    if y_vel < -0.3:  # Stabilize vertical velocity
        return 2  # Fire main engine to reduce y velocity
    
    if abs(x_vel) < 0.2 and abs(y_vel) < 0.3 and abs(angle) < 0.1 and abs(angular_vel) < 0.1:
        return 0  # Idle if everything is stabilized

    return 2  # Default action is to fire the main engine to stabilize descent