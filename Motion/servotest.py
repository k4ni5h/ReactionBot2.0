import RPi.GPIO as GPIO                                ## Import GPIO Library.
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
pwm=GPIO.PWM(22,100)
pwm.start(5)
angle1=10
duty1=(float(angle1)/18)+2
angle2=160
duty2=(float(angle2)/18)+2
ck=0
while ck<=5:
    pwm.ChangeDutyCycle(duty1)
    time.sleep(1.8)
    pwm.ChangeDutyCycle(duty2)
    time.sleep(0.8)
    ck=ck+1
time.sleep(1)
GPIO.cleanup()
