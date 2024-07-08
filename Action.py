def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    ANGLE_THRESHOLD = 0.1   # radians, acceptable angle deviation
    VELOCITY_THRESHOLD = 0.1 # m/s, acceptable velocity deviation
    DOWNWARD_VEL_LIMIT = -0.5 # m/s, acceptable downward velocity
    SAFE_ANGLE_VEL = 0.1   # radians/sec, acceptable angular velocity

    # Step 1: Strong immediate descent control
    if y_vel < DOWNWARD_VEL_LIMIT and not left_contact and not right_contact:
        return 2  # Push both engines to slow descent

    # Step 2: Simultaneous correction for angle and descent stabilization
    if y_vel >= DOWNWARD_VEL_LIMIT:
        if (abs(angle) > ANGLE_THRESHOLD or abs(ang_vel) > SAFE_ANGLE_VEL):
            if angle > ANGLE_THRESHOLD or ang_vel > SAFE_ANGLE_VEL:
                return 3  # Push right engine to stabilize
            elif angle < -ANGLE_THRESHOLD or ang_vel < -SAFE_ANGLE_VEL:
                return 1  # Push left engine to stabilize

    # Step 3: Horizontal drift management conducted concurrently
    if abs(x_vel) > VELOCITY_THRESHOLD:
        if x_vel > VELOCITY_THRESHOLD:
            return 1  # Push left to reduce rightward drift
        elif x_vel < -VELOCITY_THRESHOLD:
            return 3  # Push right to reduce leftward drift

    # Switch off engines when stability is achieved in all dimensions
    return 0  # Switch off engines