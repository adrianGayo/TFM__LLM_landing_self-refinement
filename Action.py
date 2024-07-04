import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Initial action is to do nothing
        action = 0

        # Stabilize angle and angular velocity first
        if ang_vel > 0.1 or angle > 0.1:  # Tilting or rotating right
            action = 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting or rotating left
            action = 3

        # Adjust vertical velocity if descending too fast or too slow
        if y_vel < -0.3:  # Descending too fast
            action = 2

        # Adjust horizontal velocity to correct horizontal position
        if x_vel > 0.2:  # Moving right too fast
            action = 1
        elif x_vel < -0.2:  # Moving left too fast
            action = 3

        # If close to landing, ensure fine adjustments and softly turn off engines
        if y_pos < 0.1 and y_vel < -0.1:  # Close to ground and not fast descent
            action = 2

        # Switch off engines if stable and close to ground
        if left_contact and right_contact:  # Both contacts made, indicating a stable land
            action = 0

        return action

act_controller = Action()