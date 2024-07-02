def act(observation):
    x_position = observation[0]
    y_position = observation[1]
    x_velocity = observation[2]
    y_velocity = observation[3]
    angle = observation[4]
    angular_velocity = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    # If already landed successfully
    if left_contact == 1 and right_contact == 1:
        return 0

    # Control descent speed
    if y_velocity < -0.1:
        return 2  # Push upward engine to slow down descent

    # Minimize horizontal speed; prioritize stopping horizontal drift
    if abs(x_velocity) > 0.1:
        if x_velocity > 0:
            return 1  # Push left engine to move left
        else:
            return 3  # Push right engine to move right

    # Correct tilts
    if abs(angle) > 0.1:
        if angle > 0:
            return 1  # Right tilt; push left to stabilize
        else:
            return 3  # Left tilt; push right to stabilize

    # Default to not using any engines if stable
    return 0