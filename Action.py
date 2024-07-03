import numpy as np

# Constants
LEFT_ENGINE_COST = 0.03
CENTER_ENGINE_COST = 0.3
RIGHT_ENGINE_COST = 0.03

# Indices for observation for clarity
X_POS = 0
Y_POS = 1
X_VEL = 2
Y_VEL = 3
ANGLE = 4
ANG_VEL = 5
LEFT_CONTACT = 6
RIGHT_CONTACT = 7


def act(observation):
    '''
    The function that codifies the action to be taken in each instant of time.

    Args:
        observation (numpy.array):
            Description: The state of the environment after the action is taken.
            Positions: {  
                0: X position,
                1: Y position,
                2: X velocity,
                3: Y velocity,
                4: Angle,
                5: Angular velocity,
                6: Left contact sensor,
                7: Right contact sensor
            }
            Min_values: [-1.5, -1.5, -5.0, -5.0, -3.14, -5.0, 0, 0],
            Max_values: [1.5, 1.5, 5.0, 5.0, 3.14, 5.0, 1, 1]

    Returns:
        Integer: The action to be taken.
    '''

    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Successful landing conditions
    target_region = (-0.5 <= x_pos <= 0.5) and (-0.5 <= y_pos <= 0.5)
    acceptable_velocities = (-0.5 <= x_vel <= 0.5) and (-1.0 <= y_vel <= -0.1)
    stable_orientation = (-0.1 <= angle <= 0.1) and (-0.1 <= ang_vel <= 0.1)
    landed = left_contact == 1 and right_contact == 1

    if landed:
        return 0  # Switch off engines

    if not target_region:
        if x_pos < -0.5 or x_vel < -0.5:
            return 1  # Push left engine
        elif x_pos > 0.5 or x_vel > 0.5:
            return 3  # Push right engine

    if not acceptable_velocities:
        if x_vel < -0.5:
            return 1  # Push left engine
        elif x_vel > 0.5:
            return 3  # Push right engine
        if y_vel < -1.0:
            return 2  # Push both engines

    if not stable_orientation:
        if angle < -0.1 or ang_vel < -0.1:
            return 1  # Push left engine
        elif angle > 0.1 or ang_vel > 0.1:
            return 3  # Push right engine

    return 2  # Push both engines
