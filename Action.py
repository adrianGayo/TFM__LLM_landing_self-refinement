import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0  # default action is to switch off engines

    if y_vel < -1:  # if the vertical speed is high, slow down
        action = 2  # use main engine to reduce vertical speed
    
    if x_vel > 0.5:  # if moving too fast to the right, push left engine
        action = 1
    elif x_vel < -0.5:  # if moving too fast to the left, push right engine
        action = 3

    if abs(angle) > 0.1:  # if the spacecraft is tilted, correct the tilt
        if angle < 0:  # if tilted to the left, push right engine
            action = 3
        else:  # if tilted to the right, push left engine
            action = 1

    return action