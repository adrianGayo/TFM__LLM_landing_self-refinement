import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines

        # Correct angle if spacecraft is tilting 
        if ang_vel > 0.1 or angle > 0.1:  # Tilting or rotating right
            action = 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting or rotating left
            action = 3

        # Control vertical descent speed
        if y_vel < -0.1 and not left_contact and not right_contact:  # Slower descent
            action = 2

        # Adjust horizontal velocity if moving too fast
        if x_vel > 0.3:  # Moving right quickly
            action = 1
        elif x_vel < -0.3:  # Moving left quickly
            action = 3

        # Ensure stabilization near ground
        if y_pos < 0.1 and abs(y_vel) < 0.3:  # Close to ground
            action = 0
        else:  # Correct positioning when safe 
            action = 2 if abs(x_vel) < 0.3 and abs(angle) < 0.1 else action

        # Switch off engines when both contacts are activated
        if left_contact and right_contact:  # Successful landing
            action = 0

        return action

act_controller = Action()