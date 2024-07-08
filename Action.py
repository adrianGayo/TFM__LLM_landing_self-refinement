def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    if y_pos > 0.9:  # Still high, focus on reducing x_vel and y_vel moderately
        if abs(x_vel) > 0.1:
            if x_vel > 0:
                return 1  # Left engine to reduce rightward drift
            else:
                return 3  # Right engine to reduce leftward drift
        elif abs(y_vel) > 0.5:
            return 2  # Use center engine to slow down descent
        else:
            return 0  # Conserve fuel
    else:  # Getting closer to the ground, fine-tuning the descent
        if abs(x_vel) > 0.05:
            if x_vel > 0:
                return 1  # Left engine to reduce rightward drift
            else:
                return 3  # Right engine to reduce leftward drift
        elif abs(y_vel) > 0.3:
            return 2  # Use center engine to slow down descent
        elif abs(angle) > 0.1:  # Correct the tilt
            if angle > 0:
                return 3  # Right engine to correct tilt
            else:
                return 1  # Left engine to correct tilt
        else:
            return 0  # Conserve fuel and prepare for landing
