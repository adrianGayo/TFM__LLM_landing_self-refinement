def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = observation

    # Parameters for deciding about vertical thrust (center engine)
    max_y_vel = -0.1
    max_x_vel = 0.1
    max_angle = 0.1

    # Apply upward thrust if descending too quickly or horizontally too off
    if y_vel < max_y_vel or x_vel > max_x_vel or x_vel < -max_x_vel:
        return 2  # Push both engines upward
    
    # Apply left or right engine thrust if angle is deviating or to correct slight horizontal velocities
    if angle > max_angle or x_vel > max_x_vel:
        return 1  # Push left engine
    elif angle < -max_angle or x_vel < -max_x_vel:
        return 3  # Push right engine

    # Switch off engines if in control
    return 0