import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # Stabilize orientation
        if abs(angle) > 0.1:
            return 1 if angle > 0 else 3

        # Control horizontal velocity
        if abs(x_vel) > 0.1:
            return 1 if x_vel > 0 else 3

        # Manage vertical velocity and position
        if y_vel < -0.2:
            return 2  # Slow descent
        elif y_vel > 0.1:
            return 0  # Let if float up a bit
        elif y_pos < 0.3 and y_vel < -0.1 and (left_contact or right_contact):
            return 0  # Prepare for touch down
        elif y_pos < 0.5 and y_vel < -0.1:
            return 2  # Decelerate descent as ground approaches

        return 0  # Default action is to let it fall with gravity when stable
