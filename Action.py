def act(logs):
    final_decision = []
    for log_entry in logs:
        try:
            if isinstance(log_entry, dict) and 'current status' in log_entry:
                current_status = log_entry['current status']
                if isinstance(current_status, list) and len(current_status) == 8:
                    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status

                    action = 0  # Default action: switch off engines

                    # If landed, switch off all engines
                    if left_contact == 1 and right_contact == 1:
                        action = 0
                    else:
                        # Control descent speed
                        if y_vel < -0.5:
                            action = 2  # Engage both engines to slow descent

                        # Adjust horizontal position
                        if x_pos < -0.1 and x_vel < 0.1:
                            action = 3  # Push right engine to move left
                        elif x_pos > 0.1 and x_vel > -0.1:
                            action = 1  # Push left engine to move right

                        # Adjust tilt
                        if angle < -0.1 and ang_vel < 0.1:
                            action = 3  # Push right engine to correct left tilt
                        elif angle > 0.1 and ang_vel > -0.1:
                            action = 1  # Push left engine to correct right tilt

                    final_decision.append(action)
                else:
                    raise ValueError(f'Invalid current_status length or type: {current_status}')
            else:
                raise ValueError(f'Missing current status in log_entry: {log_entry}')
        except Exception as e:
            print(f"Error processing log entry: {e}")
            final_decision.append(0)  # Default action in case of error
    return final_decision