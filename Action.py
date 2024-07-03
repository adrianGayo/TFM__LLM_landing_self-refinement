import numpy as np

def act(observation):
    X_position, Y_position, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are made, engines off
    
    # Horizontal control
    if X_position > 0.1:  # if too far right
        return 1  # push left engine
    elif X_position < -0.1:  # if too far left
        return 3  # push right engine

    # Vertical control
    if Y_velocity < -0.1:  # descending too fast
        return 2  # push both engines
    elif Y_velocity > -0.1 and Y_position < 0.3:  # reducing speed as close to ground
        return 0  # turn off engines

    # Angle control
    if angle > 0.1:  # if tilted right
        return 1  # push left engine
    elif angle < -0.1:  # if tilted left
        return 3  # push right engine

    return 2  # Default to pushing both engines
