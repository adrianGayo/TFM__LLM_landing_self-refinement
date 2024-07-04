import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # Stabilize angular position first if it's too large
        if abs(angle) > 0.1:
            if angle < 0:
                return 3  # Push right engine to rotate counter-clockwise
            else:
                return 1  # Push left engine to rotate clockwise

        # Reduce horizontal speed if too high
        if abs(x_vel) > 0.1:
            if x_vel < 0:
                return 3  # Push right engine to move right
            else:
                return 1  # Push left engine to move left

        # Reduce vertical speed when close to the ground
        if y_pos < 0.5 and y_vel < -0.1:
            return 2  # Push both engines to slow descent

        # When near zero altitude and speed, and sensors indicate contact
        if y_pos < 0.1 and y_vel > -0.1:
            if left_contact and right_contact:
                return 0  # Switch off engines

        # Otherwise, push both engines to stabilize descent
        return 2
