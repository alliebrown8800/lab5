import PCF8591
import RPi.GPIO as GPIO

# set up adc
PCF8591.setup(0x48)

# set up led
ledPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

# turn on led
GPIO.output(ledPin, 1)

# make sure to hook up middle jumper
photo = PCF8591.read(0)
print(photo)





