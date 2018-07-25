def neckrotation ():
    angle1=(p1-6)*(36./5.)
    angle2=(p2-6)*(36./5.)
    
    angle1=int(angle1)
    angle2=int(angle2)
    
    if(angle2>angle1):
		
        for i in range(angle1,angle2):
            p=(5./36.)* i +6.
            pwm.ChangeDutyCycle(p)
            time.sleep(duration)
        pwm.ChangeDutyCycle(0)
    elif(angle1>angle2):
        for i in range(angle1,angle,-1):
			p=(5./36.)*i + 6.
			pwm.ChangeDutyCycle(p)
			time.sleep(duration)
		pwm.ChangeDutyCycle(0)
	else:
		pwm.ChangeDutyCycle(0)

		return;	
