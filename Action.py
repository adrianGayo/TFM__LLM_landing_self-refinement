class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Start with default action to do nothing
        action = 0

        # Check and adjust angular velocity and angle: crucial for stable flight
        if abs(angle) > 0.1 or abs(ang_vel) > 0.1:
            action = 1 if angle > 0.1 or ang_vel > 0.1 else 3

        # Check and adjust vertical velocity if falling fast
        if y_vel < -0.4:
            action = 2

        # Check and adjust horizontal velocity if out of bounds
        if x_vel > 0.2:
            action = 1
        elif x_vel < -0.2:
            action = 3

        # In close proximity to ground, refine control
        if y_pos < 0.1 and y_vel < -0.1:
            action = 2

        # Once stable and contacts made, switch off engines\nimplies ensuring the left and right sensors indicate stable contact
        if left_contact and right_contact:
            action = 0

        return action

act_controller = Action()