import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
pwm=GPIO.PWM(22,50)
pwm.start(0)
servo_current_angle=0
servo_desired_angle=45
if servo_current_angle > servo_desired_angle :
    while(x) :
             servo_current_angle -=1 
             duty_cycle = (((12.5-2.5)/(180-0) * servo_current_angle) +2.5)
             pwm.ChangeDutyCycle (duty_cycle)
             time.sleep(0.01)
             if servo_current_angle = servo_desired_angle :
                 x = 0 
elif servo_current_angle < servo_desired_angle :
      while(x) :
             servo_current_angle +=1 
             duty_cycle = (((12.5-2.5)/(180-0) * servo_current_angle) +2.5) 
             pwm.ChangeDutyCycle (duty_cycle)
             time.sleep(0.01)
             if servo_current_angle = servo_desired_angle :
                 x = 0
 time.sleep(1)
 GPIO.cleanup()                          