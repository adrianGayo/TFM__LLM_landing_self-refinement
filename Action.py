import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines
        if y_vel < -0.3:  # If descending too fast, push both engines
            action = 2
        elif y_vel > -0.1:  # If ascending or stable, don't push both engines
            action = 0
        if ang_vel > 0.1 or angle > 0.1:  # If rotating right or angled right, push left engine
            action = 1
        elif ang_vel < -0.1 or angle < -0.1:  # If rotating left or angled left, push right engine
            action = 3
        if left_contact and right_contact:  # If both contacts are made, switch off engines
            action = 0
        return action

act_controller = Action()