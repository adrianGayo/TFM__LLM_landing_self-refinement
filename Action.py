import random

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    # Define thresholds for actions
    threshold_x_vel = 0.1
    threshold_y_vel = -0.1
    threshold_angle = 0.1
    threshold_ang_vel = 0.1

    if left_contact or right_contact:
        return 0

    if abs(angle) > threshold_angle or abs(ang_vel) > threshold_ang_vel:
        if angle > 0 or ang_vel > 0:
            return 1  # Push left to counteract right tilt or angular velocity
        else:
            return 3  # Push right to counteract left tilt or angular velocity
    
    if y_vel < threshold_y_vel or y_pos > 1.0:
        return 2  # Push both engines upwards to reduce the fall speed
    
    if x_vel > threshold_x_vel:
        return 1  # Push left engine to reduce rightward horizontal velocity
    elif x_vel < -threshold_x_vel:
        return 3  # Push right engine to reduce leftward horizontal velocity
    
    return 0  # Switch off engines by default