

import RPi.GPIO as GPIO
import time
from audio import sound  
############ SERVO MOTOR #############

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT)		# Face motor @ 21
pwm1=GPIO.PWM(21,50)		
GPIO.setup(22,GPIO.OUT)		# Eyelid motor @ 22
pwm2=GPIO.PWM(22,50)

mtr_time=0.001				# motor time
t=3							# sleep time
	
############# LED ##############

red=31
blue=32
green=33

GPIO.setup(red, GPIO.OUT)	
GPIO.setup(blue, GPIO.OUT)	
GPIO.setup(green, GPIO.OUT)	

############# DC MOTOR ##########

GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
     
def clockwise(pwm,p1,p2,duration):	# for clockwise pwm goes from 0 to 120 i.e. angle 0 to 180
	
	angle1=(p1-2.)*(18.)
	angle2=(p2-2.)*(18.)
	
	angle1=int(angle1)
	angle2=int(angle2)
	
	for i in range(angle1,angle2):
		p=(1./18.)*i + 2
		print i
		print p
		pwm.ChangeDutyCycle(p)
		time.sleep(duration)
		
	#pwm.ChangeDutyCycle(p2)
	#time.sleep(1)
	pwm.ChangeDutyCycle(0)
	
	return;
	
def anticlockwise(pwm,p1,p2,duration):		# for anticlockwise pwm goes from 12 to 0 i.e. angle 180 to 0
	
	angle1=(p1-2.)*(18.)
	angle2=(p2-2.)*(18.)
	
	angle1=int(angle1)
	angle2=int(angle2)
	
	for i in range(angle1,angle2,-1):
		p=(1./18.)*i +2
		print i
		print p
		pwm.ChangeDutyCycle(p)
		time.sleep(duration)
		
	#pwm.ChangeDutyCycle(p2)
	#time.sleep(1)
	pwm.ChangeDutyCycle(0)
	
	return;
	
def initial():
	
	# initially both motor is kept at 90
	
	pwm1.start(8)
	pwm2.start(8)
	
	#pwm1.ChangeDutyCycle(0)		# To off the motor at required position
	#pwm2.ChangeDutyCycle(0)
	
	return;
	
	
def happy():
	
	initial_pos = 8
	final_pos = 6
	
	anticlockwise(pwm1,initial_pos,final_pos,mtr_time)
	clockwise(pwm2,initial_pos,initial_pos+3.5,mtr_time)	# Eyelid happy emotion
	#time.sleep(0.05)
		# Face motor from 90 to 126 i.e. pwm 8 to pwm 5		
	
	#anticlockwise(pwm2,initial_pos,final_pos,mtr_time)	# Eyelid motor from 90 to 126 i.e. pwm 8 to pwm 5
	pwm1.ChangeDutyCycle(final_pos)
	time.sleep(1)
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(initial_pos+3.5)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)


	GPIO.output(green,GPIO.HIGH)	# Green LED glows
	#sound("test.wav")
	sound("happy.mp3")             #sound
	time.sleep(t)
	GPIO.output(green,GPIO.LOW)		# Green LED OFF
	
	clockwise(pwm1,final_pos,initial_pos,mtr_time)
	anticlockwise(pwm2,initial_pos+3.5,initial_pos,mtr_time)
		# Return to initial
	
	
	neutral()
	neutral()
	
	

	return;
	 	
def sad():
	
	initial_pos = 8
	final_pos = 9
	clockwise(pwm1,initial_pos,final_pos,mtr_time)	
	anticlockwise(pwm2,initial_pos,initial_pos-3,mtr_time)
	#clockwise(pwm2,final_pos,final_pos+1,mtr_time)	# Eyelid sad emotion
	
	pwm1.ChangeDutyCycle(final_pos)
	time.sleep(1)
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(initial_pos-3)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	sound("sad.mp3")            #sound
	time.sleep(t)
	
	anticlockwise(pwm1,final_pos,initial_pos,mtr_time)
	clockwise(pwm2,initial_pos-3,initial_pos,mtr_time)
	
	neutral()
	neutral()
	return;
	
