def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Adjust horizontal velocity to be near zero
    if abs(x_velocity) > 0.2:
        if x_velocity < 0:
            return 3
        else:
            return 1

    # Reduce vertical speed if falling too fast
    if y_velocity < -0.5:
        return 2

    # Correct significant tilt
    if abs(angle) > 0.1:
        if angle < 0:
            return 1
        else:
            return 3
        
    # Prevent further tilt from engines activating too quickly
    if abs(angular_velocity) > 0.1:
        return 0  # let it stabilize momentarily

    # Ensure reduced speed and stable position and descent close to landing
    if y_position < 0.3:
        if abs(horizontal_velocity) > 0.1 or abs(x_position) > 0.1:
            if x_position < 0:
                return 3
            else:
                return 1
        else:
            return 2

    return 0 # Reverting to stabilize if all checks pass