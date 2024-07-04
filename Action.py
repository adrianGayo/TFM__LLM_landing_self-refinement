class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines

        if y_vel < -0.3:  # Descending too fast
            if angle > 0.1 or ang_vel > 0.1:  # Tilting to the right, or rotating right
                action = 1  # Apply left engine to stabilize
            elif angle < -0.1 or ang_vel < -0.1:  # Tilting to the left, or rotating left
                action = 3  # Apply right engine to stabilize
            else:
                action = 2  # Apply center engine to slow down descent
        elif y_vel > -0.1:  # Ascending or stable, switch off engines
            action = 0

        if left_contact and right_contact:  # If both contacts are made, switch off engines
            action = 0

        return action

act_controller = Action()