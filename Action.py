import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    if left_contact or right_contact:
        return 0  # Switch off engines if contact sensors indicate landing.

    # Vertical velocity reduction
    if y_vel < -0.4:
        return 2  # Use upward thrust to reduce high downward velocity

    # Angle correction
    if np.abs(angle) > 0.1:
        if angle > 0:
            return 1  # Use left engine to counter the clockwise rotation
        else:
            return 3  # Use right engine to counter the counter-clockwise rotation

    # Horizontal drift management
    if np.abs(x_vel) > 0.1:
        if x_vel > 0:
            return 1  # Push left engine to counter positive X velocity
        else:
            return 3  # Push right engine to counter negative X velocity

    return 0  # Default action if stable.