def angry():
		
	initial_pos = 8
	final_pos = 6
	
	anticlockwise(pwm1,initial_pos,final_pos,mtr_time)	# Face motor from 90 to 126 i.e. pwm 8 to pwm 5		
	clockwise(pwm2,initial_pos,initial_pos+2,mtr_time)	# Eyelid motor from 90 to 126 i.e. pwm 8 to pwm 5
	#anticlockwise(pwm2,final_pos,final_pos-1,mtr_time)	# Eyelid happy emotion

	pwm1.ChangeDutyCycle(final_pos)
	time.sleep(1)
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(initial_pos+2)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	

	GPIO.output(red,GPIO.HIGH)	# Red LED glows
	sound("angry.mp3")                 #sound
	time.sleep(t)
	GPIO.output(red,GPIO.LOW)		# Red LED OFF
	
	clockwise(pwm1,final_pos,initial_pos,mtr_time)	# Return to initial
	anticlockwise(pwm2,initial_pos+2,initial_pos+1,mtr_time)
	neutral()
	neutral()
	
	return;
	
def fear():
	
	pwm1.ChangeDutyCycle(0)
	anticlockwise(pwm2,8,7,mtr_time)
	
	pwm2.ChangeDutyCycle(7)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	
	###### DC MOTOR MOTION REVERSE ####
	
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)
	
	sound("fear.mp3")             #sound
	time.sleep(t)
	
	clockwise(pwm2,7,8,mtr_time)
	
	####### DC MOTOR FORWARD #####
	
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(11,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
	
	neutral()
	neutral()
	return;
	
def disgust():
	
	anticlockwise(pwm1,8,6,mtr_time)
	pwm2.ChangeDutyCycle(0)
	time.sleep(1)
	pwm1.ChangeDutyCycle(5)
	time.sleep(0.5)
	pwm1.ChangeDutyCycle(0)
	
	time.sleep(2)
	
	anticlockwise(pwm2,8,5,mtr_time)
	clockwise(pwm1,6,9,mtr_time)
	
	pwm1.ChangeDutyCycle(9)
	time.sleep(1)
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(5)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	
	

	time.sleep(t)
	
	anticlockwise(pwm1,9,8,mtr_time)
	clockwise(pwm2,6,8,mtr_time)
	

	neutral()
	neutral()
	neutral()
	return;
	
def neutral():
	
	# Blink stop
	pwm1.ChangeDutyCycle(8)
	time.sleep(1)
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(8)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	
	#anticlockwise(pwm2,8,6,mtr_time)
	#time.sleep(t)
	#clockwise(pwm2,6,8,mtr_time)
	# Blink start
	
	return;
	
def blink():
	
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(6)
	#time.sleep(0.5)
	pwm2.ChangeDutyCycle(6)
	

	#pwm2.ChangeDutyCycle(0)
	
	neutral()
	
	return;
	
def sleep():
	
	initial_pos = 8
	final_pos = 9
	clockwise(pwm1,initial_pos,final_pos,mtr_time)	
	anticlockwise(pwm2,initial_pos,initial_pos-3,mtr_time)
	#clockwise(pwm2,final_pos,final_pos+1,mtr_time)	# Eyelid sleep emotion
	sound("bye.mp3")                                                  #sound
	GPIO.output(blue,GPIO.LOW)
	time.sleep(t)
	
	return;
	
def nothing():
	
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	
def servo(x):
	
	
	initial()
	#time.sleep(1)
	GPIO.output(blue,GPIO.HIGH)
	if(x==0):
		print " angry "
		angry()
		
	elif(x==1):
		print " happy "
		happy()
		
	elif(x==3):
		print "sad"
		sad()
	
	elif(x==2):
		print " fear "
		fear()
	
	elif(x==4):
		print " disgust "
		disgust()
	
	elif(x==5):
		print " neutral "
		neutral()
		
	elif(x==6):
		print "blink"
		blink()
		
	elif(x==7):
		print "sleep"
		sleep()
		
	elif(x==8):
		print "nothing"
		nothing()
		
	else:
		blink()
	
	return;
	 	
	
