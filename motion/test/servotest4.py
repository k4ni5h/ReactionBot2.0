import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
pwm=GPIO.PWM(22,125)
pwm.start(19)
angle1=180
angle2=90
for i in range(angle2,angle1):
    p=(5./36.)*i +6.
    pwm.ChangeDutyCycle(p)
    time.sleep(0.001)
    #pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(8)
time.sleep(1)

for i in range(angle1,angle2,-1):
    p=(5./36.)*i +6.
    pwm.ChangeDutyCycle(p)
    time.sleep(0.001)
    #pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(0)
time.sleep(1)
GPIO.cleanup()
 
