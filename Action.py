class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines

        # Prioritize stabilization in ang_vel and angle
        if ang_vel > 0.1 or angle > 0.1:  # Tilting or rotating right
            return 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting or rotating left
            return 3

        # Gradual vertical thrust for rate reduction, mindful of y_vel not over-accelerating upwards
        if y_vel < -0.3:  # Fast descent mitigation
            return 2
        elif y_vel > 0.2:  # Avoid upward surge by switching off
            return 0

        # Lateral velocities adjustments 
        if x_vel > 0.3:  # Excessive right shift
            return 1
        elif x_vel < -0.3:  # Excessive left shift
            return 3

        # Fine-tune near-ground stabilities
        if y_pos < 0.1 and abs(y_vel) < 0.3:  # Close with stable descent velocity
            return 0

        # If both contacts are detected, affirm landing completion
        if left_contact and right_contact:
            return 0

        return action

act_controller = Action()