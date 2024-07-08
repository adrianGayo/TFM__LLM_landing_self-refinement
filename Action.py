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

        action = 0  # Default to turning off engines

        if left_contact == 1 and right_contact == 1:
            action = 0  # Turn off engines if landed
        else:
            # Adjust vertical speed
            if y_vel < -0.2:
                action = 2  # Push both engines to reduce descent speed
            # Adjust horizontal position
            elif x_pos < -0.1:
                action = 3  # Push right engine to move left
            elif x_pos > 0.1:
                action = 1  # Push left engine to move right
            # Stabilize angle
            elif angle < -0.1:
                action = 3  # Push right engine to correct left tilt
            elif angle > 0.1:
                action = 1  # Push left engine to correct right tilt

        return action
    except Exception as e:
        print(f"Error processing log entry: {e}")
        return 0  # Return default action in case of error