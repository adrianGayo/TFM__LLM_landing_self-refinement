def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Early Phase: Manage horizontal velocity and vertical speed primarily, stabilize descent secondarily
    if y_position > 1.0:
        if abs(x_velocity) > 0.2:  # Prioritize horizontal stabilization
            if x_velocity > 0:
                return 1  # Left engine to slow rightward drift
            else:
                return 3  # Right engine to slow leftward drift
        elif y_velocity < -0.5:  # Control excessive downward speed
            return 2  # Center engine to decrease descent speed
        elif abs(angle) > 0.1:   # Moderate angular correction if necessary
            if angle > 0:
                return 3  # Right engine to correct tilt
            else:
                return 1  # Left engine to correct tilt
        else:
            return 0  # Balanced descent

    # Mid Phase: Balance lateral and vertical sensitivities closer to ground
    elif y_position > 0.3:
        if abs(x_velocity) > 0.1:
            if x_velocity > 0:
                return 1
            else:
                return 3
        elif y_velocity < -0.3:
            return 2  # Slow descent
        elif abs(angle) > 0.05:  # Minimize tilt
            if angle > 0:
                return 3
            else:
                return 1
        else:
            return 0

    # Final Phase: Precise near-final descent tuning
    else:
        if abs(x_position) > 0.05:
            if x_position < 0:
                return 3  # Correct minor left adjustments
            else:
                return 1  # Correct minor right adjustments
        elif abs(y_velocity) > 0.1:
            return 2  # Reduce vertical speed
        elif abs(angle) > 0.02:
            if angle < 0:
                return 1
            else:
                return 3
        else:
            return 0  # Final balanced descent