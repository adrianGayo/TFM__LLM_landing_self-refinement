import random

def act(observation):
    # Unpack observation variables
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Touchdown logic
    if left_contact or right_contact:  # Any contact
        return 0  # Engines off

    # Manage X velocity
    if x_vel > 0.1:  # drift right
        return 1  # push left
    elif x_vel < -0.1:  # drift left
        return 3  # push right

    # Vertical descent control
    if y_vel < -0.1:  # descending faster
        return 2  # engines upwards
    elif y_vel > 0.1:  # moving up too fast
        return 0  # engines off

    # Adjust angle
    if angle < -0.1:  # incline left
        return 3  # clockwise correction
    elif angle > 0.1:  # incline right
        return 1  # counter-clockwise

    # Final aggressive control
    if abs(x_vel) < 0.1 and abs(y_vel) < 0.2:
        return 0  # stabilize completely

    # Default random adjustment
    return random.randint(0, 3)
