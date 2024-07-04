import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # 1. Stabilize orientation first
        if angle < -0.1:
            return 3  # Push right engine to rotate counter-clockwise
        elif angle > 0.1:
            return 1  # Push left engine to rotate clockwise

        # 2. Control horizontal velocity
        if x_vel < -0.1:
            return 3  # Push right engine to reduce leftward velocity
        elif x_vel > 0.1:
            return 1  # Push left engine to reduce rightward velocity

        # 3. Vertical movement control
        if y_vel < -0.5:
            return 2  # Push both engines to slow down descent
        elif y_vel > 0.5:
            return 0  # Switch off engines if moving upwards significantly

        # 4. Gentle landing preparation as the distance to the ground decreases
        if y_pos < 0.1 and abs(y_vel) < 0.3 and (left_contact or right_contact):
            return 0  # Switch off engines for smooth touchdown
        elif y_pos < 0.5:
            return 2  # Push both engines to slow down descent

        return 0  # Default action is to let it fall with gravity when stable
