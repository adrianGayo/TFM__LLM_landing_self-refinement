def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    ANGLE_THRESHOLD = 0.1    # radians, acceptable angle deviation
    VELOCITY_THRESHOLD = 0.1 # m/s, acceptable velocity deviation
    DOWNWARD_VEL_LIMIT = -0.5 # m/s, acceptable downward velocity

    # Check for stabilization needs
    if angle < -ANGLE_THRESHOLD:
        return 1  # Push left engine to stabilize
    elif angle > ANGLE_THRESHOLD:
        return 3  # Push right engine to stabilize
    elif ang_vel < -ANGLE_THRESHOLD:
        return 1
    elif ang_vel > ANGLE_THRESHOLD:
        return 3

    # Control descent speed
    if y_vel < DOWNWARD_VEL_LIMIT:
        return 2  # Push both engines to slow descent

    # Control horizontal drift
    if x_vel > VELOCITY_THRESHOLD:
        return 1  # Push left to reduce rightward drift
    elif x_vel < -VELOCITY_THRESHOLD:
        return 3  # Push right to reduce leftward drift

    # Ideally, when stable
    return 0 # Switch off engines