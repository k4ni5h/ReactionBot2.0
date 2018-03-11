import pyaudio
import numpy as np
import time
import math
import threading
'''from multiprocessing import Process

def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()
# don't use scientific notation
'''
CHUNK = 2048 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)
d1=0
d2=0
def func(i):
    d=0
    t=time.time()
    p=pyaudio.PyAudio() # start the PyAudio class
    stream=p.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=RATE,
                  input=True,
                  input_device_index = i,
                  frames_per_buffer=CHUNK) #uses default input device
    while(True): #to it a few times just to see
        c=time.time()
        data = np.fromstring(stream.read(CHUNK,exception_on_overflow = False),
                             dtype=np.int32)
        data = np.abs(data)
        print(i, " : " ,np.argmax(data))
    stream.stop_stream()
    stream.close()
    p.terminate()

try:
    t1 = threading.Thread(target=func, args = (3,)).start()
    t2 = threading.Thread(target=func, args = (2,)).start()
    t1.join
    t2.join

except:
   print("Error: unable to start thread")

#runInParallel(func(1), func(2))
#np.set_printoptions(suppress=True)

# close the stream gracefully
