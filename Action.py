import numpy as np

class LunarLander:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, angular_velocity, left_contact, right_contact = observation
        score_threshold = 200

        # Apply upward thrust if descending too quickly
        if y_vel < -0.1:
            return 2  # Push both engines upwards
        # Apply lateral thrust to correct horizontal velocity if too large
        elif x_vel > 0.1:
            return 1  # Push left engine to move left
        elif x_vel < -0.1:
            return 3  # Push right engine to move right
        # Correct the angle if it's too tilted
        elif angle > 0.1:
            return 1  # Push left engine to rotate counter-clockwise
        elif angle < -0.1:
            return 3  # Push right engine to rotate clockwise
        # Use controlled upward thrust as a stabilizing measure if horizontal movement and angle are within acceptable limits
        elif abs(x_vel) < 0.1 and abs(angle) < 0.1:
            return 2  # Push both engines upwards
        # Otherwise, turn off the engines to save score
        else:
            return 0  # Switch off engines

lander = LunarLander()

# Example of usage
# observation = np.array([0.006, 1.393, 0.31, -0.402, -0.005, -0.029, 0.0, 0.0])
# action = lander.act(observation)
# print(action)