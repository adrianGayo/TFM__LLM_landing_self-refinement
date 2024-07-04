import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Default action is to switch off engines
        action = 0

        # Priority 1: Stabilize angle and angular velocity
        if ang_vel > 0.1 or angle > 0.1:    # Tilting or rotating right
            return 1
        elif ang_vel < -0.1 or angle < -0.1: # Tilting or rotating left
            return 3

        # Priority 2: Adjust vertical velocity (descent rate)
        if y_vel < -0.5:  # Descending too fast, use central engine to slow down
            return 2
        elif y_vel > -0.1:  # Ascending slightly or stable, switch off central engine
            return 0

        # Priority 3: Adjust horizontal velocity
        if x_vel > 0.2:  # Moving right too fast, push left engine
            return 1
        elif x_vel < -0.2:   # Moving left too fast, push right engine
            return 3

        # Additional logic for final adjustments before landing
        if y_pos < 0.1 and y_vel < -0.1:   # Close to ground and fast descent, careful slow down
            return 2

        # Check for stable landing condition
        if left_contact and right_contact:    # Both sides in contact means landed.
            return 0

        return action

act_controller = Action()