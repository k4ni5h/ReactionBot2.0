import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()

import requests
import json
import numpy as np
import sys

sys.path.insert(0, '/home/pi/Desktop/ReactionBot2.0/motion/')
from combine2 import action_f

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
    data = json.loads(str(data))
    print([data['document_tone']['tone_categories'][0]['tones'][i]['tone_name'] for i in range(5)])
    print([data['document_tone']['tone_categories'][0]['tones'][i]['score'] for i in range(5)])
    print([data['document_tone']['tone_categories'][1]['tones'][i]['tone_name'] for i in range(3)])
    print([data['document_tone']['tone_categories'][1]['tones'][i]['score'] for i in range(3)])
    print([data['document_tone']['tone_categories'][2]['tones'][i]['tone_name'] for i in range(5)])
    print([data['document_tone']['tone_categories'][2]['tones'][i]['score'] for i in range(5)])
    emotion=[0.0,0.0,0.0,0.0]
    emotion[0]=max(data['document_tone']['tone_categories'][0]['tones'][3]['score'],data['document_tone']['tone_categories'][2]['tones'][3]['score'])
    emotion[1]=data['document_tone']['tone_categories'][0]['tones'][4]['score']
    emotion[2]=max(data['document_tone']['tone_categories'][0]['tones'][0]['score'],data['document_tone']['tone_categories'][0]['tones'][1]['score'])
    emotion[3]=data['document_tone']['tone_categories'][0]['tones'][2]['score']
    print(np.array(emotion).argmax())
    action_f(np.array(emotion).argmax())
    print('emotion dekh')

def recog(mdata):	
	if mdata == 'exit'.lower():
		exit
	results = analyze_tone(mdata)
	if results != False:
		display_results(results)
		exit
	else:
		print("Something went wrong")

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
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                recog(str(value))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
                recog(str(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
