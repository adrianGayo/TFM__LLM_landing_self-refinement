class Agent:
    def __init__(self):
        pass

    def act(self, current_status):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status

        if left_contact or right_contact:
            return 0  # Vessel has landed or crashed, no further action.

        # If angle deviation is high, prioritize stabilizing the angle
        if abs(angle) > 0.2:
            if angle < 0:
                return 3  # Correct angle by pushing right engine
            else:
                return 1  # Correct angle by pushing left engine

        # Check angular velocity for any quick angle corrections needed
        if abs(ang_vel) > 0.2:
            if ang_vel < 0:
                return 3  # Push right engine to counteract negative angular velocity
            else:
                return 1  # Push left engine to counteract positive angular velocity

        # Vertical descent control to ensure smooth landing
        if y_vel < -0.5:  # Too rapid descent
            return 2  # Apply upward thrust

        # Horizontal motion adjustment
        if abs(x_pos) > 0.1:
            if x_pos < -0.1:
                return 3  # Move right to center
            elif x_pos > 0.1:
                return 1  # Move left to center

        if abs(x_vel) > 0.1:  # If lateral velocity is high
            if x_vel < 0:
                return 3  # Move right to reduce leftward drift
            else:
                return 1  # Move left to reduce rightward drift

        # Default: Smooth descent with no extra correction, keep engines off
        return 0