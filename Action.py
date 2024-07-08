class Agent:
    def __init__(self):
        pass

    def act(self, current_status):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = current_status

        if left_contact or right_contact:
            return 0  # Vessel is landed or crashed, stop all engines.

        # Prevent excessive vertical speed, give priority to slower vertical descent
        if y_vel < -0.5:  # High descent speed
            return 2  # Push both engines upward to reduce descent speed.

        # Stabilize angle first if deviation is significantly large
        if abs(angle) > 0.2:  # Significant angle deviation
            if angle < 0:
                return 3  # Push right to correct negative angle
            else:
                return 1  # Push left to correct positive angle
        if abs(ang_vel) > 0.2:  # Angular velocity correction needed
            if ang_vel < 0:
                return 3  # Push right to counteract left rotation
            else:
                return 1  # Push left to counteract right rotation

        # Control horizontal position and velocity sparingly
        if abs(x_pos) > 0.2:  # Significant horizontal offset
            if x_pos < -0.2:  # Offset to left, correct rightward
                return 3
            elif x_pos > 0.2:  # Offset to right, correct leftward
                return 1
        if abs(x_vel) > 0.2:  # Significant horizontal velocity
            if x_vel < 0:  # Moving left, push right to stabilize
                return 3
            else:  # Moving right, push left to stabilize
                return 1

        # Soft control by keeping engines off to maintain descension gradually
        return 0