import numpy as np


def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    safe_angle = 0.05  # Safer angle range to correct smaller deviations
    max_safe_y_speed = -0.2  # Safer vertical speed
    max_safe_x_speed = 0.1  # Horizontal speed threshold
    max_ang_vel = 0.2  # Angular velocity threshold

    # If already contacted the ground
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines, we're landed

    # Correct spacecraft's angle and angular velocity
    if angle > safe_angle or ang_vel > max_ang_vel:
        return 3  # Push right engine to rotate left
    elif angle < -safe_angle or ang_vel < -max_ang_vel:
        return 1  # Push left engine to rotate right

    # Correct horizontal speed
    if abs(y_vel) > 0.5 and abs(x_vel) > max_safe_x_speed:
        if x_vel > max_safe_x_speed:
            return 1  # Push left engine to move left
        elif x_vel < -max_safe_x_speed:
            return 3  # Push right engine to move right

    # Control vertical speed
    if y_vel < max_safe_y_speed:  # If descending too fast
        return 2  # Push both engines to slow down descent
    return 0  # Turn off engines to conserve fuel

if __name__ == "__main__":
    # Sample observation for testing
    sample_observation = np.array([0.1, 1.4, 0.05, -0.5, 0.01, 0.2, 0.0, 0.0])
    action = act(sample_observation)
    print(f"Decided action: {action}")