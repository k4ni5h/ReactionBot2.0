import os
def action_f(x):
	if(x==0):
		os.system("python /home/pi/Desktop/ReactionBot2.0/motion/happy.py & python /home/pi/Desktop/ReactionBot2.0/motion/happy1.py & ")
	elif(x==1):
		os.system("python /home/pi/Desktop/ReactionBot2.0/motion/sad.py & python /home/pi/Desktop/ReactionBot2.0/motion/sad1.py & ")
	elif(x==2):
		os.system("python /home/pi/Desktop/ReactionBot2.0/motion/angry.py & python /home/pi/Desktop/ReactionBot2.0/motion/angry1.py & ")
	elif(x==3):
		os.system("python /home/pi/Desktop/ReactionBot2.0/motion/fear.py & python /home/pi/Desktop/ReactionBot2.0/motion/fear1.py & ")
	return;
#i=int(input())
#emotion(i)
