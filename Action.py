def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants for safe landing
    safe_angle = 0.1  # Safe angle range for landing
    safe_angle_vel = 0.1  # Safe angular velocity
    safe_vertical_speed = -0.2  # Safe vertical descent speed
    safe_horizontal_speed = 0.1  # Safe horizontal speed

    # If the spacecraft has already landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines

    # Correct angle and reduce angular velocity first
    if abs(angle) > safe_angle or abs(ang_vel) > safe_angle_vel:
        if angle > safe_angle or ang_vel > safe_angle_vel:
            return 3  # Push right engine to correct left tilt
        elif angle < -safe_angle or ang_vel < -safe_angle_vel:
            return 1  # Push left engine to correct right tilt
    
    # Control vertical speed
    if y_vel < safe_vertical_speed:
        return 2  # Push both engines to slow descent

    # Control horizontal drift only if angle and angular velocity adjustments are minor
    if abs(angle) < safe_angle and abs(ang_vel) < safe_angle_vel:
        if x_vel > safe_horizontal_speed:
            return 1  # Push left engine to move left
        elif x_vel < -safe_horizontal_speed:
            return 3  # Push right engine to move right

    return 0  # Default action is turning off the engines