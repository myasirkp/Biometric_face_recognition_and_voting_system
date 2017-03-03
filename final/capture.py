from picamera import PiCamera
from time import sleep
import sys
camera = PiCamera()
camera.resolution=(320,240)
for i in range(1,11):
    path='/home/pi/Desktop/New/train/'
    arg=sys.argv[1]
    path=path+arg+'.'+str(i)+'.jpg'
    camera.start_preview()
    sleep(3)
    camera.capture(path)
    camera.stop_preview()
