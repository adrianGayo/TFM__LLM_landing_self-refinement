class Agent:
    def __init__(self):
        pass

    def act(self, observation):
        x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
        
        # Default action to switch off engines
        action = 0

        # 1. Immediate correction for angle stability
        if angle < -0.05:
            return 3  # Push right engine to counter left tilt
        elif angle > 0.05:
            return 1  # Push left engine to counter right tilt

        # 2. Aggressive control for descent speed
        if y_velocity < -0.3:
            return 2  # Push both engines to slow descent

        # 3. Proactive horizontal adjustments when angle is stable
        if abs(angle) < 0.05:  # Ensure angle stability before horizontal corrections
            if x_position < -0.1:
                return 3  # Push right engine to move right
            elif x_position > 0.1:
                return 1  # Push left engine to move left

        return action