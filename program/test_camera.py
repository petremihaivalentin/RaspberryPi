from picamera import PiCamera
from time import sleep




camera = PiCamera()

camera.start_preview()
sleep(120)
#camera.capture('/home/pi/test/test_magnets.png')
camera.stop_preview()


