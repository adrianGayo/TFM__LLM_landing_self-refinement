import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Correcting horizontal movement (X position and velocity)
    if x_pos > 0.02 and x_vel > 0.15:
        return 1  # Push left engine to move left
    elif x_pos < -0.02 and x_vel < -0.15:
        return 3  # Push right engine to move right

    # Correcting angular movement (Angle and Angular velocity)
    if angle > 0.1:
        return 1  # Push left engine to rotate clockwise
    elif angle < -0.1:
        return 3  # Push right engine to rotate counter-clockwise

    # Correcting vertical movement (Y position and velocity)
    if y_vel < -0.2:
        return 2  # Push both engines to slow down descent
    
    return 0  # Switch off engines to conserve fuel