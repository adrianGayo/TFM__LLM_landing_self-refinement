# Revised strategy implementation
import numpy as np

def act(observation):
    X_position, Y_position, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are made, engines off

    # Angle control: Highest priority
    if angle > 0.1:  # if tilted right,
        return 1  # push left engine
    elif angle < -0.1:  # if tilted left
        return 3  # push right engine

    # Control X velocity and position
    if X_velocity > 0.1:  # Moving right,
        return 1  # push left engine
    elif X_velocity < -0.1:  # Moving left,
        return 3  # push right engine

    # Vertical control
    if Y_velocity < -0.3:  # descending too fast,
        return 2  # push both engines
    elif Y_velocity < -0.1 and Y_position > 0.3:  # safe speed but still descending, high altitude
        return 0  # turn off engines
    elif Y_velocity > -0.1 and Y_position < 0.3:  # approaching ground quickly
        return 2  # soften the descent

    return 0  # Default to engines off if all conditions are stable
