import numpy as np

def act(observation):
    x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation

    # Constants
    safe_angle = 0.05  # Define a safer angle range to correct smaller deviations
    max_safe_speed = -0.3  # Define a safer vertical speed
    max_horizontal_drift = 0.02  # Limit horizontal drift to a minimal value
    ang_vel_threshold = 0.5  # Angular velocity threshold to stabilize the spacecraft

    # If already contacted the ground
    if left_contact == 1 and right_contact == 1:
        return 0  # Turn off engines, we're landed

    # If the spacecraft is tilting too much to the left or right, correct it by using side thrusters
    if angle > safe_angle or ang_vel > ang_vel_threshold:
        return 3  # Push right engine to rotate left
    elif angle < -safe_angle or ang_vel < -ang_vel_threshold:
        return 1  # Push left engine to rotate right

    # If horizontal velocity is too high, counteract it:
    if x_vel > max_horizontal_drift:
        return 1  # Push left engine to move left
    elif x_vel < -max_horizontal_drift:
        return 3  # Push right engine to move right

    # Control the vertical speed - reduce descent speed
    if y_vel < max_safe_speed:  # If descending too fast
        return 2  # Push both engines to slow down
    else:
        return 0  # Otherwise, turn off engines to save fuel

    return 0  # Default action is doing nothing

if __name__ == "__main__":
    # Sample observation for testing the function
    sample_observation = np.array([0.1, 1.4, 0.05, -0.5, 0.01, 0.2, 0.0, 0.0])
    action = act(sample_observation)
    print(f"Decided action: {action}")