import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
pwm=GPIO.PWM(22,100)
pwm.start(0)
current_duty_cycle = 7.5
desired_duty_cycle = 5.0
steps = 10
duty_cycle_delta = (desired_duty_cycle - current_duty_cycle) / steps
while (current_duty_cycle != desired_duty_cycle):
    if (current_duty_cycle > desired_duty_cycle):
        duty_cycle_delta = -duty_cycle_delta
    current_duty_cycle = current_duty_cycle + duty_cycle_delta
    pwm.ChangeDutyCycle (current_duty_cycle)
time.sleep(1)
GPIO.cleanup()
    
          
    