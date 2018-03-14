import RPi.GPIO as GPIO
import time
#GPIO.setwarning(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
#pwm1=GPIO.PWM(23,125)
#pwm1.start(6)
pwm2=GPIO.PWM(23,125)
pwm2.start(6)
#pwm3=GPIO.PWM(23,125)
#pwm3.start(16)

time.sleep(1)
GPIO.cleanup()
