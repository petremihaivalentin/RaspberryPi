import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)
#print('Magnet off')
print('15 seconds to set up')
GPIO.output(2,GPIO.HIGH)
time.sleep(15)
#GPIO.output(2,GPIO.LOW)