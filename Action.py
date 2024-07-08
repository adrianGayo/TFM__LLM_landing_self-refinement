import numpy as np

def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Prioritize reducing horizontal speed if it's above a smaller threshold
    if abs(x_velocity) > 0.1:
        if x_velocity > 0:
            return 1  # Fire left engine to reduce rightward drift
        else:
            return 3  # Fire right engine to reduce leftward drift

    # Control descent speed earlier if falling moderately fast
    if y_velocity < -0.3:
        return 2  # Fire the center engine to slow down descent

    # Maintain upright orientation if angle deviates significantly
    if abs(angle) > 0.1:
        if angle > 0:
            return 3  # Fire right engine to correct tilt
        else:
            return 1  # Fire left engine to correct tilt

    # Fine-tune horizontal position and descent when close to the ground
    if y_position < 0.5:
        if abs(x_position) > 0.1:
            if x_position < 0:
                return 3  # Push right to center
            else:
                return 1  # Push left to center
        elif abs(y_velocity) > 0.2:  # Ensure more vertical control near the surface
            return 2  # Gentle descent

    # Default to switching off engines
    return 0  # Controlled descent