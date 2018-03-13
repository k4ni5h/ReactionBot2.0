import RPi.GPIO as GPIO                                ## Import GPIO Library.
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
pwm=GPIO.PWM(22,1000)
pwm.start(5)
angle=10
duty=float(angle)/18+2
ck=0
while ck<=5:
    pwm.ChangeDutyCycle(duty)
    ck=ck+1
time.sleep(1)
GPIO.cleanup()
