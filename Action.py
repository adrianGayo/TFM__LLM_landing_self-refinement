import random 

def act(observation): 
  x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_contact, right_contact = observation[0], observation[1], observation[2], observation[3], observation[4], observation[5], observation[6], observation[7] 
  
  if left_contact or right_contact:  # touchdown event if any contact 
    return 0  # switch off engines 
  
  if x_vel > 0.1:  # move left
    return 1  # left engine 
  elif x_vel < -0.1:  # move right
    return 3  # right engine 
  
  if y_vel < -0.1:  # adjust descent
    return 2  # both engines up 
  
  if angle < -0.1:  # clockwise rotate
    return 3  # right engine 
  elif angle > 0.1:  # counter-clockwise rotate
    return 1  # left engine 
  
  return random.randint(0, 3)  # default, small random adjustments 
