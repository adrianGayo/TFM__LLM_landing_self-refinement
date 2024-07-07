class Agent:
    def __init__(self):
        pass

    def act(self, observation):
        x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
        
        # Initialize default action to switch off engines
        action = 0

        # 1. Stabilize angle aggressively
        if angle < -0.1:
            action = 3  # Push right engine to counter left tilt
        elif angle > 0.1:
            action = 1  # Push left engine to counter right tilt

        # 2. Control descent speed
        if y_velocity < -0.5:
            action = 2  # Push both engines to slow descent

        # 3. Adjust horizontal position while ensuring angle stability
        if abs(angle) < 0.1:  # Prioritize horizontal adjustments if angle is stable
            if x_position < -0.2:
                action = 3  # Push right engine to move right
            elif x_position > 0.2:
                action = 1  # Push left engine to move left

        return action