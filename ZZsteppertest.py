import time
from stepper import Stepper

myMotor = Stepper() # the stepper motor
prev_angle = 0 # assume starting angle is zero

while True: # if slider was submitted
  new_angle = prev_angle + 60
  myMotor.goAngle(prev_angle,new_angle) # go to that angle
  prev_angle = new_angle # prev_angle is now this angle
  time.sleep(3)
  



