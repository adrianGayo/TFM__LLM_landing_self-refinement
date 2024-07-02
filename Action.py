def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    if left_contact or right_contact:  # Already landed
        return 0

    if y_pos < 0.1 and abs(x_pos) < 0.05 and abs(x_vel) < 0.1 and abs(y_vel) < 0.1 and abs(angle) < 0.1 and abs(angular_vel) < 0.1:
        return 0  # Switch off engines for gentle landing

    # Correct significant angle deviation first when necessary
    if abs(angle) >= 0.1:  # Adjusted angle threshold
        if angle > 0:
            return 3  # Push right engine to correct clockwise tilt
        else:
            return 1  # Push left engine to correct counterclockwise tilt

    # Correct horizontal velocity for alignment dynamically
    if abs(x_vel) >= 0.2:  # threshold for smoother horizontal velocity control
        if x_vel > 0:
            return 1  # Push left engine to mitigate rightward movement
        else:
            return 3  # Push right engine to mitigate leftward movement

    # Manage vertical descent velocities for smoother landing control
    if y_vel <= -0.5 and y_pos >= 0.3:  # Manage descent speed considering altitude
        return 2  # Use center engine to slow down descent progressively

    if y_pos > 0.2 and y_vel < 0:  # Use center engine upright thrust for controlled descent
        return 2  # Push both engines upwards strategically

    return 0  # Default action: switch off engines if stable