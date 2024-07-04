import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.15
SAFE_VERTICAL_SPEED = 0.25
SAFE_ANGLE = math.radians(5)  # About 0.087 radians

# Helper function to decide if action is needed

def should_fire_side_engines(angle, ang_vel):
    	return abs(angle) > SAFE_ANGLE or abs(ang_vel) > SAFE_ANGLE / 2

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    	# Defaults to turning off engines if no immediate action is needed
    action = 0
    
    # Stabilize the angle first
    if should_fire_side_engines(angle, ang_vel):
        if angle < 0:
            action = 1  # Fire left engine
        else:
            action = 3  # Fire right engine
    
    # Control vertical speed
    elif y_vel < -SAFE_VERTICAL_SPEED:
        action = 2  # Fire main engine to reduce vertical speed

    # Control horizontal speed
    elif abs(x_vel) > SAFE_HORIZONTAL_SPEED:
        if x_vel > 0:
            action = 1  # Fire left engine to reduce horizontal speed
        else:
            action = 3  # Fire right engine to reduce horizontal speed
    
    # Fine positioning adjustments close to landing zone
    elif abs(x_pos) > SAFE_HORIZONTAL_SPEED / 2:
        if x_pos < 0:
            action = 3  # Fire right engine to nudge left
        else:
            action = 1  # Fire left engine to nudge right
        
    return action
