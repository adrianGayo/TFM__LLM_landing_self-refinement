import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Thresholds for control
    vertical_speed_threshold = -0.3
    horizontal_speed_threshold = 0.1
    angle_threshold = 0.1
    y_position_threshold = 0.1
    x_position_threshold = 0.1
    
    if left_contact == 1 and right_contact == 1:
        return 0  # Landed successfully

    if abs(angle) > angle_threshold and y_velocity < vertical_speed_threshold:
        # Use two engines for balance and moderate thrust
        return 2
    
    if abs(angle) > 0.05:
        if angle > 0:
            return 1  # Slight correction for the angle
        elif angle < 0:
            return 3
            
    if abs(x_velocity) > horizontal_speed_threshold:
        if x_velocity > 0:
            return 1
        elif x_velocity < 0:
            return 3
            
    if y_velocity < vertical_speed_threshold or abs(y_position) > y_position_threshold:
        return 2  # Throttle with 2 engines near the ground
    
    return 0
