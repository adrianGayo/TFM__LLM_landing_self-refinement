import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.2
SAFE_VERTICAL_SPEED = 0.4
SAFE_ANGLE = math.radians(5)

# Helper function to decide if action is needed

def should_fire_side_engines(angle):
    return abs(angle) > SAFE_ANGLE

# Main function to decide action based on observation

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Prioritize stabilizing the angle
    if should_fire_side_engines(angle) or abs(ang_vel) > SAFE_ANGLE / 2:
        return 1 if angle < 0 else 3  # Fire left or right engine accordingly
    
    # Control vertical speed
    if y_vel < -SAFE_VERTICAL_SPEED:
        return 2  # Fire main engine to slow descent

    # Control horizontal speed by reducing drift
    if abs(x_vel) > SAFE_HORIZONTAL_SPEED:
        return 1 if x_vel > 0 else 3  # Fire left or right engine accordingly

    # Fine correction to maintain horizontal position
    if abs(x_pos) > SAFE_HORIZONTAL_SPEED / 2:
        return 3 if x_pos < 0 else 1  # Adjust position left or right

    return 0  # Default action: turn off engines