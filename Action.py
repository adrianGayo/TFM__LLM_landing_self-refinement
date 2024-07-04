import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Default to do nothing
        action = 0

        # Priority 1: Stabilize angle and angular velocity
        if ang_vel > 0.1 or angle > 0.1:  # Tilting or rotating right
            action = 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting or rotating left
            action = 3

        # Priority 2: If both contact sensors are activated, switch off engines
        if left_contact and right_contact:
            return 0

        # Priority 3: Adjust vertical velocity if descending too fast
        if y_vel < -0.5:  # Descending too fast
            return 2

        # Priority 4: Adjust horizontal velocity to correct horizontal position
        if x_vel > 0.3:  # Moving right too fast
            return 1
        elif x_vel < -0.3:  # Moving left too fast
            return 3

        # Priority 5: Near-ground final adjustments if necessary
        if y_pos < 0.1 and y_vel < -0.1:  # Close to ground and descending fast
            return 2

        return action

act_controller = Action()