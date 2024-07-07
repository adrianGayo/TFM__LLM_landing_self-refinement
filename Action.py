import numpy as np

def act(observation):
    # Extract observations for better readability
    xpos, ypos, xvel, yvel, angle, ang_vel, left_contact, right_contact = observation
    
    # Target states for successful landing
    target_xvel, target_yvel = 0, -0.5  # Target gentle descent
    max_yvel = -1.0  # Max descent speed threshold
    max_angle = 0.1  # Max angle threshold
    min_angle_control = 0.02  # Minimal angle adjustment threshold

    # Action decision logic
    if ypos > 0.5:  # Higher altitude
        if abs(angle) > max_angle or abs(ang_vel) > 0.1:  # Stabilize angle early
            if angle < 0:
                return 1
            return 3
        if yvel < max_yvel:  # Control vertical speed
            return 2
        if abs(xvel) > 0.1:  # Horizontal stability
            if xvel > 0:
                return 1
            return 3
    elif ypos > 0.3:  # Medium altitude
        if yvel < target_yvel:  # Approaching gentle descent
            return 2
        if abs(angle) > min_angle_control:  # Correct minimal angle deviations
            if angle < 0:
                return 1
            return 3
        if abs(xvel) > 0.05:  # Correct horizontal drift
            if xvel > 0:
                return 1
            return 3
    elif ypos > 0.1:  # Lower altitude
        if abs(angle) > min_angle_control:  # Correct angle
            if angle < 0:
                return 1
            return 3
        if abs(xvel) > 0.02:  # Control horizontal speed
            if xvel > 0:
                return 1
            return 3
        if yvel < target_yvel:  # Ensure gentle descent
            return 2
    else:  # Near ground, ensure smooth touchdown
        if not (left_contact and right_contact):  # Stabilize landing
            if abs(xvel) > 0.01:  # Minimize lateral drift
                if xvel > 0:
                    return 1
                return 3
            if abs(angle) > min_angle_control:  # Maintain angle stability
                if angle < 0:
                    return 1
                return 3
            if yvel < max_yvel:  # Controlled descent
                return 2

    return 0  # Default to engine off if stable
