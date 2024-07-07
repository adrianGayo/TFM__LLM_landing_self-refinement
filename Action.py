import numpy as np

def act(observation):
    # Extract observations for better readability
    xpos, ypos, xvel, yvel, angle, ang_vel, left_contact, right_contact = observation
    
    # Target states for successful landing
    target_xvel, target_yvel = 0, -0.1  # Target a gentle descent
    max_yvel = -0.2  # More negative means going down too fast
    max_angle = 0.1

    # Action decision logic
    if ypos > 0.5:  # Higher altitude, prioritize stabilizing descent and horizontal position
        if abs(angle) > max_angle or abs(ang_vel) > 0.1:  # Need to stabilize angle
            return 1 if angle < 0 else 3
        elif yvel < max_yvel:  # Too fast vertical descent
            return 2
        elif abs(xvel) > 0.1:  # Moving horizontally, need correction
            return 1 if xvel > 0 else 3
    elif ypos > 0.1:  # Medium altitude, fine tuning positions and angles
        if abs(angle) > max_angle:  # Stabilize
            return 1 if angle < 0 else 3
        elif abs(xvel) > 0.05:  # Further reduce horizontal speed
            return 1 if xvel > 0 else 3
        elif yvel < target_yvel:  # Apply gentle descent
            return 2
    else:  # Near ground, ensure contacts are light and balanced
        if not (left_contact and right_contact):  # Contacts not touched down
            if abs(xvel) > 0.05:  # Minimize horizontal drift
                return 1 if xvel > 0 else 3
            elif abs(angle) > max_angle:  # Stabilize angle
                return 1 if angle < 0 else 3
            elif yvel < max_yvel:  # Slow down vertical speed
                return 2

    return 0  # Default action is to switch off engines if stable
