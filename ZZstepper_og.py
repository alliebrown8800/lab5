import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0 # current position in stator sequence

# technically not necessary for python3
def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

# new modified code
def halfstep(dir):
  # dir = +1 for CCW and -1 for CW
  state += dir
  if state > 7:   state = 0
  elif state < 0: state = 7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000) # FIGURE OUT HOW FAR TO PUSH THIS VALUE (MINIMIZE IT)

def moveSteps(steps, dir):
  # move the actuation sequence a specified number of half steps
  for step in steps:
    halfstep(dir)

try:
  moveSteps(1000,1) # counterclockwise 1000 halfsteps
  moveSteps(1000,-1)
except:
  pass
GPIO.cleanup() 