def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants for safe landing
    safe_angle = 0.1  # Angle within this range is considered safe
    safe_angle_vel = 0.1  # Safe angular velocity
    safe_vertical_speed = -0.2  # Safe vertical descent speed
    safe_horizontal_speed = 0.2  # Safe horizontal speed

    # If the spacecraft has already landed
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines

    # Performing necessary corrections
    if abs(angle) > safe_angle:  # Correct the angle if necessary
        if angle > 0:
            return 3  # Push right engine to correct left tilt
        elif angle < 0:
            return 1  # Push left engine 
    if abs(ang_vel) > safe_angle_vel:  # Correct angular velocity
        if ang_vel > 0:
            return 3  # Push right engine
        elif ang_vel < 0:
            return 1  # Push left engine
    if abs(x_vel) > safe_horizontal_speed:  # Control horizontal drift
        if x_vel > 0:
            return 1  # Push left engine to counter right drift
        elif x_vel < 0:
            return 3  # Push right engine 
    if y_vel < safe_vertical_speed:  # Control descent speed
        return 2  # Push both engines to slow descent

    return 0  # Default action is turning off engines
