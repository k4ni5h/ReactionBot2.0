import pygame
from time import sleep
#pygame.init()
#def playsong
 #   if finalemotion==happiness
k=1
pygame.mixer.init()
pygame.mixer.music.load("/home/anant/Desktop/ReactionBot2.0/Songs/Happiness/"+str(k)+".mp3")
pygame.mixer.music.play(2)
#while pygame.mixer.music.get_busy():
#  pygame.time.Clock().tick(100)
sleep(20)
pygame.mixer.music.stop()


