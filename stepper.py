import RPi.GPIO as GPIO
import time
from PCF8591 import PCF8591

# Pin setup
ledPin = 20 # you can change this
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT) # led pin is output

# ADC setup
photoresistor = PCF8591(0x48)

class Stepper:

  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    self.pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
    for pin in self.pins:
      GPIO.setup(pin, GPIO.OUT, initial=0) # all pins are outputs
    # Define the pin sequence
    self.sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
    self.state = 0 # current position in stator sequence
  
  def __delay_us(self, tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass

  def __halfstep(self, dir):
    # dir = +1 for CCW and -1 for CW
    self.state += dir
    if self.state > 7:   self.state = 0
    elif self.state < 0: self.state = 7
    for pin in range(4):    # 4 pins that need to be energized
      GPIO.output(self.pins[pin], self.sequence[self.state][pin])
    self.__delay_us(1000) # FIGURE OUT HOW FAR TO PUSH THIS VALUE (MINIMIZE IT)
    # Note: a full rotation is 4096 half-steps

  def __moveSteps(self, steps, dir):
    # move the actuation sequence a specified number of half steps
    for step in range(steps):
      self.__halfstep(dir)

  def goAngle(self, prev_angle, new_angle):
    # angle in range of zero to 359; 0 is left (zeroed) 90 is up etc
    diff = prev_angle - new_angle # difference between 2 angles
    if diff != 0:
      if abs(diff) > 180: # this means it would be better to move the other way
        if diff > 0: diff = diff - 360
        elif diff < 0: diff = diff + 360
      halfsteps = abs(diff*11.38)
      self.__moveSteps(halfsteps, diff/diff) # move the specified angle in the specified direction (diff/diff will be 1 or -1)

  def zero(self, prev_angle):
    threshold = 100 # threshold for if cardboard is covering (change if needed)
    if prev_angle <= 180: # for most efficient direction
      dir = 1 # turn counterclockwise
    else:
      dir = -1 # turn clockwise
    GPIO.output(ledPin, 1) # turn LED on
    photo = photoresistor.read(0) # read photoresistor value
    while photo < threshold: # while the light is still on the photoresistor...
      self.__moveSteps(8, dir) # move 8 half steps in the specified direction
      photo = PCF8591.read(0) # read photoresistor value
    GPIO.output(ledPin, 0) # once done, turn off LED

