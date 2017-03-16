from picamera import PiCamera
from time import sleep
import sys
camera = PiCamera()
camera.resolution=(320,240)
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/gui/detect/test.jpg')
camera.stop_preview()
