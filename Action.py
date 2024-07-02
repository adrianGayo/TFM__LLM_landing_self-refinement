def act(curr_status):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = curr_status
    if left_contact == 0 and right_contact == 0:
        if x_pos < -0.1:
            return 3  # Push right engine
        elif x_pos > 0.1:
            return 1  # Push left engine
        else:
            return 2  # Push both engines (upwards)
    else:
        return 0  # Switch off engines