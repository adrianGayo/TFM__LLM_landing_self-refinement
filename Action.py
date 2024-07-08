def act(logs):
    final_decision = []
    for log_entry in logs:
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

            action = 0  # Default action is to switch off engines

            # Prioritize stabilization if on-ground
            if left_contact == 1 and right_contact == 1:
                action = 0  # Engines off as the spacecraft is landed
            else:
                # Control descent speed
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
        except Exception as e:
            print(f"Error processing log entry: {log_entry}", e)
    return final_decision