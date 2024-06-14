def act(observation):
    X_pos, Y_pos, X_vel, Y_vel, Angle, Angular_vel, Left_contact, Right_contact = observation
    # Central x-axis position
    central_x_threshold = 0.1
    # Gently landing threshold
    x_vel_threshold = 0.1
    y_vel_threshold = -0.1
    angle_threshold = 0.1
    angular_vel_threshold = 0.1

    if Left_contact == 1 or Right_contact == 1:
        return 0 
    if abs(X_pos) > central_x_threshold:
        # Correct horizontal position
        if X_pos > 0:
            return 3
        else:
            return 1
    if abs(X_vel) > x_vel_threshold:
        # Correct horizontal velocity
        if X_vel > 0:
            return 3
        else:
            return 1
    if abs(Angle) > angle_threshold or abs(Angular_vel) > angular_vel_threshold:
        # Correct angle
        return 2    # Fire main engine to stabilize
    if Y_vel < y_vel_threshold:
        # Correct vertical velocity
        return 2     # Fire main engine
    return 0