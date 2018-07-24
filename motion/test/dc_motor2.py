import RPi.GPIO as GPIO
import time

#11 - in2 , 12 -in1 , 13 - in3 , 15 - in4 

def dcmotor(m):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(03,GPIO.OUT)
	GPIO.setup(05,GPIO.OUT)
	GPIO.setup(07,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(10,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)


	motion = m;

	if (m == "forward"):
	
		GPIO.output(03,GPIO.HIGH)
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(05,GPIO.LOW)
		GPIO.output(10,GPIO.LOW)
		pwm.ChangeDutyCycle(25)
		
		GPIO.output(07,GPIO.HIGH)
		GPIO.output(12,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(07,GPIO.LOW)
		GPIO.output(12,GPIO.LOW)

		#a =  "MOVING " + m.upper();
	
	
	
	elif (m == "reverse"):
	
	    
		GPIO.output(03,GPIO.LOW)
		GPIO.output(05,GPIO.HIGH)
		GPIO.output(11,GPIO.LOW)
		GPIO.output(10,GPIO.HIGH)
		pwm.ChangeDutyCycle(25)

		GPIO.output(07,GPIO.HIGH)
		GPIO.output(12,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(07,GPIO.LOW)
		GPIO.output(12,GPIO.LOW)


		# a =  "MOVING " + m.upper();
	
	

	elif (m == "left"):
	
		GPIO.output(03,GPIO.LOW)
		GPIO.output(05,GPIO.LOW)
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(10,GPIO.LOW)
        pwm.ChangeDutyCycle(25)
        GPIO.output(07,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(07,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
     elif (m == "right"):
		
		GPIO.output(03,GPIO.HIGH)
		GPIO.output(05,GPIO.LOW)
		
		GPIO.output(11,GPIO.LOW)
		GPIO.output(10,GPIO.LOW)
		pwm.ChangeDutyCycle(25)
		GPIO.output(07,GPIO.HIGH)
		GPIO.output(12,GPIO.HIGH)
		
		time.sleep(2)
		GPIO.output(07,GPIO.LOW)
		GPIO.output(12,GPIO.LOW)
	
		a =  "MOVING " + m.upper();
	
	else:

		a =  "I can't dance! :("
	
		
	
	return a;
dcmotor("forward")
