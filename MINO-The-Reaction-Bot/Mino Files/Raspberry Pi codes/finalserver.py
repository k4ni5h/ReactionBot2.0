

from bottle import run, route, request                #for bottle server 
from multiprocessing import Process                   #for multi threading of programs
import sys
import thread
import RPi.GPIO as GPIO
import time


import json
from watson_developer_cloud import AlchemyLanguageV1

from testAL import alchemyL         #file name of the file containing Alchemy function
from dc_motor import dcmotor        #file for dc motor 
from funservo1 import servo          #file for servo
from audio import sound              #file for sound

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
blue = 32
GPIO.setup(blue, GPIO.OUT)


@route('/querytest')
def querytest():
	
	param1 = request.query.param1
	                        
	test = 0
	
	pro = 0
	a = "Sorry I couldn't get you! :("
	p = param1                          # input text
	emot = 6                               # 6 and others = blink , 5 = neutral , 4 = disgusted , 3 = sad , 2 = scared , 1 = happy , 0 = angry
	#servo(emot)                               # 7 = sleep



	try:
		t = float(p);
	except Exception:
		test = 1;
		


	p = p.lower();
	parray = p.split();
	
	#print p + '*'
	
	if (test == 0):

		emot = 1;
		#servo(emot)

		if(len(p) == 10):

			print "Thanks! I'll call you at night!"               #for fun
			a = "Thanks! I'll call you at night!"

		else:

			print 'I would rather have your phone number! :)'            #for fun
			a = 'I would rather have your phone number! :)'
	
	else:
		
		parray = p.split();

			
		try:
			if(parray[0] == 'motion'):
				#a = dcmotor(parray[1])
				print parray[1].upper();
				a = "MOVING " + parray[1].upper()
				#servo(6) 
				
		
			else:
				try:

					if(p == "sleep" or p == "bye" or p == "off" or p == "good night"):

						a = "Good Byee!"
						emot = 7
						#servo(emot)
						
					elif(p == "hi" or p == "hi mino" or p == "hello" or p == "hello mino" or p == "hey" or p == "hii" or p == "namaste" or p == "heya"):
						
						a = "Hi! I am Mino! Lets talk!"
						emot = 1 
						
					elif(p == "blink"):
						
						
						a = "blinking"
						emot = 6
						
					elif( p == "play songs" or p == "play music" or p == "play song"):
						
						a = "Playing Faded by Alan Walker"
						emot = 6
						
					elif( p == "stop songs" or p == "stop music" or p == "stop song"):
						
						a = "Stopping music"
						emot = 6	
					
					elif( p == "switch 1 on" or p == "switch one on" or p=="on switch one"  or p == "on switch1" or p == "switch1 on" or p == "on switch 1"):
						
						a = "Switching on switch 1"
						emot=8
						sound("oka oka.mp3")                      #sound
						
					elif( p == "switch 2 on" or p == "switch two on" or p=="on switch two" or p == "switch to on" or p=="on switch to" or p == "on switch2" or p == "switch2 on" or p == "on switch 2"):
						
						a = "Switching on switch 2"
						emot=8
						sound("oka oka.mp3")                             #sound
		 			
		 			elif( p == "switch 3 on" or p == "switch three on" or p=="on switch three" or p == "on switch3" or p == "switch3 on" or p == "on switch 3" ):
						
						a = "Switching on switch 3"
						emot=8
						sound("oka oka.mp3")                  #sound
					
					elif( p == "switch 1 off" or p == "switch one off" or p=="off switch one" or p == "off switch1" or p == "switch1 off" or p == "off switch 1" or p == "switch 1 of" or p == "switch one of" or p=="of switch one" or p == "of switch1" or p == "switch1 of" or p == "of switch 1"):
						
						a = "Switching off switch 1"
						emot=8
						sound("oka oka.mp3")                      #sound
						
					elif(p == "switch 2 of" or p == "switch two of" or p=="of switch two" or p == "switch to of" or p=="of switch to" or p == "of switch2" or p == "switch2 of" or p == "of switch 2" or p == "switch 2 off" or p == "switch two off" or p=="off switch two" or p == "switch to off" or p=="off switch to" or p == "off switch2" or p == "switch2 off" or p == "off switch 2"):
						
						a = "Switching off switch 2"
						emot=8
						sound("oka oka.mp3")                       #sound
		 			
		 			elif( p == "switch 3 off" or p == "switch three off" or p=="off switch three" or p == "off switch3" or p == "switch3 off" or p == "off switch 3" or p == "switch 3 of" or p == "switch three of" or p=="of switch three" or p == "of switch3" or p == "switch3 of" or p == "of switch 3"  ):
						
						a = "Switching off switch 3"
						emot=8
						sound("oka oka.mp3")             #sound
			
					else:
						a,emot = alchemyL(p);
						#servo(emot)

				except Exception :
					emot = 1
					#servo(emot)
					
					print 'I am unaware of this language, I\'ll be happy to learn it from you'
					a = 'I am unaware of this language, I\'ll be happy to learn it from you'
		except Exception:
			emot = 5
			#servo(emot)
			print 'I am Neutral'
			
			a = 'I am Neutral'
			
			
	def z1(x):
		
		print emot 
		
		if(parray[0] == 'motion'):
			
				
			try:
				a = dcmotor(parray[1])
				servo(emot)
					
			except Exception:	
				a = "My joints are jammed :("
				
		else:
			
			try:
				servo(emot)
				
			except Exception:
				a = "I think I have a neck pain :("
				
		
		
		#sound("test.wav")
		return;
	
	def z2(y):
		
		
		try:
			
			
			if( p == "play songs" or p == "play music" or p == "play song"):
				sound("oka oka.mp3")                      #sound
				sound("Alan Walker - Faded.mp3")
			
			elif(p == "stop music" or p == "stop song" or p=="stop song"):
				sound("oka oka.mp3")                         #sound
				
			else:
				print emot
				
		except Exception:
			
			a = "Error playing song :("
			servo(3)
			print "error" 
		
		return;
		

	try:
		
		thread.start_new_thread( z1 ,(5,))
		thread.start_new_thread( z2 ,("z2",))
			
	except:
   		print "Error: unable to start thread"
   		a = "I think I have a neck pain :("

   	return a;

	while 1:
   		pass

	
	


	
if (__name__ == '__main__' ):
	
	GPIO.output(blue,GPIO.HIGH)                          	# Blue LED glows
	run(host='0.0.0.0', port=8080)
	GPIO.output(blue,GPIO.LOW)
