import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.2
SAFE_VERTICAL_SPEED = 0.4
SAFE_ANGLE = 0.1

# Control gains
ANGLE_TOLERANCE = math.radians(5)
VEL_TOLERANCE = 0.1

# Helper function to decide if action is needed

def should_fire_side_engines(angle):
    return abs(angle) > ANGLE_TOLERANCE


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Step 1: Stabilize angle control first, primary aspect stability
    if should_fire_side_engines(angle) or abs(ang_vel) > ANGLE_TOLERANCE:
        if angle < 0:
            return 1  # Fire left engine, stabilizing leftward
        else:
            return 3  # Fire right engine, stabilizing rightward
    
    # Step 2: Vertical speed moderation preventing rapid fall
    if y_vel < -SAFE_VERTICAL_SPEED:
        return 2  # Fire main engine for slowing descent

    # Step 3: Horizontal speed control to prevent drifts, manageable limits
    if abs(x_vel) > SAFE_HORIZONTAL_SPEED:
        if x_vel > 0:
            return 1  # Correction leftwards
        else:
            return 3  # Correction rightwards

    # Step 4: Minor positional tweaks closer proximity steady
    if abs(x_pos) > SAFE_HORIZONTAL_SPEED:
        if x_pos < 0:
            return 3  # Fire right engine incrementally
        else:
            return 1  # Fire left engine incrementally

    # Default stable when corrections unnecessary.
    return 0
