import math

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
        "options": {
                '0' : "Switch off engines",
                '1' : "Push left engine",
                '2': "Push both engines (upwards)",
                '3' : "Push right engine"
            }
    '''

    X_pos, Y_pos, X_vel, Y_vel, angle, ang_vel, left_contact, right_contact = observation

    angle_threshold = 0.1  # Angle limit for near upright
    vel_threshold = 0.1  # Close to zero velocity
    pos_threshold = 0.1  # Close to landing area
    descent_speed_limit = -0.5  # Max descent speed

    def safe_firing_combined(angle, ang_vel):
        if angle < 0 or ang_vel < 0:
            return 1  # Firing left engine to balance right?
        return 3  # Firing right engine to balance left?

    # Regulate angle exclusively 
    if abs(angle) > angle_threshold:
        return safe_firing_combined(angle, ang_vel)
        
    # Single approach for vertical stability
    elif Y_vel < descent_speed_limit>:
        return 2

    # Manage primary positional keeps with X-axis corrections
    elif abs(X_pos) > pos_threshold or abs(X_vel) > vel_threshold:
        if X_pos < 0 or X_vel < 0:
            return 3  # Push Move Left Engine back level
        return 1  # Push Right level moves horizontally back.

    # Optimize conserving System
    return 0