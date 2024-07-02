import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants for decision-making thresholds and corrective steps
    ANGLE_THRESHOLD = 0.1  # radians
    ANGLE_CORRECT_THRESHOLD = 0.05  # radians
    HORIZONTAL_VELOCITY_THRESHOLD = 0.1  # m/s
    VERTICAL_VELOCITY_THRESHOLD = -0.2  # m/s
    POSITION_THRESHOLD = 0.05  # meters

    # Base dynamic reassessment ensuring stable control across state elements
    if abs(x_pos) < POSITION_THRESHOLD and \
       abs(x_vel) < HORIZONTAL_VELOCITY_THRESHOLD and \
       abs(y_vel) < VERTICAL_VELOCITY_THRESHOLD and \
       abs(angle) < ANGLE_THRESHOLD and y_pos < POSITION_THRESHOLD:
        return 0  # Switch off engines

    # Handle pre-actions for stabilizing angle
    if abs(angle) > ANGLE_THRESHOLD:
        if angle > 0:
            return 1  # Push left engine on exceeding positive angle
        else:
            return 3  # Push right engine on exceeding negative angle

    # Prioritize correcting angular velocity beyond specific bounds for safety
    if ang_vel > ANGLE_CORRECT_THRESHOLD:
        return 1  # Engaging correction steps preferentially using left
    elif ang_vel < -ANGLE_CORRECT_THRESHOLD:
        return 3  # Engaging correction steps preferentially using right

    # Sequentially mitigate descent and dynamically allocate for velocity
    if y_vel <= VERTICAL_VELOCITY_THRESHOLD:
        return 2  # Start reducing drastic descent where necessary

    # Divert corrections ensuring balance for horizontal velocity proactively
    if x_vel >= HORIZONTAL_VELOCITY_THRESHOLD:
        return 3  # Start corrective engagements for horizontal velocity rightwards
    elif x_vel <= -HORIZONTAL_VELOCITY_THRESHOLD:
        return 1  # Start corrective engagements for horizontal velocity leftwards

    # Default process ensuring two-way downward thrust aligning stability
    return 2  # Engaging downward thrust process balancing in default flights
