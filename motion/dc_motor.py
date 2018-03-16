import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(03,GPIO.OUT)
GPIO.setup(05,GPIO.OUT)
GPIO.setup(07,GPIO.OUT)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
pwm4=GPIO.PWM(07,100)
pwm5=GPIO.PWM(32,100)
pwm4.start(0)
pwm5.start(0)

'''                 #for forwad motion
GPIO.output(03,GPIO.HIGH)   
GPIO.output(05,GPIO.LOW)
pwm4.ChangeDutyCycle(25)
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
'''


GPIO.output(03,GPIO.LOW)
GPIO.output(05,GPIO.HIGH)
GPIO.output(24,GPIO.LOW)
GPIO.output(26,GPIO.HIGH)
pwm4.ChangeDutyCycle(20)
pwm5.ChangeDutyCycle(20)
GPIO.output(07,GPIO.HIGH)
GPIO.output(32,GPIO.HIGH)
time.sleep(2)
GPIO.output(07,GPIO.LOW)
GPIO.output(32,GPIO.LOW)
pwm4.stop()
pwm5.stop()
GPIO.cleanup()
