
import os

def clickcam() :
    os.system("raspistill -w 480 -h 320 -q 100 -o picam.jpg")
    return
clickcam()
