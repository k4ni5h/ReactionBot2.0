import RPi.GPIO as GPIO
import time

#11 - in2 , 12 -in1 , 13 - in3 , 15 - in4 

def dcmotor(m):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)


	motion = m;

	if (m == "forward"):
	
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(11,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(11,GPIO.LOW)

		a =  "MOVING " + m.upper();
	
	
	
	elif (m == "reverse"):
	
		GPIO.output(12,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(12,GPIO.LOW)

		a =  "MOVING " + m.upper();
	
	

	elif (m == "left"):
	
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(12,GPIO.HIGH)
		time.sleep(0.4)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(12,GPIO.LOW)

		a =  "MOVING " + m.upper();
	
	

	elif (m == "right"):
		
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		time.sleep(0.4)
		GPIO.output(11,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
	
		a =  "MOVING " + m.upper();
	
	else:

		a =  "I can't dance! :("
	
		
	
	return a;
