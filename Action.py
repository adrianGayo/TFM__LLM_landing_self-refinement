import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    safe_angle = 0.1  # Safe angle range for upright landing
    max_safe_y_speed = -0.1  # Safe descent vertical speed
    max_horizontal_drift = 0.2  # Allowable horizontal speed
    max_ang_vel = 0.1  # Safe angular velocity range

    # If already contacted the ground
    if left_contact == 1 and right_contact == 1:
        return 0  # Engines off—landed successfully

    # Correct orientation
    if angle > safe_angle or ang_vel > max_ang_vel:
        return 3  # Push right to rotate left 
    elif angle < -safe_angle or ang_vel < -max_ang_vel:
        return 1  # Push left to rotate right

    # Manage descent—Control vertical speed
    if y_vel < max_safe_y_speed:  # Slow descent, push both engines
        return 2

    # Control horizontal speed only if angle-stable and ang_vel-secure within limits
    if abs(angle) < safe_angle and abs(ang_vel) < max_ang_vel:
        if x_vel > max_horizontal_drift:
            return 1  # Rectify rightward drift by pushing left
        elif x_vel < -max_horizontal_drift:
            return 3  # Rectify leftward drift by pushing right

    return 0  # Default: Turn off engines to conserve fuel

if __name__ == "__main__":
    # Sample observation for function verification
    sample_observation = np.array([0.1, 1.4, 0.05, -0.5, 0.01, 0.2, 0.0, 0.0])
    action = act(sample_observation)
    print(f"Determined action: {action}")