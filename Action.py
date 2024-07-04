class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Default to do nothing
        action = 0

        # Priority 1: Stabilize angle and angular velocity
        if ang_vel > 0.1 or angle > 0.1:  # Tilting or rotating right
            return 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting or rotating left
            return 3

        # Priority 2: Adjust vertical descent speed if too fast
        if y_vel < -0.3:  # Descending too fast
            action = 2

        # Priority 3: Adjust horizontal velocity to align the x position
        if x_vel > 0.2:  # Moving right too fast
            action = 1
        elif x_vel < -0.2:  # Moving left too fast
            action = 3

        # Priority 4: Near-ground final adjustments if necessary
        if y_pos < 0.1 and y_vel < -0.1:  # Close to ground and descending fast
            action = 2
        
        # Check for stable landing condition
        if left_contact and right_contact:
            return 0

        return action

act_controller = Action()