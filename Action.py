import numpy as np

class SpacecraftLandingAgent:
    def __init__(self):
        pass

    def act(self, state):
        x_pos, y_pos, x_vel, y_vel, angle, angular_vel, left_contact, right_contact = state

        # 1. Stabilize angular position first if it's too large
        if abs(angle) > 0.1:
            if angle < 0:
                return 3  # Push right engine to rotate counter-clockwise
            else:
                return 1  # Push left engine to rotate clockwise

        # 2. Reduce horizontal speed if it's too high
        if abs(x_vel) > 0.1:
            if x_vel < 0:
                return 3  # Push right engine to move right
            else:
                return 1  # Push left engine to move left

        # 3. Approach landing zone in gentle vertical descent
        # If very close to ground and not descending too fast, try to land
        if y_pos < 0.1 and abs(y_vel) < 0.1 and (left_contact or right_contact):
            return 0  # Switch off engines
        # If close to ground and descending faster
        elif y_pos < 0.5 and y_vel < -0.3:
            return 2  # Push both engines to slow descent
        # If further up and descending
        elif y_vel < -0.5:
            return 2  # Push both engines to slow descent
        else:
            return 0  # Default action
