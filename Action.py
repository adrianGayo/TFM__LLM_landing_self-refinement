def act(observation):
    speed_x = observation[0]
    speed_y = observation[1]
    pos_x = observation[2]
    pos_y = observation[3]
    angle = observation[4]
    speed_angle = observation[5]
    side_engine = observation[6]
    center_engine = observation[7]
    score = 0
    
    if center_engine == 1:
        score -= 0.3
    if side_engine == 1:
        score -= 0.03
    if pos_y > 1.07:
        score -= 0.2
    if pos_y < 1.03:
        score += 0.2
    if angle < -0.15:
        score -= 0.15
    if speed_angle < 0.08:
        score += 0.08
    if abs(speed_x) < 0.02 and abs(speed_y) < 0.02:
        score += 100
    
    return score