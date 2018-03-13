import pyaudio
import numpy as np
import time
import math

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
e=0.0
t=time.time()
f=1.2
while(True): #to it a few times just to see
    c=time.time()
    if c>=t+1:
        t=c
        print(e,math.degrees(math.atan(e)))
        e=1.0
        d=d2=0.0
    data = np.fromstring(stream.read(CHUNK, exception_on_overflow = False),
                         dtype=np.int32)
    data = np.abs(data)
    data2 = np.fromstring(stream2.read(CHUNK, exception_on_overflow = False),
                          dtype=np.int32)
    data2 = np.abs(data2)
    e=e+(np.max(data)-f*np.max(data2))/(np.max(data)+f*np.max(data2))

# close the stream gracefully
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
p.terminate()
p2.terminate()
p.terminate()

