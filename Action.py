import numpy as np

# Define constants for easier adjustments
HORIZONTAL_THRESHOLD = 0.1
VELOCITY_THRESHOLD = 0.1
VERTICAL_VELOCITY_THRESHOLD = -0.3
ANGLE_THRESHOLD = 0.1

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
    Function determining the required action for optimal landing.

    Args:
        observation (numpy.array):
            - Description: State of the environment after the action is taken.
            - Positions: {  
                "0": X position,
                "1": Y position,
                "2": X velocity,
                "3": Y velocity,
                "4": Angle,
                "5": Angular velocity,
                "6": Left contact sensor,
                "7": Right contact sensor
            }
            - Min_values: [-1.5, -1.5, -5.0, -5.0, -3.14, -5.0, 0, 0]
            - Max_values: [1.5, 1.5, 5.0, 5.0, 3.14, 5.0, 1, 1]

    Returns:
        Integer: The action to be executed next.
    '''
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Checking for successful landing
    if left_contact == 1 and right_contact == 1:
        return 0  # Switch off engines since safely landed

    # Horizontal Adjustment and Angle Control
    if (x_pos > HORIZONTAL_THRESHOLD or x_vel > VELOCITY_THRESHOLD) and angle < ANGLE_THRESHOLD:
        return 1  # Push left engine when right drift/component exceeds thresholds
    elif (x_pos < -HORIZONTAL_THRESHOLD or x_vel < -VELOCITY_THRESHOLD) and angle > -ANGLE_THRESHOLD:
        return 3  # Push right engine when left drift/component emerges significantly

    # Vertical Control (stabilize velocity)
    if y_vel < VERTICAL_VELOCITY_THRESHOLD or (y_pos > HORIZONTAL_THRESHOLD and y_vel < VELOCITY_THRESHOLD):
        return 2  # Execute enough thrust ensuring reduced downward acceleration

    # Auxiliary Angle Adjustment within Vertical Consideration
    if angle > ANGLE_THRESHOLD or ang_vel > ANGLE_THRESHOLD:
        return 1  # Push left engine for upper angle correction
    elif angle < -ANGLE_THRESHOLD or ang_vel < -ANGLE_THRESHOLD:
        return 3  # Push right engine for lower angle correction

    # Maintain current status as no intervention is conditional
   
    return 0