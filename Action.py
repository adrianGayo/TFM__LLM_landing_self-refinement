def act(logs):
    final_decision = []
    for log in logs:
        current_status = log['current status'] 
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status
        action = 0  # Default action is to switch off engines

        # Prioritize stabilization if on-ground (prevents over-adjustment)
        if left_contact == 1 and right_contact == 1:
            action = 0  # Engines off as the spacecraft is landed
        else:
            # Control descent speed (ensure it is gentle)
            if y_vel < -0.5:
                action = 2  # Engage both engines to slow descent

            # Adjust horizontal movement to align with landing zone
            if x_pos < -0.1 and x_vel < 0.1:  # Moving too far left
                action = 3  # Push right engine to counter left drift
            elif x_pos > 0.1 and x_vel > -0.1:  # Moving too far right
                action = 1  # Push left engine to counter right drift

            # Maintain an optimal angle
            if angle < -0.1 and ang_vel < 0.1:
                action = 3  # Push right engine to correct left tilt
            elif angle > 0.1 and ang_vel > -0.1:
                action = 1  # Push left engine to correct right tilt

        final_decision.append(action)
    return final_decision