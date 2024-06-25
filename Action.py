import numpy as np

def act(ob):
    distance_to_center = np.sqrt(ob[0] ** 2 + ob[1] ** 2)
    
    # Speed control
    if ob[1] > -0.4:
        action = 2  # Decrease altitude
    else:
        # Position control
        if distance_to_center > 0.24:  # Move closer to the center
            if ob[0] > 0:
                action = 1  # Move to the left
            else:
                action = 3  # Move to the right
        else:
            action = 0  # Maintain current position
    
    # Tilt control
    if ob[3] > 0.2:
        action = 1  # Correct left tilt
    if ob[3] < -0.2:
        action = 3  # Correct right tilt
    
    # Firing engine penalty
    if action == 1 or action == 3:
        ob_action = ob[action + 5]
        if ob_action > 0:
            if action == 1:
                ob[7] -= 0.3  # Penalty for left engine firing
            else:
                ob[7] -= 0.3  # Penalty for right engine firing
        else:
            ob[7] -= 0.03  # Penalty for side engine firing
    
    # Score calculation
    score = ob[7]
    if action == 0:
        score += 100  # Successful landing
    
    return action, score

# Test the function with the last observation
test_observation = [0.087, -0.001, 0.0, -0.0, 0.001, 0.0, 1.0, 1.0]
action, score = act(test_observation)
print("Action to take:", action)
print("Score:", score)