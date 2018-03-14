import RPi.GPIO as GPIO
import time
import threading
from audio import sound  
############ SERVO MOTOR #############

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT)		# Face motor @ 21
pwm1=GPIO.PWM(21,125)		
GPIO.setup(22,GPIO.OUT)		# Eyelid motor @ 22
pwm2=GPIO.PWM(22,125)
GPIO.setup(23,GPIO.OUT)     #neck rotation motor @ 23
pwm3=GPIO.PWM(23,125)

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

GPIO.setup(03,GPIO.OUT)
GPIO.setup(05,GPIO.OUT)
GPIO.setup(07,GPIO.OUT)
GPIO.setup(08,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
     
def clockwise(pwm,p1,p2,duration):	# for clockwise pwm goes from 6 to 31 i.e. angle 0 to 180
	
	angle1=(p1-6.)*(36./5.)
	angle2=(p2-6.)*(36./5.)
	
	angle1=int(angle1)
	angle2=int(angle2)
	for i in range(1,1000):
        angle1=180
        new_angle=(angle2)-((i*(angle2-angle1))/1000.)
        p=(5./36.)*new_angle +6.
        pwm.ChangeDutyCycle(p)
        time.sleep(0.001)
	#for i in range(angle1,angle2):
	#	p=(5./36.)*i + 6
	#	print i
	#	print p
	#	pwm.ChangeDutyCycle(p)
	#	time.sleep(duration)
		
	#pwm.ChangeDutyCycle(p2)
	#time.sleep(1)
	pwm.ChangeDutyCycle(0)
	
	return;
	
def anticlockwise(pwm,p1,p2,duration):		# for anticlockwise pwm goes from 31 to 6 i.e. angle 180 to 0
	
	angle1=(p1-6.)*(36./5.)
	angle2=(p2-6.)*(36./5.)
	
	angle1=int(angle1)
	angle2=int(angle2)
	for i in range(1,1000):
        angle1=180
        new_angle=(angle2)+((i*angle1)/1000.)
        p=(5./36.)*new_angle +6.
        pwm.ChangeDutyCycle(p)
        time.sleep(0.001)
	
	#for i in range(angle1,angle2,-1):
	#	p=(5./36.)*i +6
	#	print i
	#	print p
	#	pwm.ChangeDutyCycle(p)
	#	time.sleep(duration)
		
	#pwm.ChangeDutyCycle(p2)
	#time.sleep(1)
	pwm.ChangeDutyCycle(0)
	
	return;
	
def initial():
	
	# initially both motor is kept at 90
	
	pwm1.start(19)
	pwm2.start(19)
	pwm3.start(19)
	#pwm1.ChangeDutyCycle(0)		# To off the motor at required position
	#pwm2.ChangeDutyCycle(0)
	
	return;
	
	
def happiness():
	
	initial_pos = 19  #initial position at 90
	final_pos = 24    #final position at 126
	
	t1=threading.Thread(target=anticlockwise,args=(pwm1,initial_pos,final_pos,mtr_time,))
	t2=threading.Thread(target=clockwise,args=(pwm2,initial_pos,initial_pos+3.5,mtr_time,))	# Eyelid happy emotion
    t1.start()
    t2.start()
    t1.join()
    t2.join()
	#time.sleep(0.05)
		# Face motor from 90 to 126 i.e. pwm 8 to pwm 5		
	
	#anticlockwise(pwm2,initial_pos,final_pos,mtr_time)	# Eyelid motor from 90 to 126 i.e. pwm 19 to pwm 24
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
	 	
def sadness():
	
	initial_pos = 19  #initial position at 90
	final_pos = 15    #final position at 62
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
	
def anger():
		
	initial_pos = 19   #initial position at 90
	final_pos = 24    #final position at 125
	
	anticlockwise(pwm1,initial_pos,final_pos,mtr_time)	# Face motor from 90 to 126 i.e. pwm 19 to pwm 24		
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
	anticlockwise(pwm2,19,22,mtr_time)  #initial position at 90 & final position at 111

	pwm2.ChangeDutyCycle(22)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	
	###### DC MOTOR MOTION REVERSE ####
	
	
	GPIO.output(03,GPIO.LOW)
	GPIO.output(05,GPIO.HIGH)
	GPIO.output(08,GPIO.LOW)
	GPIO.output(10,GPIO.HIGH)
	pwm.ChangeDutyCycle(25)

	GPIO.output(07,GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(07,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)

	
	sound("fear.mp3")             #sound
	time.sleep(t)
	
	clockwise(pwm2,7,8,mtr_time)
	
	####### DC MOTOR FORWARD #####
	GPIO.output(03,GPIO.HIGH)
	GPIO.output(08,GPIO.HIGH)
	GPIO.output(05,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	pwm.ChangeDutyCycle(25)
		
	GPIO.output(07,GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(07,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)

	
	
	neutral()
	neutral()
	return;
	
def disgust():
	
	anticlockwise(pwm1,19,24,mtr_time)
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
	pwm1.ChangeDutyCycle(19)
	time.sleep(1)
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(19)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(19)
	time.sleep(1)
	pwm3.ChangeDutyCycle(0)
	#anticlockwise(pwm2,8,6,mtr_time)
	#time.sleep(t)
	#clockwise(pwm2,6,8,mtr_time)
	# Blink start
	
	return;
	
def blink():
	
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(24)  #blink in range(90,125)
	#time.sleep(0.5)
	pwm2.ChangeDutyCycle(24)
	

	#pwm2.ChangeDutyCycle(0)
	
	neutral()
	
	return;
	
def sleep():
	
	initial_pos = 19 #initial position at 90
	final_pos = 17 #final position at 76
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
	
def yes():
	initial_pos = 19  #initial position at 90
	final_pos = 24    #final position at 126
	
	#anticlockwise(pwm2,initial_pos,final_pos,mtr_time)
	clockwise(pwm2,initial_pos,final_pos,mtr_time)	# face movement
	#time.sleep(0.05)
		# Face motor from 90 to 126 i.e. pwm 8 to pwm 5		
	
	#anticlockwise(pwm2,initial_pos,final_pos,mtr_time)	# Eyelid motor from 90 to 126 i.e. pwm 19 to pwm 24
	#pwm1.ChangeDutyCycle(final_pos)
	#time.sleep(1)
	#pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(final_pos)
	time.sleep(1)
	pwm2.ChangeDutyCycle(0)
	
def no():
		
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
	 	
	
