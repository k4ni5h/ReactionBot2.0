import speech_recognition as sr

import requests
import json

def analyze_tone(text):
    username = '926325e3-3eea-4494-86c0-c03d1a9deefe'
    password = 'CuExNGBJgChT'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-2'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username,password), headers = headers,
         data=data)
        return r.text
    except:
        return False

def display_results(data):
    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        results = analyze_tone(data)
        if results != False:
            results = json.loads(str(results))
            return results['document_tone']['tone_categories']
        else:
            return "Something went wrong"

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You say {}".format(value).encode("utf-8"))
                print(display_results(format(value).encode("utf-8")))
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You say {}".format(value))
                print(display_results(format(value)))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
