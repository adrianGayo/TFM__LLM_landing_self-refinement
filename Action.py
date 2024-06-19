def act(data):
    
    # Parameters
    min_speed_x = -0.1
    max_speed_x = 0.1
    target_pos_x = 0.0
    safe_range_x = 0.01
    min_speed_y = -0.05
    max_speed_y = 0.05
    target_pos_y = 1.0
    safe_range_y = 0.1
    crash_threshold = -1.0
    success_threshold = 100.0
    center_engine_penalty = 0.3
    side_engine_penalty = 0.03
    tilt_penalty = 0.03
    
    # Extracting data
    current_status = data['current_status']
    time = data['time']
    
    # Calculating values
    pos_x = current_status[0]
    pos_y = current_status[1]
    speed_x = current_status[4]
    speed_y = current_status[5]
    tilt = current_status[3]
    action = 0
    
    # If the position is safe
    if (pos_x >= target_pos_x - safe_range_x and pos_x <= target_pos_x + safe_range_x) and \
        (pos_y >= target_pos_y - safe_range_y and pos_y <= target_pos_y + safe_range_y):
        if speed_x >= min_speed_x and speed_x <= max_speed_x and speed_y >= min_speed_y and speed_y <= max_speed_y:
            if tilt <= tilt_penalty:  # Tilt penalty
                action = 0
            else:
                action = 2  # Main engine
        else:
            action = 3  # Down engine
    else:
        if crash_threshold <= current_status[7] <= success_threshold:  # Checking if the landing is successful or a crash
            if pos_x < target_pos_x:
                action = 1  # Right engine
            else:
                action = 4  # Left engine
        else:
            action = 3  # Down engine
    
    return action