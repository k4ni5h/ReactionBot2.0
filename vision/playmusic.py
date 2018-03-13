import pygame
from time import sleep
#pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/ReactionBot2.0/song.mp3")
pygame.mixer.music.play(2)
#while pygame.mixer.music.get_busy():
#  pygame.time.Clock().tick(100)
sleep(20)
pygame.mixer.music.stop()
