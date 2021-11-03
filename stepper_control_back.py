import json
import Stepper
import time

myMotor = Stepper() # the stepper motor
prev_angle = 0 # assume starting angle is zero

while True: # continuous loop
  with open("lab5.json", 'r') as f: # open text file
    data = json.load(f) # retrieve json data from txt
  new_angle = float(data['angle']) # the new angle from slider (or 0 if zero is yes)
  zero = str(data['zero']) # yes or no (zero)

  if zero == 'yes': # if zeroing was selected
    myMotor.zero(prev_angle) # zero the motor
    prev_angle = new_angle # now prev_angle will be zero
    with open("lab5.json", 'w') as f: # open json
      data = {"angle":prev_angle, "zero":'no'} # angle is zero, zero is no
      json.dump(data,f) # insert data

  elif zero == 'no': # if slider was submitted
    myMotor.goAngle(prev_angle,new_angle) # go to that angle
    prev_angle = new_angle # prev_angle is now this angle
    
  time.sleep(0.1)# background code