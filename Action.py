class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Start with default action to do nothing
        action = 0  # Default action: Switch off engines

        # Priority 1: stabilize angle and angular velocity
        if angle > 0.1 or ang_vel > 0.1:  # Tilting/rotating right
            return 1
        elif angle < -0.1 or ang_vel < -0.1:  # Tilting/rotating left
            return 3

        # Priority 2: Control vertical descent
        if y_vel < -0.4:  # Descending too fast
            return 2
        elif y_vel > -0.1:  # Stabilized or ascending
            return 0

        # Priority 3: Horizontal control
        if x_vel > 0.2:  # Moving right too fast
            return 1
        elif x_vel < -0.2:  # Moving left too fast
            return 3

        # Close proximity adjustments for soft landing
        if y_pos < 0.1 and y_vel < -0.1:  # Near ground and descending
            return 2

        # Check for stable landing
        if left_contact and right_contact:  # Both contacts indicate stability
            return 0

        return action

act_controller = Action()