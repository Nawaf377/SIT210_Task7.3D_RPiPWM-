import RPi.GPIO as GPIO
import time

# USE GPIO NUMBERS NOT PIN NUMBERS
GPIO.setmode(GPIO.BCM)

# PIN DEFINITION
Led = 18
Triger = 23
Echo = 24


GPIO.setup(Triger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.setup(Led, GPIO.OUT)

# FUNCTIONS
pwm = GPIO.PWM(Led, 100)
pwm.start(0)

def dits():
    GPIO.output(Triger, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(Triger, GPIO.LOW)
    while GPIO.input(Echo) == 0:
        P_start = time.time()
    while GPIO.input(Echo) == 1:
        P_end = time.time()
        
    dits = ((P_end - P_start) * 34300) / 2
    
    return dits
        
    

try:
    while 1:
        dis = dits()*3
        
        if dis < 0:
            dis = 0
        if dis > 100:
            dis = 100
        pwm.ChangeDutyCycle(100 - dis)
        time.sleep(0.0001)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    




