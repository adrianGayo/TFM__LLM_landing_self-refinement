class Agent:
    def __init__(self):
        pass

    def act(self, observation):
        x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation
        
        # Thrusters' action
        action = 0 # Default is to switch off engines

        # Minimize tilt
        if angle < -0.1:
            action = 3 # Push right engine to reduce left tilt
        elif angle > 0.1:
            action = 1 # Push left engine to reduce right tilt
        
        # Control descent speed
        if y_velocity < -1.0:
            action = 2 # Push both engines to slow down descent
        
        # Correct horizontal position
        if x_position < -0.1:
            action = 3 # Push right engine to move right
        elif x_position > 0.1:
            action = 1 # Push left engine to move left

        # Ensure we only increase velocity control if necessary
        if y_velocity < -1.0 and abs(y_position) < 0.5:
            action = 2

        return action