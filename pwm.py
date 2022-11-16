import RPi.GPIO as GPIO 
from time import sleep


from gpiozero import zero 

LED = 16 #LED Output port
ultraSonicSensor = zero(trigger = 20, echo = 21, max_distance = 1.0)

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)


pwm = GPIO.PWM(LED, 30) 
pwm.start(0) 


try:
    while True: 
        sleep(1)         
        objDistanceCM = ultraSonicSensor.distance * 100 
        print("Distance (CM): %.2f" % objDistanceCM) 
        pwm.ChangeDutyCycle(100 - round(objDistanceCM, 0)) 
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
