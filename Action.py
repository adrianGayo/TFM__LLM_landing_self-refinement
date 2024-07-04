import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.2
SAFE_VERTICAL_SPEED = 0.3
SAFE_ANGLE = 0.1
SAFE_ANGULAR_VELOCITY = 0.1

# Control gains
SIDE_ENGINE_THRESHOLD = math.radians(5)  # Angle threshold before using side engines

# Helper function to decide if angle correction is needed

def should_fire_side_engines(angle, ang_vel):
    return abs(angle) > SAFE_ANGLE or abs(ang_vel) > SAFE_ANGULAR_VELOCITY


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Stabilize the angle first
    if should_fire_side_engines(angle, ang_vel):
        if angle < 0 or ang_vel < 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine

    # Control vertical speed
    if y_vel < -SAFE_VERTICAL_SPEED:
        return 2  # Fire main engine to cut down vertical speed

    # Control horizontal speed
    if abs(x_vel) > SAFE_HORIZONTAL_SPEED:
        if x_vel > 0:
            return 1  # Fire left engine to reduce horizontal speed
        else:
            return 3  # Fire right engine
    
    # Fine-tuning in case the angle is beyond marginal safety but not too severe
    if abs(angle) > SIDE_ENGINE_THRESHOLD:
        if angle > 0:
            return 1  # Fire left engine
        else:
            return 3  # Fire right engine

    return 0  # Default action: turn off engines
