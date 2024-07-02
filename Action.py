def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_sensor, right_sensor = observation

    if y_pos < 0.2 and abs(x_pos) < 0.1 and abs(x_vel) < 0.1 and abs(y_vel) < 0.1:
        return 0  # Switch off engines for minor adjustments when close to the ground.
    if y_vel < -0.5:
        return 2  # Push both engines upwards to reduce descent speed.
    if x_pos > 0.1:
        return 1  # Push left engine to move left if moving too far to the right.
    if x_pos < -0.1:
        return 3  # Push right engine to move right if moving too far to the left.
    if angle > 0.1:
        return 1  # Adjust left for tilt correction.
    if angle < -0.1:
        return 3  # Adjust right for tilt correction.

    return 0  # Default action to Switch off engines to conserve fuel.

filename = 'Action.py'