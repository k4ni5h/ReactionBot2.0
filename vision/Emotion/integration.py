from music import playmusic
from picture import clickcam
from emotionapi import getemotion

action=0
if action==0  :
    clickcam()
emotion=getemotion()   
print(emotion)
playmusic(emotion) 
action=1
