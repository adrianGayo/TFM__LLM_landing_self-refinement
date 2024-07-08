import math

# Define the act function to make better decisions based on the observations

def act(observation):
    # Extract observations
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Define acceptable landing angle and velocities
    ideal_angle = 0.05  # Small angle deviation allowed
    max_y_vel = -0.5  # Max downward velocity allowed for safe landing
    max_x_vel = -0.1  # Max horizontal velocity allowed

    # If landed, or both contacts are true, do nothing (Action 0)
    if left_contact and right_contact:
        return 0
    
    # If approaching the ground rapidly, thrust both engines
    if y_vel < max_y_vel:
        return 2
    
    # Correct horizontal velocity by adjusting side engines
    if x_vel > max_x_vel:
        return 1  # Push left engine
    elif x_vel < -max_x_vel:
        return 3  # Push right engine

    # Correct angle
    if angle > ideal_angle:
        return 1  # Push left engine
    elif angle < -ideal_angle:
        return 3  # Push right engine

    # If all parameters are within range, maintain descent with controlled y thrust
    if max_x_vel >= x_vel >= -max_x_vel and max_y_vel >= y_vel >= -max_y_vel and -ideal_angle <= angle <= ideal_angle:
        if y_vel < 0:  # Continue to thrust upwards gently if descending
            return 2
        else:
            return 0  # Otherwise maintain current state

    # Default action
    return 0