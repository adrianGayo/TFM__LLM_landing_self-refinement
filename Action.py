import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    if left_contact or right_contact:
        return 0  # Switch off engines if contact sensors indicate landing.
    if np.abs(x_vel) > 0.2:  # Horizontal velocity control
        if x_vel > 0:
            return 1  # Push left engine to counter positive X velocity
        else:
            return 3  # Push right engine to counter negative X velocity
    if np.abs(y_vel) > 0.5:  # Vertical velocity reduction
        return 2  # Use upwards thrust to reduce high downward velocity
    if np.abs(angle) > 0.1:  # Angle correction
        if angle > 0:
            return 1  # Use left engine to counter clockwise rotation
        else:
            return 3  # Use right engine to counter counter-clockwise rotation
    return 0  # Default action if stable.