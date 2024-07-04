import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        action = 0  # Default action: Switch off engines

        # Stabilize angle and angular velocity first
        if ang_vel > 0.1 or angle > 0.1:  # Tilting or rotating right
            return 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting or rotating left
            return 3

        # Adjust vertical velocity if descending too fast
        if y_vel < -0.3:  # Descending too fast
            return 2

        # Minor adjustments to control the x velocity and stabilization
        if x_vel > 0.2:  # Moving right too fast
            return 1
        elif x_vel < -0.2:  # Moving left too fast
            return 3

        # If close to landing, make low-intensity final adjustments
        if y_pos < 0.1 and y_vel < -0.1:  # Close to ground and decreasing fast
            return 2

        # If both contact sensors are activated, safe on ground
        if left_contact and right_contact:
            return 0

        return 0

act_controller = Action()