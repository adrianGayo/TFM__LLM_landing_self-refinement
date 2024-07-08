def act(logs):
    final_decision = []
    for log in logs:
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = log['current status']
        action = 0  # Default to switching off engines

        if left_contact == 1 and right_contact == 1:
            # Safe landing condition met
            action = 0
        else:
            # Control descent speed
            if y_vel < -0.5:
                action = 2  # Push both engines to slow down descent

            # Correct horizontal alignment
            if x_pos < -0.1:
                action = 3  # Push right engine to move left
            elif x_pos > 0.1:
                action = 1  # Push left engine to move right

            # Correct tilt
            if angle < -0.1:
                action = 3  # Push right engine
            elif angle > 0.1:
                action = 1  # Push left engine

        final_decision.append(action)
    return final_decision