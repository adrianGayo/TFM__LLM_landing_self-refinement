def act(observation):
    # Observation Format: [x, y, v_x, v_y, angle, v_angle, leg1_contact, leg2_contact]
    # Decision Codes: 0: Do nothing, 1: Fire left engine, 2: Fire main engine, 3: Fire right engine
    
    # Define actions
    main_engine = 2
    left_engine = 1
    right_engine = 3
    
    # Extract relevant data from observation
    x, y, v_x, v_y, angle, v_angle, leg1_contact, leg2_contact = observation
    
    # Criteria for actions
    if angle > 0.1 or angle < -0.1:
        # If the angle is too much, fire the side engines to stabilize
        return left_engine if angle < 0 else right_engine
    elif y > 1.4:
        # If the spacecraft is still high, fire the main engine to go down
        return main_engine
    elif v_y < -0.1:
        # If the spacecraft is descending too fast, fire the main engine to slow down the descent
        return main_engine
    elif abs(v_x) > 0.05:
        # If the horizontal speed is too high, fire the side engines to adjust the horizontal position
        return left_engine if v_x < 0 else right_engine
    else:
        # Otherwise, stay stable
        return 0