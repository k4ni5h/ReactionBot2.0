#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import random
from subprocess import Popen
k=random.randint(1,3)
print(k)
def playmusic(finalemotion) :
    if finalemotion==0 :
        movie_path = '/home/pi/Desktop/ReactionBot2.0/songs/happiness/'+str(k)+'.mp3'
        omxp = Popen(['omxplayer',movie_path])
        time.sleep(5)
        omxp.kill()
    elif finalemotion==1  :
        movie_path = '/home/pi/Desktop/ReactionBot2.0/songs/sadness/'+str(k)+'.mp3'
        omxp = Popen(['omxplayer',movie_path])
        time.sleep(5)
        omxp.kill()
    else finalemotion==3  :
	    movie_path = '/home/pi/Desktop/ReactionBot2.0/songs/fear/1.mp3'
	    omxp = Popen(['omxplayer',movie_path])
	    time.sleep(5)
	    omxp.kill()
    command1 = "sudo killall -s 9 omxplayer.bin"
    os.system(command1)
    return
