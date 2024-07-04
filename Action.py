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
        if abs(x_vel) > 0.05:
            if x_vel < 0:
                return 3  # Push right engine to reduce left velocity
            else:
                return 1  # Push left engine to reduce right velocity

        # 3. Smooth Vertical Descent
        if y_pos > 1.0:
            if y_vel < -0.3:
                return 2  # Push both engines to slow down
            else:
                return 0  # Let it fall with gravity.
        elif y_pos > 0.5:
            if y_vel < -0.2:
                return 2  # Push both engines to control descent
            else:
                return 0  # Let it fall with gravity.
        else:
            if y_vel < -0.1:
                return 2  # Push both engines to gentle the landing
            else:
                return 0  # Let it fall with gravity.

        # 4. Final gentle landing when contacts are made
        if (left_contact or right_contact) and abs(y_vel) < 0.2:
            return 0  # Switch off engines
        else:
            return 2  # Gently push engines for controlled descent
