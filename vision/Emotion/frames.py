# recording.py
from picamera import PiCamera
from time import sleep
#camera = PiCamera()
#camera.start_preview()
#camera.start_recording("recorded.h264")
#camera.wait_recording(10)
#camera.stop_recording()
#camera.stop_preview()
#import cv2
vidcap = cv2.VideoCapture("recorded.h264")
success,image = vidcap.read()
#count = 0
success = True
while success:
    success,image = vidcap.read()
    #print('Read a new frame: ', success)
    cv2.imwrite("frame.jpg", image)     # save frame as JPEG file
