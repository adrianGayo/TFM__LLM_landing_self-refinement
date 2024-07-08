import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    # Define thresholds based on successful landings
    stop_y_threshold = -0.3  # Threshold for acceptable y velocity
    tilt_threshold = 0.1  # Threshold for acceptable tilt

    # Use upward engines to slow down descent
    if y_vel < stop_y_threshold:
        return 2
    
    # Control horizontal velocity based on x position
    if x_pos > 0.1:
        return 1  # Push left to correct right drift
    elif x_pos < -0.1:
        return 3  # Push right to correct left drift

    # Control tilt by counter-acting angle with side engines
    if angle > tilt_threshold:
        return 1  # Push left to correct right tilt
    elif angle < -tilt_threshold:
        return 3  # Push right to correct left tilt

    # In the default case, turn off all engines
    return 0