import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # 1. Immediate Angular Correction
        if abs(angle) > 0.1:
            if angle < 0:
                return 3  # Push right engine to rotate counter-clockwise
            else:
                return 1  # Push left engine to rotate clockwise

        # 2. Control Horizontal Movement
        if abs(x_vel) > 0.1:
            if x_vel < 0:
                return 3  # Push right engine to reduce leftward velocity
            else:
                return 1  # Push left engine to reduce rightward velocity

        # 3. Control Vertical Descent and Gentle Landing
        if y_vel < -0.1:
            if y_pos > 1.0:
                return 2  # Push both engines to slow down
            elif y_pos > 0.5:
                return 2  # Push both engines to control descent
            elif (left_contact or right_contact):
                return 0  # Switch off engines when near ground with sensor contacts
            else:
                return 2  # Push both engines to maintain gentle landing
        else:
            return 0  # Default to gravity when descent rate is manageable
