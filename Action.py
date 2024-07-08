class Agent:
    def __init__(self):
        pass

    def act(self, current_status):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status

        if left_contact or right_contact:
            return 0  # Switch off engines as we have landed or crashed.

        # Stabilize angle and minimize angular velocity
        if abs(angle) > 0.1:
            if angle < -0.1:
                return 3  # Push right engine to adjust angle to the right.
            elif angle > 0.1:
                return 1  # Push left engine to adjust angle to the left.
        elif abs(ang_vel) > 0.1:
            if ang_vel < 0:  # If rotating left, push right to stabilize.
                return 3
            else:  # If rotating right, push left to stabilize.
                return 1
        
        # Control horizontal position and velocity
        if abs(x_pos) > 0.1:  # If too far horizontally, push opposite engine.
            if x_pos < -0.1:  # Too far left, push right.
                return 3
            elif x_pos > 0.1:  # Too far right, push left.
                return 1
        elif abs(x_vel) > 0.1:
            if x_vel < 0:  # Moving left, push right engine.
                return 3
            else:  # Moving right, push left engine.
                return 1
        
        # Control vertical velocity for a smooth landing
        if y_vel < -0.5:  # Falling too fast, push upwards to slow down.
            return 2
        
        # Default action to stabilize descent
        return 0