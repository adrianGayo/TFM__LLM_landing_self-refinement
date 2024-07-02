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

    # Control horizontal velocity
    if x_vel > 0.1:  # Moving too fast to the right
        return 1  # Push left engine to slow down movement
    elif x_vel < -0.1:  # Moving too fast to the left
        return 3  # Push right engine to slow down movement

    # Control angle (keep near 0)
    if angle > 0.1:  # Tilted right
        return 3  # Push right engine to counteract tilt
    elif angle < -0.1:  # Tilted left
        return 1  # Push left engine to counteract tilt

    # Control descent velocity
    if y_vel < -0.5:  # Falling too quickly
        return 2  # Push both engines to slow down descent
    if y_pos > 0.3 and y_vel < -0.1:  # High enough for gentle control
        return 2  # Keep descent controlled

    # If somewhat stable, conserve fuel
    if abs(x_vel) < 0.1 and abs(y_vel) < 0.1:
        return 0

    # Default safe state
    if abs(ang_vel) > 0.1:  # Rotation correction if it's too fast
        if ang_vel > 0:  # Clockwise rotation
            return 1  # Push left engine
        else:  # Counterclockwise rotation
            return 3  # Push right engine
    return 0
