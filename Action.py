import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # 1. Stabilize orientation
        if angle < -0.1:
            return 3  # Push right engine to rotate counter-clockwise
        elif angle > 0.1:
            return 1  # Push left engine to rotate clockwise

        # 2. Control horizontal velocity
        if x_vel < -0.1:
            return 3  # Push right engine to reduce leftward velocity
        elif x_vel > 0.1:
            return 1  # Push left engine to reduce rightward velocity

        # 3. Manage vertical velocity
        if y_vel < -0.5:
            return 2  # Push both engines to slow descent
        elif y_vel > 0.2:
            return 0  # Switch off engines if moving upwards
        elif y_pos < 1.0 and y_vel < -0.2:
            return 2  # Push both engines to control descent as it approaches ground

        # Switch off engines for landing when contacts are detected
        if y_pos < 0.1 and abs(y_vel) < 0.1 and (left_contact or right_contact):
            return 0  # Switch off engines for touch down

        return 0  # Default action is to let it fall with gravity when stable
