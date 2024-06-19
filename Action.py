def act(data):
    
    acc_x = data[2]
    acc_y = data[3]
    vel_x = data[4]
    vel_y = data[5]
    landing_status = data[1]
    score = data[6]
    action = 0
    
    # Implement your decision-making process here
    if landing_status == 3:  # If the landing is out of bounds
        action = 0
    elif acc_y < -0.2:  # Increase altitude if falling too fast
        action = 1
    elif acc_y > 0.2:  # Decrease altitude if ascending too fast
        action = 3
    elif vel_x > 0.05:  # Move left
        action = 2
    elif vel_x < -0.05:  # Move right
        action = 4
    else:
        action = 0  # Stay still
    
    return action