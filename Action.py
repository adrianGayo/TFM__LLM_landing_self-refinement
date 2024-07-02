import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants for decision-making thresholds and corrective steps
    ANGLE_THRESHOLD = 0.1  # radians
    HORIZONTAL_VELOCITY_THRESHOLD = 0.2  # m/s
    VERTICAL_VELOCITY_THRESHOLD = -0.5  # m/s
    POSITION_THRESHOLD = 0.1  # meters
    MAX_ANGLE = 0.3  # radians to prevent over-tilting

    # If the spacecraft is close to landing and aligned, shut off engines
    if abs(x_pos) < POSITION_THRESHOLD and \
       abs(x_vel) < HORIZONTAL_VELOCITY_THRESHOLD and \
       abs(y_vel) < VERTICAL_VELOCITY_THRESHOLD and \
       abs(angle) < ANGLE_THRESHOLD and \
       y_pos < POSITION_THRESHOLD:
        return 0  # Switch off engines

    # Correct angle if tilting excessively
    if angle > ANGLE_THRESHOLD or ang_vel > ANGLE_THRESHOLD:
        return 1  # Push left engine to reduce positive angle and angular velocity
    elif angle < -ANGLE_THRESHOLD or ang_vel < -ANGLE_THRESHOLD:
        return 3  # Push right engine to reduce negative angle and angular velocity

    # Correct horizontal drift and dynamic angular velocity simultaneously
    if abs(angle) < MAX_ANGLE:
        if x_pos > POSITION_THRESHOLD:
            if ang_vel <= 0: return 1  # Push left engine to move right when stable
        elif x_pos < -POSITION_THRESHOLD:
            if ang_vel >= 0: return 3  # Push right engine to move left when stable

    # Reduce horizontal velocity if too high
    if x_vel > HORIZONTAL_VELOCITY_THRESHOLD:
        return 3  # Push right engine to reduce positive x velocity
    elif x_vel < -HORIZONTAL_VELOCITY_THRESHOLD:
        return 1  # Push left engine to reduce negative x velocity

    # Minimizing vertical speed dynamically
    if y_vel < VERTICAL_VELOCITY_THRESHOLD:
        return 2  # Push both engines to reduce descent rate

    # Default action to push both engines to maintain control
    return 2