import RPi.GPIO as GPIO
import time
import argparse

#GPIO.setwarning(Fal
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
pwm3=GPIO.PWM(23,125)
pwm3.start(19)

def initial():
	print("initial")
	# initially both motor is kept at 90
	
	pwm3.start(19)
	#pwm2.start(19)
	#pwm3.start(19)
	#pwm1.ChangeDutyCycle(0)		# To off the motor at required position
	#pwm2.ChangeDutyCycle(0)
	return;
def neutral():
	print("Neutral")
	# Blink stop
	pwm3.ChangeDutyCycle(19)
	time.sleep(1)
	pwm3.ChangeDutyCycle(0)
	return;	
def neckrotation (angle1):
    #angle1=(p1-6)*(36./5.)
    #angle2=(p2-6)*(36./5.)
    angle2=90
    angle1=int(angle1)
    angle2=int(angle2)
    
    if(angle2>angle1):
	   	for i in range(1,1000):
			new_angle=(angle2)-((i*(angle2-angle1))/1000.)
			p=(5./36.)*new_angle +6.
			pwm3.ChangeDutyCycle(p)
			time.sleep(0.001)
		pwm3.ChangeDutyCycle(0)
    elif(angle1>angle2):
        for i in range(1,1000):
			new_angle=(angle2)+((i*angle1)/1000.)
			p=(5./36.)*new_angle +6.
			pwm3.ChangeDutyCycle(p)
			#p=(5./36.)*i + 6.
			time.sleep(0.001)
        pwm3.ChangeDutyCycle(0)
    else:
        pwm3.ChangeDutyCycle(0)
    return;

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
angle=int(args.echo)
neckrotation(angle)		
time.sleep(2)
neutral()			
time.sleep(1)
GPIO.cleanup()
