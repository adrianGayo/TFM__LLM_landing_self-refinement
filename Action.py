import numpy as np

def act(observation):
    x_pos = observation[0]
    y_pos = observation[1]
    x_vel = observation[2]
    y_vel = observation[3]
    angle = observation[4]
    ang_vel = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    # If the lander has touched down, stop engines
    if left_contact and right_contact:
        return 0

    # Function to determine if thrust up is needed, either slightly or substantially
    def thrust_up(y_vel, y_pos, significant=False):
        if significant:
            return y_vel < -0.5 or (y_pos > 0.3 and y_vel < -0.1)
        return y_vel < -0.1

    # Handling horizontal velocity
    if x_vel > 0.1:
        return 1
    elif x_vel < -0.1:
        return 3

    # Handling angle stabilization
    if angle > 0.1:
        return 3
    elif angle < -0.1:
        return 1

    # Handling vertical descent and maintaining stability
    if thrust_up(y_vel, y_pos):
        return 2

    # Handling angular velocity if it's too high
    if ang_vel > 0.1:
        return 1
    elif ang_vel < -0.1:
        return 3

    # Default to switch off engines in absence of specific controls
    return 0
