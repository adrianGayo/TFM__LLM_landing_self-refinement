import numpy as np

thresholds = {
    'x_velocity': 0.1,  # Threshold for acceptable horizontal velocity
    'y_velocity': -0.5,  # Threshold for acceptable vertical velocity
    'angle': 0.1,  # Threshold for acceptable angle
    'angular_velocity': 0.1  # Threshold for acceptable angular velocity
}

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation
    
    if right_contact == 1 and left_contact == 1:
        return 0  # On the ground, no action needed

    # Counteract angular velocity to reduce tilt
    if angular_vel > thresholds['angular_velocity']:
        return 1  # Push left engine to counteract clockwise rotation
    elif angular_vel < -thresholds['angular_velocity']:
        return 3  # Push right engine to counteract counter-clockwise rotation

    # Stabilize descent if falling too fast
    if y_vel < thresholds['y_velocity']:
        return 2  # Both engines to slow down descent

    # Stabilize horizontal movement
    if x_vel > thresholds['x_velocity']:
        return 1  # Push left engine to reduce rightward movement
    elif x_vel < -thresholds['x_velocity']:
        return 3  # Push right engine to reduce leftward movement

    # Minor adjustments and default action
    return 0  # Default action is to switch off engines and observe