def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Early Phase: Manage initial horizontal stabilization and reduce excessive descent speed
    if y_position > 1.0:
        if abs(x_velocity) > 0.2:  # Correct horizontal drift
            return 1 if x_velocity > 0 else 3
        elif abs(y_velocity) > 0.5:  # Control excessive vertical speed
            return 2
        elif abs(angle) > 0.1:  # Moderate angular corrections
            return 3 if angle > 0 else 1
        return 0

    # Mid Phase: Prioritize fine-tuning of velocity to stabilize entire descent
    elif y_position > 0.5:
        if abs(x_velocity) > 0.15:  # Adjust tighter threshold for horizontal drift
            return 1 if x_velocity > 0 else 3
        elif abs(y_velocity) > 0.3:  # Adjust for mid-range vertical speed control
            return 2
        elif abs(angle) > 0.05:
            return 3 if angle > 0 else 1
        return 0

    # Final Phase: Precision in minimal horizontal, vertical, and angular corrections
    else:
        if abs(x_position) > 0.05:  # High priority on final horizontal position
            return 3 if x_position < 0 else 1
        elif abs(y_velocity) > 0.1:
            return 2
        elif abs(angle) > 0.02:  # Tight angular corrections
            return 1 if angle < 0 else 3
        return 0