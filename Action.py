class Agent:
    def __init__(self):
        pass

    def act(self, current_status):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status

        if left_contact or right_contact:
            return 0  # Stop engines on landing or crashing.

        # Vertical descent control to ensure smooth landing
        if y_vel < -0.5:  # High descent speed priority
            return 2  # Push both engines upwards to reduce descent speed.

        # Control horizontal position more conservatively
        if abs(x_pos) > 0.2:  # Major horizontal offset correction
            if x_pos < -0.2:
                return 3  # Move right to center
            elif x_pos > 0.2:
                return 1  # Move left to center
        if abs(x_vel) > 0.2:  # Horizontal velocity correction
            if x_vel < 0:
                return 3  # Moving left, stabilize right
            else:
                return 1  # Moving right, stabilize left
        
        # Angle stabilization focusing on small incremental adjustments
        if abs(angle) > 0.1:  # Large angle deviation correction
            if angle < 0:
                return 3  # Push right to reduce negative angle
            else:
                return 1  # Push left to reduce positive angle
        if abs(ang_vel) > 0.1:  # Angular velocity correction
            if ang_vel < 0:
                return 3  # Correct leftward angular velocity
            else:
                return 1  # Correct rightward angular velocity

        # Default action to stabilize descent gradually
        return 0