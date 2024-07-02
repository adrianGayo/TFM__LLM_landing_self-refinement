import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    action = 0  # Default action is to turn off all engines
    # Start immediate control of vertical descent
    if y_vel <= -0.1:  # Trigger engines to slow down descent early on
        action = 2
    # Correct larger angle deviations first
    if abs(angle) > 0.3: 
        action = 1 if angle > 0 else 3
    # Prioritize correcting horizontal drift while handling tilt
    elif abs(x_vel) > 0.2 or abs(ang_vel) > 0.3:
        if x_vel > 0.2:  # drifting right
            action = 1
        elif x_vel < -0.2:  # drifting left
            action = 3
    # Consistent control to slow descent
    if y_vel <= -0.5:  # Further slow vertical descent.
        action = 2
    return action
