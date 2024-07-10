import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Check for landing contact first.
    if left_contact or right_contact:
        return 0

    # Vertical descent control: ensure descent is gentle
    if y_vel < -0.5:
        return 2

    # Horizontal velocity control: mitigate drift
    if np.abs(x_vel) > 0.2:
        if x_vel > 0:
            return 1
        elif x_vel < 0:
            return 3

    # Angular velocity control: neutralize rotation
    if np.abs(angle) > 0.1:
        if angle > 0:
            return 1
        else:
            return 3

    # Switch off engines by default if stable
    return 0