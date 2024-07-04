import numpy as np

class Action:
    def __init__(self):
        pass

    def act(self, observation):
        x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

        # Default action is to switch off engines
        action = 0

        # Priority 1: Correct angle and angular velocity for stabilization
        if ang_vel > 0.1 or angle > 0.1:    # Right tilt or rotation correction
            return 1  # Push left engine to counter
        elif ang_vel < -0.1 or angle < -0.1: # Left tilt or rotation correction
            return 3  # Push right engine to counter

        # Priority 2a: Adjust vertical velocity if descending too fast using central engine
        if y_vel < -0.5:  # Unsafe descent speed
            return 2

        # Priority 2b: Switch off central engine if ascending or descent well managed
        if y_vel > -0.3:  # Slight ascent or near-zero descent
            action = 0  # Minimize resource use

        # Priority 3: Correct horizontal velocity to prevent drifting away
        if x_vel > 0.2:  # Excessive rightward drift brings left engine to balance
            return 1
        elif x_vel < -0.2:   # Excessive leftward drift right engine to balance
            return 3

        # Safety Check: Edge-case scenario for final adjustments close to ground
        if y_pos < 0.1 and y_vel < -0.1:   # Near-ground fast descent
            return 2

        # Landing Confirmation: No stabilization necessary if both contacts detect ground
        if left_contact and right_contact:    # Upon landing, no engine usage
            return 0

        return action

act_controller = Action()