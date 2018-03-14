#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
 
# Record Audio
while(True):
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        print("Say something!")
        audio = r.listen(source)
    print(1)
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
