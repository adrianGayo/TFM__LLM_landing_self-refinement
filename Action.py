def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    ANGLE_THRESHOLD = 0.1   # radians, acceptable angle deviation
    VELOCITY_THRESHOLD = 0.1 # m/s, acceptable velocity deviation
    DOWNWARD_VEL_LIMIT = -0.5 # m/s, acceptable downward velocity
    SAFE_ANGLE_VEL = 0.1   # radians/sec, acceptable angular velocity

    # Priority 1: Control descent speed
    if y_vel < DOWNWARD_VEL_LIMIT:
        return 2  # Push both engines to slow descent

    # Priority 2: Correct angle and reduce angular velocity
    if angle > ANGLE_THRESHOLD or ang_vel > SAFE_ANGLE_VEL:
        return 3  # Push right engine to stabilize
    elif angle < -ANGLE_THRESHOLD or ang_vel < -SAFE_ANGLE_VEL:
        return 1  # Push left engine to stabilize

    # Priority 3: Manage horizontal drift
    if x_vel > VELOCITY_THRESHOLD:
        return 1  # Push left to reduce rightward drift
    elif x_vel < -VELOCITY_THRESHOLD:
        return 3  # Push right to reduce leftward drift

    # Endgame: when everything is stable, switch off engines
    return 0  # Switch off engines