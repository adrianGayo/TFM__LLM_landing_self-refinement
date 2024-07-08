def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Priority check for a stable landed state.
    if left_contact == 1 and right_contact == 1:
        return 0 # Maintain engine off keeping it stable if landed

    # Prioritize correction of angle deviations early stabilizing for reducing positional drifts.
    if angle > 0.1:
        return 1
    elif angle < -0.1:
        return 3

    # Stabilize horizontal control under improved thresholds.
    if x_pos > 0.05 and x_vel > -0.3:
        return 1
    elif x_pos < -0.05 and x_vel < 0.3:
        return 3

    # Apply vertical corrective thrust to decelerate descent ensuring smooth approach.
    if y_vel < -0.5:
        return 2

    # Default engine-off strategy as stable state post-stabilization.
    return 0
