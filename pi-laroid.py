import os
from picamera import PiCamera
import time 
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()
camera.resolution = (3280, 2464) #Max resolution = 3280 x 2464 #print resolution = 512, 384

LED = 16
BUTTON = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
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
    while True:
        #turn_on_button_led() 
        print("wait for button")
        print("Button Status = ", GPIO.input(BUTTON))
        if GPIO.input(BUTTON) == 1:
            print("button pressed")
            camera_preview()
        else:
            print("flash LED")
            turn_on_button_led()
                
    print("Button Status = ", GPIO.input(BUTTON))

    
def turn_on_button_led():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)

def camera_preview():
    camera.start_preview()
    GPIO.output(LED, GPIO.HIGH)
    sleep(5)
    camera.stop_preview()
    GPIO.output(LED, GPIO.LOW)
    sleep(1)

main()
GPIO.cleanup()
