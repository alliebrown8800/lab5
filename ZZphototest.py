import PCF8591
import RPi.GPIO as GPIO

photoresistor = PCF8591(0x48)

# set up led
ledPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

# turn on led
GPIO.output(ledPin, 1)

# make sure to hook up middle jumper
photo = photoresistor.read(0)
print(photo)





