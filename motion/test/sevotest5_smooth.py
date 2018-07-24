import RPi.GPIO as GPIO
import time
#GPIO.setwarning(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.OUT)
pwm=GPIO.PWM(23,125)
pwm.start(21)
angle1=180

for i in range(1,1000):
    angle1=180
    new_angle=(i*angle1)/1000.
    p=(5./36.)*new_angle +6.
    pwm.ChangeDutyCycle(p)
    time.sleep(0.004)
    #pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(8)
time.sleep(1)
for i in range(1000,1,-1):
    angle1=180
    new_angle=(i*angle1)/1000.
    p=(5./36.)*new_angle +6.
    pwm.ChangeDutyCycle(p)
    time.sleep(0.004)
#for i in range(angle1,angle2,-1):
 #   p=(5./36.)*i +6.
  #  pwm.ChangeDutyCycle(p)
   # time.sleep(0.001)
    #pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(0)
time.sleep(1)
GPIO.cleanup()
