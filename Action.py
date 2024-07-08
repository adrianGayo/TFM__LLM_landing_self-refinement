import random

def act(observation):
    '''
    The function that codifies the action to be taken in each instant of time.

    Args:
        observation (numpy.array):
            The state of the environment after the action is taken.
            positions: 
                0: X position
                1: Y position
                2: X velocity
                3: Y velocity
                4: Angle
                5: Angular velocity
                6: Left contact sensor
                7: Right contact sensor
            min_values: [-1.5, -1.5, -5.0, -5.0, -3.14, -5.0, 0, 0]
            max_values: [1.5, 1.5, 5.0, 5.0, 3.14, 5.0, 1, 1]

    Returns:
        Integer : The action to be taken.
            options:
                0 : Switch off engines
                1 : Push left engine
                2 : Push both engines (upwards)
                3 : Push right engine
    '''
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Thrust upwards if falling too fast
    if y_vel < -0.3:
        return 2

    # Adjust horizontal position using left and right engines
    if x_pos > 0.1:
        return 1
    elif x_pos < -0.1:
        return 3

    # Control angle if tilted too much
    if angle > 0.1:
        return 1
    elif angle < -0.1:
        return 3

    # Switch off engines to conserve fuel in stable conditions
    return 0