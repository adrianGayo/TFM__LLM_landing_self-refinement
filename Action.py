class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
        action = 0  # Default action: Switch off engines

        # Angle and angular velocity adjustments
        if ang_vel > 0.1 or angle > 0.1:  # Tilting right
            action = 1
        elif ang_vel < -0.1 or angle < -0.1:  # Tilting left
            action = 3

        # Vertically mitigate only fast descents while abstaining from continuous thrust
        elif y_vel < -0.5:  # Fast Descend
            action = 2
        elif y_vel > -0.1:  # Check to stabilize ascent rate.
            action = 0

        # Horizontal position adjustments for drift exceedence
        elif x_vel > 0.3:  # Moving right too fast
            action = 1
        elif x_vel < -0.3:  # Moving left too fast
            action = 3

        # Manage low altitudes nearing landing zones
        elif y_pos < 0.1 and y_vel < -0.1:  # Near ground approached controlled
            action = 2

        # Check combined footer contact and completely stabilize
        if left_contact and right_contact:  # Successful landing detection
            action = 0

        return action

act_controller = Action()