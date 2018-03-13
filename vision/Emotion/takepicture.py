import os
import time
a=1
while(a) :
    os.system("raspistill -w 480 -h 320 -q 100 -o picam.jpg")
    time.sleep(1)
    import requests
    import json
    json_resp = requests.post( 'https://api-face.sightcorp.com/api/detect/',
              data  = { 'app_key' : '48855f9ed48942d8bfeedbb3ff515e10' },
              files = { 'img'     : ( 'filename', open( '/home/pi/Desktop/ReactionBot2.0/Emotion/picam.jpg', 'rb' ) ) } )
    print(json_resp.text)
    apiresp =json.loads(json_resp.text)
    for person in apiresp['people']:
        onlyemotion=(person['emotions'])
    #print(onlyemotion)
    #del onlyemotion["surprise"]
    #del onlyemotion["disgust"]

    print (onlyemotion)

    finalemotion = max(onlyemotion, key=lambda i: onlyemotion[i])
    print (finalemotion)
