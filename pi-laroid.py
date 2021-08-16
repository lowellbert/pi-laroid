import os
from picamera import PiCameara
from time import sleep

camera = PiCamera()

def take_picture_and_print():
    #"raspistill command details
    # -n = nopreview
    # -t = timeout : Time (in ms) before takes picture and shuts down (if not specified, set to 5s)
    # -w = width: set image width
    # -h = height: set image height
    # -o = output:  Output filename (to write to stdout, use '-o -'). If not specified, no file is saved
    # -lp = print a file "
    raspistill -n -t 200 -w 512 -h -384 -o - | lp 

def main():
    take_picture_and_print()


main()

