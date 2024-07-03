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

        # Vertical speed control
        if vy < SAFE_VERTICAL_SPEED:
            thrust += 1
        elif vy > -0.5:  # Reduce excessive upward thrust
            thrust -= 1

        # Horizontal alignment with rotation
        if abs(x) > CLOSE_DISTANCE:
            rotate = -1 if x > 0 else 1  # Rotate towards center line
            if abs(vx) > SAFE_HORIZONTAL_SPEED:
                thrust += 1  # Control horizontal speed

        # Fine adjustments near the ground for smooth landing
        if y < 10:
            if vy < -1:  # Stable descent speed near ground
                thrust += 1
            if abs(vx) > 0.5:
                thrust += 1

        # Ensure thrust within operational limits
        thrust = min(4, max(0, thrust))

        return [rotate, thrust]