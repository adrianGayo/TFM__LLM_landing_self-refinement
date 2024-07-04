import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.2
SAFE_VERTICAL_SPEED = 0.4
SAFE_ANGLE = 0.1

# Control gains
ANGLE_TOLERANCE = math.radians(5) # around 0.087 radians as before
VEL_TOLERANCE = 0.1

# Helper function to decide if action is needed


def should_fire_side_engines(angle):
    return abs(angle) > ANGLE_TOLERANCE


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Prioritize angle stabilization first
    if should_fire_side_engines(angle) or abs(ang_vel) > ANGLE_TOLERANCE:
        if angle < 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine
    
    # Control vertical speed even before it gets too fast
    if y_vel < -SAFE_VERTICAL_SPEED * 4:  # Early stronger bursts when falling too fast
        return 2  # Fire main engine to reduce vertical speed
    elif y_vel < -SAFE_VERTICAL_SPEED:  # Regular adjustment
        return 2  # Main engine

    
    # Control horizontal speed early
    if abs(x_vel) > SAFE_HORIZONTAL_SPEED * 4:  # Early stronger burst when moving very fast horizontally
        if x_vel > SAFE_HORIZONTAL_SPEED:
            return 1  # Fire left engine to reduce speed
        else:
            return 3  # Fire right engine to reduce speed
    elif abs(x_vel) > SAFE_HORIZONTAL_SPEED:  # Adjustment when in range
        if x_vel > 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine

    
    # Lastly, fix any remaining positional errors closer to ground and more subtle approach
    if abs(x_pos) > SAFE_HORIZONTAL_SPEED:  # maintain slightly above threshold for positional correction
        if x_pos < 0:
            return 3  # Fire right engine to move left
        else:
            return 1  # Fire left engine to move right
    
    # For minimal required fine adjustments, hover nearer to ground and less abrupt integrations
    if abs(angle) > SAFE_ANGLE:
        if angle > 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine

    return 0  # Default action: turn off engines


