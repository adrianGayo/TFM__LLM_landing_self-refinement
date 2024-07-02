import numpy as np

def act(observation):
    x_pos = observation[0]
    y_pos = observation[1]
    x_vel = observation[2]
    y_vel = observation[3]
    angle = observation[4]
    ang_vel = observation[5]
    left_contact = observation[6]
    right_contact = observation[7]

    # If the lander has touched down, stop engines
    if left_contact and right_contact:
        return 0

    def control_horizontal_velocity(x_vel):
        if x_vel > 0.1:
            return 1
        elif x_vel < -0.1:
            return 3
        return None

    def control_angle_stabilization(angle, ang_vel):
        if abs(angle) > 0.1:
            if angle > 0:  # Tilted right
                return 3
            elif angle < -0.1:  # Tilted left
                return 1
            elif ang_vel > 0.1:  # Clockwise rotation
                return 1
            elif ang_vel < -0.1:  # Counterclockwise rotation
                return 3
        return None

    def control_vertical_descent(y_vel, y_pos):
        if y_vel < -0.5 or (y_pos > 0.3 and y_vel < -0.1):  # Rapid descent, apply more thrust
            return 2
        elif y_vel < -0.1:  # Mild descent correction needed
            return 2
        return None

    # Priority 1: Horizontal velocity stabilization
    action = control_horizontal_velocity(x_vel)
    if action is not None:
        return action

    # Priority 2: Angle Stability
    action = control_angle_stabilization(angle, ang_vel)
    if action is not None:
        return action

    # Priority 3: Vertical descent control
    action = control_vertical_descent(y_vel, y_pos)
    if action is not None:
        return action

    # Default action: conserve fuel
    return 0
