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
        CLOSE_DISTANCE = 5

        # Continuous vertical speed control
        if vy < SAFE_VERTICAL_SPEED:
            thrust += 1
        elif vy > -0.5:
            thrust -= 1

        # Frequent rotational adjustments for horizontal alignment
        if abs(x) > CLOSE_DISTANCE:
            rotate = -1 if x > 0 else 1  # Adjust rotation towards center
            if abs(vx) > SAFE_HORIZONTAL_SPEED:
                thrust += 1  # Control horizontal speed

        # Fine adjustments when near the ground
        if y < 10:
            if vy < -0.5:
                thrust += 1
            if abs(vx) > 0.5:
                thrust += 1

        # Ensure thrust is within limits
        thrust = min(4, max(0, thrust))

        return [rotate, thrust]