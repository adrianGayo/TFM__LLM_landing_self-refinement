import numpy as np

def act(observation):
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
    x, y, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Define thresholds for velocities and angles
    x_pos_threshold = 0.1
    y_pos_threshold = 0.1
    x_vel_threshold = 0.1
    y_vel_threshold = 0.15
    angle_threshold = 0.1
    ang_vel_threshold = 0.1

    # Ensure that everything is within the thresholds before cutting the engines
    if left_contact == 1 or right_contact == 1:
        if abs(x) < x_pos_threshold and abs(y) < y_pos_threshold and abs(x_vel) < x_vel_threshold and abs(y_vel) < y_vel_threshold and abs(angle) < angle_threshold and abs(ang_vel) < ang_vel_threshold:
            return 0  # Cut all engines to settle

    # Order of priority
    # 1. Reduce y velocity if it's too high (falling too fast)
    if y_vel < -y_vel_threshold:
        return 2  # Main engine on

    # 2. Stabilize angular velocity if needed
    if abs(ang_vel) > ang_vel_threshold:
        return 3 if ang_vel > 0 else 1  # Turn on the appropriate side engine

    # 3. Stabilize angle if needed
    if abs(angle) > angle_threshold:
        return 3 if angle > 0 else 1  # Turn on the appropriate side engine

    # 4. Reduce x velocity if it's too high
    if abs(x_vel) > x_vel_threshold:
        return 1 if x_vel > 0 else 3  # Turn on the appropriate side engine

    # 5. Keep main engine off for gentle descent if all conditions are stable
    return 0
