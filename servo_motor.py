#import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
servo=18
freq=50
GPIO.setup(servo,GPIO.OUT)
p = GPIO.PWM(servo,freq)
dc = 0
p.start(dc)
directions=[5,8]
direction=0
try:
    while True:
        p.ChangeDutyCycle(directions[direction])
        time.sleep(2)
        print("dc: {}".format(directions[direction]))
        direction=direction+1
        direction=direction%2
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
