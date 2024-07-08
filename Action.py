def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # If we are too far from the landing zone horizontally, reduce horizontal speed
    if abs(x_velocity) > 0.2:
        if x_velocity < 0:
            return 3  # Fire right engine to push left (reduce negative x velocity)
        else:
            return 1  # Fire left engine to push right (reduce positive x velocity)

    # Control descent speed
    if y_velocity < -0.5:  # If falling too fast
        return 2  # Fire the center engine to slow down descent

    # Maintain upright orientation
    if abs(angle) > 0.1:
        if angle < 0:
            return 1  # Fire left engine to rotate clockwise
        else:
            return 3  # Fire right engine to rotate counterclockwise

    # Fine-tune horizontal position and descent when close to the ground
    if y_position < 0.3:
        if abs(x_position) > 0.1:
            if x_position < 0:
                return 3  # Push right to center
            else:
                return 1  # Push left to center
        else:
            return 2  # Gentle descent

    # Default action is to continue descent if no immediate adjustments are needed
    return 0  # Switch off engines for controlled descent