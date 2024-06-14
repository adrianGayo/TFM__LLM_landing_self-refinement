import numpy as np


class LunarLanderAgent:
    def __init__(self):
        # Define thresholds for decision making
        self.angle_threshold = 0.1  # radians
        self.velocity_threshold = 0.1  # velocity units
        self.position_threshold = 0.1  # position units
        self.previous_velocity = None

    def act(self, observation):
        '''
        The function that codifies the action to be taken in each instant of time.

        Args:
            observation (numpy.array):
                "description": "The state of the environment after the action is taken.",
                "positions": {  
                    "0": "X position",
                    "1": "Y position",
                    "2": "X velocity",
                    "3": "Y velocity",
                    "4": "Angle",
                    "5": "Angular velocity",
                    "6": "Left contact sensor",
                    "7": "Right contact sensor"
                },
                "min_values": [-1.5, -1.5, -5.0, -5.0, -3.14, -5.0, 0, 0],
                "max_values": [1.5, 1.5, 5.0, 5.0, 3.14, 5.0, 1, 1]

        Returns:
            Integer  : The action to be taken.
            "options": {
                    '0' : "Switch off engines",
                    '1' : "Push left engine",
                    '2' : "Push both engines (upwards)",
                    '3' : "Push right engine"
                }
        '''
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Stabilize the angle
        if abs(angle) > self.angle_threshold:
            if angle > 0:
                return 1  # Push left engine
            else:
                return 3  # Push right engine

        # Reduce horizontal velocity
        if abs(x_vel) > self.velocity_threshold:
            if x_vel > 0:
                return 1  # Push left engine to move left
            else:
                return 3  # Push right engine to move right

        # Control vertical velocity and position
        if y_vel < -self.velocity_threshold or y_pos < self.position_threshold:
            return 2  # Push both engines upwards

        # If in contact with ground, do nothing (simulation completed)
        if left_contact == 1 or right_contact == 1:
            return 0  # Switch off engines

        return 0  # Default action to switch off engines


# Instantiate the agent
agent = LunarLanderAgent()


def act(observation):
    return agent.act(observation)
