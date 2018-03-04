import pyaudio
import numpy as np
import time

np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 2048 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
p2=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,input_device_index = 2,
              frames_per_buffer=CHUNK) #uses default input device
stream2=p2.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,input_device_index = 3,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
e=0.0
t=time.time()
d=d2=0.0
while(True): #to it a few times just to see
    c=time.time()
    if c>=t+1:
        t=c
        print(e*10**4, d/d2)
        e=1.0
    data = np.fromstring(stream.read(CHUNK, exception_on_overflow = False),dtype=np.int32)
    data = np.abs(data)
    data2 = np.fromstring(stream2.read(CHUNK, exception_on_overflow = False),dtype=np.int32)
    data2 = np.abs(data2)
    e=e+(np.max(data)-2*np.max(data2))/(np.max(data)+2*np.max(data2))
    d+=np.max(data)
    d2+=np.max(data2)
    #print("peak :",np.max(data), "time :",datetime.datetime.now().time())
    #data = data * np.hanning(len(data)) # smooth the FFT by windowing data
    #fft = abs(np.fft.fft(data).real)
    #fft = fft[:int(len(fft)/2)] # keep only first half
    #freq = np.fft.fftfreq(CHUNK,1/RATE)
    #freq = freq[:int(len(freq)/2)] # keep only first half
    #freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1
    #if freqPeak>500:
    #    print("peak frequency: %d Hz"%freqPeak, datetime.datetime.now().time())
    #print("peak frequency: %d Hz"%freqPeak, datetime.datetime.now().time())
    # uncomment this if you want to see what the freq vs FFT looks like
    #plt.plot(freq,fft)
    #plt.axis([0,4000,None,None])
    #plt.show()
    #plt.close()

# close the stream gracefully
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
p.terminate()
p2.terminate()
p.terminate()

