import pygame

def sound(p):
	pygame.mixer.init()
	pygame.mixer.music.load(p)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
		
	pygame.mixer.music.stop()
	pygame.mixer.stop()
	return;
	


