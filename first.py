import sounddevice #pip install sounddevice

for i in range(30): #30 updates in 1 second
    rec = sounddevice.rec(44100/30)
    sounddevice.wait()
    print(rec.shape)