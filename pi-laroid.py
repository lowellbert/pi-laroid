import os
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (3280, 2464) #Max resolution = 3280 x 2464 #print resolution = 512, 384


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
    take_picture_and_print()
    camera.start_preview()


main()

