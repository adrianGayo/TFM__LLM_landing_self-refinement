class Agent:
    def __init__(self):
        pass

    def act(self, current_status):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status

        if left_contact or right_contact:
            return 0  # Switch off engines as we have landed or crashed.

        # Stabilize angle and minimize angular velocity
        if angle < -0.1:
            return 3  # Push right engine to adjust angle to the right.
        elif angle > 0.1:
            return 1  # Push left engine to adjust angle to the left.
        elif ang_vel < -0.1 or ang_vel > 0.1:
            if ang_vel < 0:  # If rotating left, push right to stabilize.
                return 3
            else:  # If rotating right, push left to stabilize.
                return 1
        
        # Control horizontal position and velocity
        if x_pos < -0.1:  # If too far left, push right.
            return 3
        elif x_pos > 0.1:  # If too far right, push left.
            return 1
        elif x_vel < -0.1 or x_vel > 0.1:  # If moving horizontally, stabilize horizontal velocity.
            if x_vel < 0:
                return 3
            else:
                return 1
        
        # Control vertical velocity for a smooth landing
        if y_vel < -0.5:  # If falling too fast, push upwards to slow down.
            return 2
        
        # Default action to stabilize and allow smooth descent
        return 0