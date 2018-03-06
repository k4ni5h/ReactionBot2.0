import pyaudio
import numpy as np
import time

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
e=0
t=time.time()
while(True): #to it a few times just to see
    c=time.time()
    if c>=t+1:
        t=c
        print(e)
        e=0
    data = np.fromstring(stream.read(CHUNK, exception_on_overflow = False),
                         dtype=np.int32)
    data = np.abs(data)
    data2 = np.fromstring(stream2.read(CHUNK, exception_on_overflow = False),
                          dtype=np.int32)
    data2 = np.abs(data2)
    if np.max(data)>0.20*10**8:
        e+=1
    if np.max(data2)>0.60*10**8:
        e-=1

# close the stream gracefully
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
p.terminate()
p2.terminate()
p.terminate()
