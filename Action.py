import numpy as np

def act(observation):
    x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation
    
    # Step 1: Stabilize the angle
    if angle < -0.1:  # Tilted left
        return 3  # Fire right engine to tilt to the right
    elif angle > 0.1:  # Tilted right
        return 1  # Fire left engine to tilt to the left
    
    # Step 2: Velocity Control
    if vy < -0.5:  # Falling fast
        return 2  # Fire both engines to slow descent
    elif vy > -0.2:  # Moving upwards or slow fall
        return 0  # Switch off engines to let it fall naturally
    
    # Step 3: Centering
    if x > 0.1:  # Drifting right
        return 1  # Fire left engine for left movement
    elif x < -0.1:  # Drifting left
        return 3  # Fire right engine for right movement
    
    return 0  # all stable, turn off engines