import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
pwm=GPIO.PWM(22,125)
pwm.start(10)
servo_current_angle=28
servo_desired_angle=120
if servo_current_angle > servo_desired_angle :
    while(x) :
    servo_current_angle =servo_current_angle-1
    duty_cycle = (((5./36.) * servo_current_angle) +6)
    pwm.ChangeDutyCycle (duty_cycle)
    time.sleep(0.01)
    if servo_current_angle == servo_desired_angle :
        x = 0 
elif servo_current_angle < servo_desired_angle :
      while(x) :
      servo_current_angle =servo_current_angle+1
      duty_cycle = (((5./36.) * servo_current_angle) +6) 
      pwm.ChangeDutyCycle (duty_cycle)
      time.sleep(0.01)
      if servo_current_angle == servo_desired_angle :
          x = 0
time.sleep(1)
GPIO.cleanup()                          
