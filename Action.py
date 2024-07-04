class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines
        
        # Threshold values for decision making
        MAX_VERTICAL_SPEED = -0.5
        MAX_HORIZONTAL_SPEED = 0.3
        MAX_TILT = 0.1

        # Adjust vertical descent speed
        if y_vel < MAX_VERTICAL_SPEED:  # If descending too fast, push both engines
            action = 2
        
        # Adjust horizontal speed
        if x_vel > MAX_HORIZONTAL_SPEED:
            action = 1
        elif x_vel < -MAX_HORIZONTAL_SPEED:
            action = 3
        
        # Correct tilt to be as upright as possible
        if angle > MAX_TILT or ang_vel > 0.1:
            action = 1
        elif angle < -MAX_TILT or ang_vel < -0.1:
            action = 3

        # If both contacts are made, switch off engines
        if left_contact and right_contact:
            action = 0

        return action

act_controller = Action()