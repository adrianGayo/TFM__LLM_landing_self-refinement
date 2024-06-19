def act(observation):
    
    # Check if time is less than 100 for initial maneuvers
    if observation[0] < 100:
        # Accelerate downwards to stabilize the descending ship
        if observation[3] < -0.25:
            return 3
        # Slow down the ship to control landing speed
        elif observation[2] > 0.1:
            return 1
        # Make small adjustments before landing
        else:
            return 2
    
    # After time 100, start the landing procedure
    else:
        # Land gently by adjusting the ship's tilt and speed
        if observation[3] < -0.15:
            return 3
        elif observation[2] > 0.06:
            return 1
        else:
            return 2