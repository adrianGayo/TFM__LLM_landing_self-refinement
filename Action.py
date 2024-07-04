import numpy as np

def act(observation):
    X_pos, Y_pos, X_vel, Y_vel, angle, angular_velocity, left_contact, right_contact = observation
    
    # Condition-specific Actions
    if Y_vel < -0.3:
        return 2  # Push both engines (Upwards) to reduce descending speed
    elif abs(angle) > 0.1:
        if angle > 0:
            return 1 # Push left engine to correct right tilt
        else:
            return 3 # Push right engine to correct left tilt
    elif abs(X_vel) > 0.2:
        if X_vel > 0:
            return 1 # Push left engine to correct right drift
        else:
            return 3 # Push right engine to correct left drift
    else:
        return 0  # Switch off engines if all conditions are within safe bounds
