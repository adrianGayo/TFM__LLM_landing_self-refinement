def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Early Phase: Large height, manage horizontal velocity primarily, stabilize descent second
    if y_position > 1.0:
        if abs(x_velocity) > 0.2:  # Prioritize horizontal stabilization
            if x_velocity > 0:
                return 1  # Left engine to slow rightward drift
            else:
                return 3  # Right engine to slow leftward drift
        elif y_velocity < -0.5:  # Control excessive downward speed
            return 2  # Center engine to reduce descent speed
        elif abs(angle) > 0.05:  # More sensitive angular corrections
            if angle > 0:
                return 3  # Right engine to correct tilt
            else:
                return 1  # Left engine to correct tilt
        else:
            return 0  # Balanced descent

    # Mid Phase: Transition closer to ground, balance lateral and vertical with more sensitivity
    elif y_position > 0.3:
        if abs(x_velocity) > 0.1:
            if x_velocity > 0:
                return 1
            else:
                return 3
        elif y_velocity < -0.3:
            return 2
        elif abs(angle) > 0.05:
            if angle > 0:
                return 3
            else:
                return 1
        else:
            return 0

    # Final Pre-landing Phase: Minor & precise tuning for near-final descent
    else:
        if abs(x_position) > 0.03:  # More precise positioning
            if x_position < 0:
                return 3
            else:
                return 1
        elif abs(y_velocity) > 0.1:
            return 2  # Gentle descent
        elif abs(angle) > 0.02:
            if angle > 0:
                return 3  # Correct tilt
            else:
                return 1  # Correct tilt
        else:
            return 0