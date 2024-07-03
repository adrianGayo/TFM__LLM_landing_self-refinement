import numpy as np

def act(observation):
    X_position, Y_position, X_velocity, Y_velocity, angle, angular_velocity, left_contact, right_contact = observation

    if left_contact == 1 and right_contact == 1:
        return 0  # If both contacts are made, engines off
    
    # Immediate Angle Control - Prioritized Loop
    if angle > 0.1:  # tilted right
        return 1  # push left engine
    elif angle < -0.1:  # tilted left
        return 3  # push right engine
    
    # Horizontal Movement Control - X_velocity stabilization
    if X_velocity > 0.2 and X_position > 0.1:  # moving fast right
        return 1  # push left engine
    elif X_velocity < -0.2 and X_position < -0.1:  # moving fast left
        return 3  # push right engine
    
    # Vertical Control: Managed Descent
    if Y_velocity < -0.5:  # descending rapidly
        return 2  # push both engines
    elif Y_velocity < -0.2 and Y_position > 0.4:  # managing speed at higher altitude
        return 2  # moderate engine push
    elif Y_velocity > -0.1 and Y_position < 0.3:  # approaching land
        return 2  # soften descent
    elif Y_velocity > 0:  # moving upwards
        return 0  # engine off ensuring counter reduction of positive elevation

    return 0  # Default engines off ensuring stability
