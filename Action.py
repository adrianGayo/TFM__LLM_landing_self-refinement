import random
def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, l_contact, r_contact = observation
    # Initialize action
    action = 0  # by default, do nothing (engines off)
    # Handling horizontal stability
    if x_pos > 0.1:  # drifted right
        action = 1  # push left engine
    elif x_pos < -0.1:  # drifted left
        action = 3  # push right engine
    # Handling vertical stability
    if y_vel < -1.0:  # descending too fast
        action = 2  # push center engine to slow down
    elif y_vel > -0.2:  # not descending (hovering)
        action = 2  # push both engines (upwards)
    # Handling angular stability
    if angle > 0.1:  # tilted to right
        action = 1  # push left engine
    elif angle < -0.1:  # tilted to left
        action = 3  # push right engine
    if l_contact and r_contact:  # landed successfully
        action = 0  # engines off
    return action