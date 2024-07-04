class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        action = 0  # Default action: Switch off engines

        # Stabilize angle and angular velocity first
        if angle > 0.1 or ang_vel > 0.1: # Tilting or rotating right
            return 1
        elif angle < -0.1 or ang_vel < -0.1: # Tilting or rotating left
            return 3

        # Adjust vertical velocity if descending too fast
        if y_vel < -0.3: # Descending too fast
            return 2

        # Adjust horizontal velocity for position correction
        if x_vel > 0.2: # Movement right too fast
            return 1
        elif x_vel < -0.2:  # Movement left too fast
            return 3

        # Adjust while close: final precision adjustments for soft landing
        if y_pos < 0.1 and y_vel < -0.1: 
            return 2

        # Once landed and in stable contact, ensure no engine thruster
        if left_contact and right_contact:
            return 0
        
        return action

act_controller = Action()