import random

class LunarLanderController:
    def __init__(self):
        self.steps_without_scoring_well = 0

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
        '''
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # If the lunar lander has landed correctly, do nothing (action 0)
        if left_contact == 1 and right_contact == 1:
            return 0

        # If the angle is too large, attempt to correct it
        if angle < -0.1:
            return 1  # fire right engine
        elif angle > 0.1:
            return 3  # fire left engine

        # If the lander is moving too fast horizontally, attempt to correct it
        if x_vel < -0.1:
            return 1  # fire right engine
        elif x_vel > 0.1:
            return 3  # fire left engine

        # If the lander is falling too fast, fire the main engine
        if y_vel < -0.3:
            return 2

        # If the lander is not descending, start descending
        if y_vel >= 0:
            return 2  # fire main engine

        # Increment the steps without well score
        self.steps_without_scoring_well += 1

        # Edge case: if point threshold without well score perform random step
        if self.steps_without_scoring_well >= 7:
            self.steps_without_scoring_well = 0
            return random.randint(0, 3)

        # Default action
        return 0

# Initialize the controller instance
lander_controller = LunarLanderController()

# Wrapper function to use the controller in the environment
get_action = lander_controller.act