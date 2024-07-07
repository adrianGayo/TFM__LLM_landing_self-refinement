class Agent:
    def __init__(self):
        pass

    def act(self, observation):
        x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
        
        # Prioritize actions for control
        action = 0 # Default to switching off engines

        # 1. Stabilize the angle to be upright
        if angle < -0.1:
            return 3 # Push right engine to reduce left tilt
        elif angle > 0.1:
            return 1 # Push left engine to reduce right tilt

        # 2. Control descent: use upward thrusters if we are descending too quickly
        if y_velocity < -0.5:
            return 2 # Push both engines to slow the descent

        # 3. Control horizontal position: while horizontal movement is manageable
        if x_position < -0.2:
            return 3 # Push right engine to move right
        elif x_position > 0.2:
            return 1 # Push left engine to move left

        return action