def act(observation):
    x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    # Early Phase: Large height, prioritize horizontal and vertical stabilization
    if y_position > 1.0:
        if abs(x_velocity) > 0.2: 
            if x_velocity > 0:
                return 1 
            else:
                return 3 
        elif y_velocity < -0.5: 
            return 2 
        elif abs(angle) > 0.1: 
            if angle > 0:
                return 3 
            else:
                return 1 
        else:
            return 0 

    # Mid Phase: Balancing closer to ground, horizontal and vertical refinements
    elif y_position > 0.3:
        if abs(x_velocity) > 0.1:
            if x_velocity > 0:
                return 1 
            else:
                return 3 
        elif y_velocity < -0.3:
            return 2 
        elif abs(angle) > 0.05: 
            if angle > 0:
                return 3 
            else:
                return 1 
        else:
            return 0 

    # Final Phase: Precise adjustments for landing
    else:
        if abs(x_position) > 0.05:
            if x_position < 0:
                return 3 
            else:
                return 1 
        elif abs(y_velocity) > 0.1:
            return 2 
        elif abs(angle) > 0.02:
            if angle < 0:
                return 1 
            else:
                return 3 
        else:
            return 0 
