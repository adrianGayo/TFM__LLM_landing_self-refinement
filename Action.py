def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Define finely tuned thresholds
    x_pos_threshold = 0.05
    x_vel_threshold = 0.2
    y_vel_threshold = 0.3
    angle_threshold = 0.1
    ang_vel_threshold = 0.2  
    left_contact, right_contact = observation[6], observation[7]

    # Check if landed
    if left_contact == 1 and right_contact == 1:
        return 0 # Turn off engines

    # Moderate horizontal movements
    if x_pos > x_pos_threshold and x_vel > -x_vel_threshold:
        return 1 # Thrust left
    elif x_pos < -x_pos_threshold and x_vel < x_vel_threshold:
        return 3 # Thrust right

    # Stabilize vertical descent
    if y_vel < -y_vel_threshold:
        return 2 # Thrust both upwards

    # Keep the spacecraft upright
    if angle > angle_threshold:
        return 1 # Thrust left
    elif angle < -angle_threshold:
        return 3 # Thrust right

    if abs(ang_vel) > ang_vel_threshold:
        return 1 if ang_vel > 0 else 3

    return 0
