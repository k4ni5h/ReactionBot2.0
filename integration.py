import os

import sys

sys.path.insert(0, '/home/pi/Desktop/ReactionBot2.0/vision/')
from music import playmusic
from picture import clickcam
from emotionapi import getemotion

sys.path.insert(0, '/home/pi/Desktop/ReactionBot2.0/speech/')
from tone import main

sys.path.insert(0, '/home/pi/Desktop/ReactionBot2.0/motion/')
from combine2 import action_f

def cam():
	clickcam()
	emotion=getemotion()   
	print(emotion)
	if emotion!=99:
		action_f(emotion)
		playmusic(emotion)
	return

def speech():
	os.system('python /home/pi/Desktop/ReactionBot2.0/speech/spr')
	return

def rotate():
	os.system('python /home/pi/Desktop/ReactionBot2.0/speech/code2.py')
	return

def switch(x):
	if(x==0):
		cam()
	elif(x==1):
		speech()
	elif(x==2):
		rotate()

x=int(input())
switch(x)
print('kam ho gaya')
