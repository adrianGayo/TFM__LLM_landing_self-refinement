import random

def act(observation):
    # Unpack observation variables
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Touchdown logic
    if left_contact or right_contact:  # Any contact with ground
        return 0  # Engines Off

    # Manage horizontal velocity
    if x_vel > 0.1:  # drifting right
        return 1  # left engine
    elif x_vel < -0.1:  # drifting left
        return 3  # right engine

    # Vertical descent control
    if y_vel < -0.1:  # descending
        return 2  # both engines up
    elif y_vel > 0.1:  # moving up fast
        return 0  # engines off

    # Adjust Angle
    if angle < -0.1:  # left tilt
        return 3  # clockwise
    elif angle > 0.1:  # right tilt
        return 1  # counter clockwise

    # Final descent stabilization
    if abs(x_vel) < 0.1 and abs(y_vel) < 0.2 and abs(angle) < 0.1:  # slow and steady
        return 0

    return 2  # default action for gentle downward force
