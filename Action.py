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
    
    VELOCITY_THRESHOLD = 0.1
    ALTITUDE_THRESHOLD = 0.1
    
    # Control horizontal movement
    if abs(x_vel) > VELOCITY_THRESHOLD: 
        if x_vel > 0:  # Moving right too fast
            return 1  # Push left engine
        else:  # Moving left too fast
            return 3  # Push right engine
    
    # Manage angle/rotation if it's too tilted
    if abs(angle) > 0.05:
        if angle > 0:  # Tilted right
            return 3  # Push right engine to tilt left
        else:  # Tilted left
            return 1  # Push left engine to tilt right
    
    # Control descent
    if y_vel < -0.5:  # Falling too fast
        return 2  # Push both engines upwards to slow descent
    elif y_vel > -0.1 and y_pos > ALTITUDE_THRESHOLD:  # Falling slowly and still high
        return 2  # Slightly push up to slow steady descent
    
    # Default action: ensure balance and stable descent
    if abs(ang_vel) > VELOCITY_THRESHOLD:
        if ang_vel > 0:  # Rotating clockwise too fast
            return 1  # Push left engine to counteract spin
        else:  # Rotating counterclockwise too fast
            return 3  # Push right engine to counteract spin
    return 0  # Otherwise, stabilize and conserve fuel by switching off engines
