
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(03,GPIO.OUT)
GPIO.setup(05,GPIO.OUT)
GPIO.setup(07,GPIO.OUT)

pwm=GPIO.PWM(07,100)
pwm.start(0)                 #for forwad motion
GPIO.output(03,GPIO.HIGH)   
GPIO.output(05,GPIO.LOW)
pwm.ChangeDutyCycle(25)
GPIO.output(07,GPIO.HIGH)
time.sleep(2)
GPIO.output(07,GPIO.LOW)
                            #FOR REVERSE MOTION
GPIO.output(03,GPIO.LOW)
GPIO.output(05,GPIO.HIGH)
pwm.ChangeDutyCycle(25)
GPIO.output(07,GPIO.HIGH)
time.sleep(2)
GPIO.output(07,GPIO.LOW)
pwm.stop()
GPIO.cleanup()
    
