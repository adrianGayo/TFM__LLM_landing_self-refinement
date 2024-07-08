def act(log_entry):
    try:
        current_status = log_entry['current status']
        x_pos = current_status[0]
        y_pos = current_status[1]
        x_vel = current_status[2]
        y_vel = current_status[3]
        angle = current_status[4]
        ang_vel = current_status[5]
        left_contact = current_status[6]
        right_contact = current_status[7]

        action = 0  # Default action: switch off engines

        # If landed, switch off all engines
        if left_contact == 1 and right_contact == 1:
            action = 0
        else:
            # Control descent speed
            if y_vel < -0.5:
                action = 2  # Engage both engines to slow descent
            # If stable descent speed, adjust horizontal position
            elif x_pos < -0.1 or x_pos > 0.1:
                if x_vel > 0.1:
                    action = 1  # Push left engine to counter right drift
                elif x_vel < -0.1:
                    action = 3  # Push right engine to counter left drift
            # If vertical and horizontal movements are stable, adjust angle
            elif angle < -0.1 or angle > 0.1:
                if angle > 0.1:
                    action = 1  # Push left engine to correct right tilt
                elif angle < -0.1:
                    action = 3  # Push right engine to correct left tilt
        return action
    except Exception as e:
        print(f"Error processing log entry: {e}")
        return 0  # Default action in case of error