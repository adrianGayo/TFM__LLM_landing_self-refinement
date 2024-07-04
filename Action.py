import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.2
SAFE_VERTICAL_SPEED = 0.4
SAFE_ANGLE = 0.1
ANGLE_TOLERANCE = math.radians(5)

# Helper function to decide if action is needed
def should_fire_side_engines(angle):
    return abs(angle) > ANGLE_TOLERANCE

# Main function to decide action based on observation
def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Stabilize the angle first
    if should_fire_side_engines(angle) or abs(ang_vel) > ANGLE_TOLERANCE:
        if angle < 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine
        
    # Control vertical speed
    if y_vel < -SAFE_VERTICAL_SPEED:
        return 2  # Fire main engine to reduce vertical speed

    # Control horizontal speed
    if abs(x_vel) > SAFE_HORIZONTAL_SPEED:
        if x_vel > 0:
            return 1  # Fire left engine to reduce horizontal speed
        else:
            return 3  # Fire right engine to reduce horizontal speed

    # Positional Adjustments and Maintain Alignment
    if abs(x_pos) > SAFE_HORIZONTAL_SPEED:
        if x_pos < 0:
            return 3  # Fire right engine to lurch left
        else:
            return 1  # Fire left engine to lurch right
    
    # Ensure the lander is aligned vertically
    if abs(angle) > SAFE_ANGLE:
        if angle > 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine
    return 0  # Default action: turn off engines
