def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    # Define thresholds for taking certain actions
    ANGLE_TOLERANCE = 0.1  # radians
    VEL_TOLERANCE = 0.1  # m/s
    if abs(angle) > ANGLE_TOLERANCE:
        if angle > 0:
            return 1  # Push left engine to counteract tilt
        else:
            return 3  # Push right engine to counteract tilt
    elif abs(y_vel) > VEL_TOLERANCE:
        return 2  # Use center engine to slow vertical descent
    elif abs(x_vel) > VEL_TOLERANCE:
        if x_vel > 0:
            return 1  # Push left engine to counteract positive horizontal velocity
        else:
            return 3  # Push right engine to counteract negative horizontal velocity
    else:  # If everything is within the desired range, switch off engines
        return 0
