import math

# Constants for safe landing
SAFE_HORIZONTAL_SPEED = 0.2
SAFE_VERTICAL_SPEED = 0.4
SAFE_ANGLE = 0.1
ANGLE_TOLERANCE = math.radians(5)

# Helper function to decide if action is needed


def should_fire_side_engines(angle):
    return abs(angle) > ANGLE_TOLERANCE


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation
    
    # Step 1: Stabilize angle, primary critical level correction
    if should_fire_side_engines(angle) or abs(ang_vel) > ANGLE_TOLERANCE:
        if angle < 0:
            return 1  # Left engine correcting leftward
        else:
            return 3  # Right Engine correcting rightward
            
    # Step 2: Vertical Speed regulation descending preventing abrupt falls
    if y_vel < -SAFE_VERTICAL_SPEED:
        return 2  # Initiate central thruster slightly dampening vertical speed

    # Step 3: Drift management broad-level horizontal speed standard
    if abs(x_vel) > SAFE_HORIZONTAL_SPEED:
        if x_vel > 0:
            return 1  # Rightward drift reducing manageable speed
        else:
            return 3  # Leftward drift manageable allowing correction toward center

    # Positional minor tweaks hard ensuring gradual controlled stable disposition
    if abs(x_pos) > SAFE_HORIZONTAL_SPEED:
        if x_pos < 0:
            return 3  # Correct positional offset rightwards minor boost
        else:
            return 1  # Correct positional drift leftwards reintegration

    # Last Step: Angle steady ensuring maintained straight vertical aligned nearer descent
    if abs(angle) > SAFE_ANGLE:
        if angle > 0:
            return 1  # Minor stabilization for left correction ensuring nearer centered
        else:
            return 3  # Minor stabilization, right maintaining near aligned

    # Default state stable mild fluctuations handling minimum resources displaced
    return 0
