import pyaudio
import numpy as np
import time
import math

import sys
sys.path.insert(0, '/home/pi/Desktop/ReactionBot2.0/motion/')
from funservo2 import rotat

np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 2048 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
p2=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,
              channels=1,
              rate=RATE,
              input=True,
              input_device_index = 2,
              frames_per_buffer=CHUNK) #uses default input device
stream2=p2.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                input_device_index = 3,
                frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
e1=e2=1.0
t=time.time()
while(True): #to it a few times just to see
    c=time.time()
    if c>=t+0.5:
        t=c
        angle=2*math.degrees(math.atan(e1/(e2*1.1)))-90
        print(angle)
        if angle>45:
			rotat(90-int(angle))
        if angle<-45:
			rotat(90-int(angle))
        e1=e2=1.0
    data = np.fromstring(stream.read(CHUNK,exception_on_overflow = False),
                         dtype=np.int32)
    data = np.abs(data)
    data2 = np.fromstring(stream2.read(CHUNK, exception_on_overflow = False),
                          dtype=np.int32)
    data2 = np.abs(data2)
    e1+=np.average(data)
    e2+=(np.average(data2))

# close the stream gracefully
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
p.terminate()
p2.terminate()
p.terminate()
