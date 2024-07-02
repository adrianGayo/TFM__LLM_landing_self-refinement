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

    # Correcting angle for stability as top priority if exceeds safe threshold
    if angle > 0.1:
        return 1  # Tilted right, push left engine to stabilize
    elif angle < -0.1:
        return 3  # Tilted left, push right engine to stabilize

    # If descent speed is high, balance it correctly
    if y_velocity < -0.1:
        return 2  # Push up to reduce descent speed

    # Control horizontal drift if high
    if abs(x_velocity) > 0.1:
        if x_velocity > 0:
            return 1  # Push left engine to counteract right drift
        else:
            return 3  # Push right engine to counteract left drift

    # Ensure minimal use of engines when stable
    return 0  # Default to switch off engines