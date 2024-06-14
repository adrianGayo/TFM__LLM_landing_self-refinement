def act(observation):
    X_pos, Y_pos, X_vel, Y_vel, Angle, Angular_vel, Left_contact, Right_contact = observation

    # Initialize constants
    central_x_threshold = 0.1
    x_vel_threshold = 0.1
    y_vel_threshold = -0.1
    angle_threshold = 0.1
    angular_vel_threshold = 0.1

    # If the spaceship has landed, stop all maneuvers
    if Left_contact == 1 or Right_contact == 1:
        return 0
    
    # Maintain level by correcting angle first
    if abs(Angle) > angle_threshold or abs(Angular_vel) > angular_vel_threshold:
        return 2  # Fire main engine to stabilize

    # Correct horizontal velocity
    if abs(X_vel) > x_vel_threshold:
        if X_vel > 0:
            return 3  # Fire left engine
        else:
            return 1  # Fire right engine

    # Correct vertical velocity
    if Y_vel < y_vel_threshold:
        return 2  # Fire main engine

    # Correct horizontal position to bring it towards the center
    if abs(X_pos) > central_x_threshold:
        if X_pos > 0:
            return 3  # Fire left engine
        else:
            return 1  # Fire right engine

    # Default action is no action to save fuel
    return 0
