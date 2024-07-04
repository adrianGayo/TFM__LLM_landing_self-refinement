import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # 1. Immediate Angular Correction
        if angle < -0.1:
            return 3  # Push right engine to rotate counter-clockwise
        elif angle > 0.1:
            return 1  # Push left engine to rotate clockwise

        # 2. Control Horizontal Movement
        if x_vel < -0.1:
            return 3  # Push right engine to reduce leftward velocity
        elif x_vel > 0.1:
            return 1  # Push left engine to reduce rightward velocity

        # 3. Control Vertical Descent and Gentle Landing
        if y_pos < 0.3 and y_vel >= -0.1:
            if left_contact or right_contact:
                return 0  # Switch off engines for touchdown
        if y_vel < -0.1 and y_pos > 0.5:
            return 2  # Push both engines to slow down
        return 0  # Default to gravity when descent rate is manageable
