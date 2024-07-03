class Agent:
    def __init__(self):
        pass

    def act(self, observation):
        position, velocity = observation['position'], observation['velocity']
        x, y = position
        vx, vy = velocity

        # Initialize actions
        thrust = 0
        rotate = 0 

        # Define thresholds
        SAFE_VERTICAL_SPEED = -2  # Safe descent speed
        SAFE_HORIZONTAL_SPEED = 1  # Safe lateral speed
        CLOSE_DISTANCE = 5  # Close to landing zone margin

        # Vertical stabilization
        if vy < SAFE_VERTICAL_SPEED:  # Falling too fast
            thrust += 1  # Increase thrust to slow descent

        # Horizontal stabilization
        if abs(x) > CLOSE_DISTANCE and abs(vx) > SAFE_HORIZONTAL_SPEED:  # Too far laterally and moving fast
            thrust += 1  # Correct lateral position

        # Fine adjustments near ground
        if y < 10:
            if vy < -0.5:
                thrust += 1
            if abs(vx) > 0.5:
                thrust += 1

        # Ensure thrust is within limits
        thrust = min(4, max(0, thrust))

        return [rotate, thrust]