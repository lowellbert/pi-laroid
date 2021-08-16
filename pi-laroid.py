import os
from picamera import PiCamera
import time 
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()
camera.resolution = (3280, 2464) #Max resolution = 3280 x 2464 #print resolution = 512, 384

LED = 21
BUTTON = 20
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)


#def take_picture_and_print():
    #"raspistill command details
    # -n = nopreview
    # -t = timeout : Time (in ms) before takes picture and shuts down (if not specified, set to 5s)
    # -w = width: set image width
    # -h = height: set image height
    # -o = output:  Output filename (to write to stdout, use '-o -'). If not specified, no file is saved
    # -lp = print a file "
    #raspistill -n -t 200 -w 512 -h -384 -o - | lp 

def main():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)
    camera_preview()

    


def camera_preview():
    camera.start_preview()
    sleep(5)
    camera.stop_preview

main()
GPIO.cleanup()

