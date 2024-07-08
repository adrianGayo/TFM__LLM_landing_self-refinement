def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Early Phase: Large height, manage horizontal velocity primarily, stabilize descent second
    if y_position > 1.0:
        if abs(x_velocity) > 0.2:  # Prioritize horizontal stabilization
            return 1 if x_velocity > 0 else 3
        elif y_velocity < -0.5:  # Control excessive downward speed
            return 2
        elif abs(angle) > 0.1:  # Moderate angular correction if necessary
            return 3 if angle > 0 else 1
        else:
            return 0  # Balanced descent

    # Mid Phase: Transition closer to ground, balance lateral and vertical with more sensitivity
    elif y_position > 0.5:
        if abs(x_velocity) > 0.15:
            return 1 if x_velocity > 0 else 3
        elif abs(y_velocity) > 0.3:
            return 2
        elif abs(angle) > 0.05:
            return 3 if angle > 0 else 1
        else:
            return 0

    # Final Pre-landing Phase: Minor & precise tuning for near-final descent
    else:
        if abs(x_position) > 0.05:
            return 3 if x_position < 0 else 1
        elif abs(y_velocity) > 0.1:
            return 2
        elif abs(angle) > 0.02:
            return 1 if angle < 0 else 3
        else:
            return 0