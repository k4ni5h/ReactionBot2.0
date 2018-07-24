import requests
import json
import numpy as np
def getemotion() :
    json_resp = requests.post( 'https://api-face.sightcorp.com/api/detect/',
              data  = { 'app_key' : 'e00f8c8746bf4b01b3f33b476cbf1e74' },
              files = { 'img'     : ( 'filename', open( '/home/pi/Desktop/ReactionBot2.0/visionandmusic/picam.jpg', 'rb' ) ) } )

    print (json_resp.text)
    apiresp =json.loads(json_resp.text)
    emotion=[0.0,0.0,0.0,0.0]
    for person in apiresp['people']:
        onlyemotion=(person['emotions'])
#for key,val in onlyemotion.items():
 #       exec(key + '=val')

#del onlyemotion["surprise"]
#del onlyemotion["disgust"]

    #print (onlyemotion)
        print(onlyemotion)
        emotion[0]=max(onlyemotion['happiness'],emotion[0])
        emotion[1]=max(onlyemotion['sadness'],emotion[1])
        emotion[2]=max(onlyemotion['anger'],emotion[2])
        emotion[3]=max(onlyemotion['fear'],emotion[3])
    print(emotion)
    if emotion==[0.0,0.0,0.0,0.0]:
		return(99)
    else:
		print(np.array(emotion).argmax())
		return np.array(emotion).argmax()


#if emotion == "happiness":

#print (max(onlyemotion.items(), key=operator.itemgetter(1))[0])
# emotionarray[0]=happiness
# emotionarray[1]=sadness
# emotionarray[2]=anger
# emotionarray[3]=fear
# maxval=emotionarray[0]
# for k in range(1,3) :
#     if maxval<emotionarray[k] :
#         maxval=emotionarray[k]
# for i in range(0,3) :
#     if maxval==emotionarray[i] :
#         break

# print(i)
