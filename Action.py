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

    # Define thresholds for decision making
    angle_threshold = 0.1  # Near vertical
    velocity_threshold = 0.1  # Near zero velocity
    position_threshold = 0.1  # Near landing area
    descent_speed_limit = -0.5  # Maximum safe descent speed

    # Combined approach for angle and angular velocity management
    if abs(angle) > angle_threshold or abs(ang_vel) > velocity_threshold:
        if angle < 0 and ang_vel <= 0:
            return 1  # Push left engine to rotate right
        elif angle > 0 and ang_vel >= 0:
            return 3  # Push right engine to rotate left
        elif angle < 0 and ang_vel > 0:
            return 1  # Push left engine to reduce angular velocity
        elif angle > 0 and ang_vel < 0:
            return 3  # Push right engine to reduce angular velocity
        
    # Adjust vertical descent speed only when critically needed
    elif Y_vel < descent_speed_limit:
        return 2  # Push both engines to slow descent 

    # Correct horizontal position primarily when angle is stable
    elif abs(X_pos) > position_threshold or abs(X_vel) > velocity_threshold:
        if X_pos < 0 and X_vel <= 0:
            return 3  # Push right engine to move left
        elif X_pos > 0 and X_vel >= 0:
            return 1  # Push left engine to move right
        elif X_pos < 0 and X_vel > 0:
            return 1  # Counter velocity to balance
        elif X_pos > 0 and X_vel < 0:
            return 3  # Counter velocity to balance
    
    # Maintain current status (engines off) to conserve score
    return 0