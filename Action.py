import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines
        if y_vel < -0.3 and not left_contact and not right_contact:  # High descending speed, use up thrust
            action = 2
        elif ang_vel > 0.1 or angle > 0.1:  # If rotating right or angled right, push left engine
            action = 1
        elif ang_vel < -0.1 or angle < -0.1:  # If rotating left or angled left, push right engine
            action = 3
        elif abs(x_vel) > 0.1:  # If horizontal velocity is high, apply appropriate lateral thrust 
            action = 1 if x_vel > 0 else 3
        elif left_contact and right_contact:  # If both contacts are made, switch off engines
            action = 0
        elif not (left_contact or right_contact) and abs(y_vel) < 0.1 and abs(x_vel) < 0.1 and abs(angle) < 0.1:  # Safe stable descent
            action = 0
        return action

act_controller = Action()