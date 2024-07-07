import numpy as np

def act(observation):
    # Extract observations for better readability
    xpos, ypos, xvel, yvel, angle, ang_vel, left_contact, right_contact = observation
    
    # Target states for successful landing
    target_xvel, target_yvel = 0, -0.5  # Target a controlled descent
    max_yvel = -1.0  # Safety threshold for descent speed
    max_angle = 0.1  # Tighter control on angle for stability

    # Action decision logic
    if ypos > 0.5:  # Higher altitude, prioritize descent control
        if abs(angle) > max_angle or abs(ang_vel) > 0.1:  # Stabilize angle early
            if angle < 0: return 1
            else: return 3
        elif yvel < max_yvel:  # Improve vertical speed control
            return 2
        elif abs(xvel) > 0.1:  # Fine-tune horizontal speed
            if xvel > 0: return 1
            else: return 3
    elif ypos > 0.3:  # Medium altitude, balance descent and horizontal drift
        if yvel < target_yvel:  # Smooth descent
            return 2
        elif abs(angle) > max_angle or abs(ang_vel) > 0.1:  # Angle stability
            if angle < 0: return 1
            else: return 3
        elif abs(xvel) > 0.05:  # Reduce horizontal drift
            if xvel > 0: return 1
            else: return 3
    elif ypos > 0.1:  # Lower altitude, prepare for landing
        if abs(angle) > max_angle:  # Ensure minimal angle
            if angle < 0: return 1
            else: return 3
        elif abs(xvel) > 0.02:  # Maintain low horizontal speed
            if xvel > 0: return 1
            else: return 3
        elif yvel < target_yvel:  # Control descent speed
            return 2
    else:  # Very near ground, ensure stable touchdown
        if not (left_contact and right_contact):  # Touchdown stability
            if abs(xvel) > 0.01:  # Minimize lateral drift
                if xvel > 0: return 1
                else: return 3
            elif abs(angle) > max_angle:  # Prevent tilt at touchdown
                if angle < 0: return 1
                else: return 3
            elif yvel < max_yvel:  # Gentle descent at landing
                return 2

    return 0  # Default to engine off if stable and near ground
