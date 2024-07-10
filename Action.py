def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants for safe landing
    safe_angle = 0.05  # Angle within this range is considered safe
    safe_angle_vel = 0.05  # Safe angular velocity
    safe_vertical_speed = -0.2  # Safe vertical descent speed
    safe_horizontal_speed = 0.2  # Safe horizontal speed

    # If already on the ground
    if left_contact == 1 and right_contact == 1:
        return 0  # Engines off

    # If the angle is safe, manage velocities
    if abs(angle) <= safe_angle and abs(ang_vel) <= safe_angle_vel:
        if y_vel < safe_vertical_speed:  # Too fast downward
            return 2  # Upward thrust

        if x_vel > safe_horizontal_speed:  # Move left
            return 1  # Push left engine
        elif x_vel < -safe_horizontal_speed:  # Move right
            return 3  # Push right engine

    # Correct angle if out of bounds
    if angle > safe_angle:
        return 3  # Push right engine to correct left tilt
    elif angle < -safe_angle:
        return 1  # Push left engine to correct right tilt

    if ang_vel > safe_angle_vel:
        return 1  # Correct positive angular velocity
    elif ang_vel < -safe_angle_vel:
        return 3  # Correct negative angular velocity

    return 0  # Default action: engines off