import random

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    if left_contact or right_contact:  # any ground contact
        return 0  # engines off

    if y_vel < -0.1 or y_pos > 1.2:  # descending faster
        return 2  # push engine up for landing stability
    elif y_vel > 0.1:  # rectifying upward move
        return 0

    if abs(x_vel) > 0.2:  # proportionally correct drift
        if x_vel > 0: 
            return 1  # push left
        else: 
            return 3  # push right

    if abs(angle) > 0.1:  # correcting tilt
        if angle < 0: 
            return 3  # clockwise rectification
        else: 
            return 1  # counter-clockwise rectification

    return 2  # default be gentle downward

act_filename = "Action.py"
