import PCF8591 as ADC
import RPi.GPIO as GPIO

photoresistor = ADC(0x48)

# set up led
ledPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

# turn on led
GPIO.output(ledPin, 1)

# make sure to hook up middle jumper
photo = photoresistor.read(0)
print(photo)





