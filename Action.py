def act(observation):
  x_position, y_position, x_velocity, y_velocity, angle, angular_velocity, left_contact, right_contact = observation

  # Control horizontal speed
  if abs(x_velocity) > 0.2:
    if x_velocity > 0:
      return 1  # Engage left engine
    else:
      return 3  # Engage right engine

  # Control vertical speed when descending fast
  if y_velocity < -0.5:
    return 2  # Engage center engine

  # Maintain upright position
  if abs(angle) > 0.1:
    if angle > 0:
      return 3  # Correct tilt by engaging right engine
    else:
      return 1  # Correct tilt by engaging left engine

  # Fine-tune adjustments closer to landing area
  if y_position < 0.3:
    if abs(x_position) > 0.1:
      if x_position < 0:
        return 3  # Adjust right to center
      else:
        return 1  # Adjust left to center
    else:
      return 2  # Gentle descent in a safe method

  # Default descent with no immediate adjustment needed
  return 0  # Controlled descent switching off engines