import RPi.GPIO as GPIO
import time

LED = 19
LS = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.IN)

#set GPIO Pins
GPIO_TRIGGER = 20
GPIO_ECHO = 6
  
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
   
def distance():
# set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
                
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
                             
    StartTime = time.time()
    StopTime = time.time()
                                      
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
                                                           
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

while True:
    dist = distance()
    if dist < 10:
        GPIO.output(LED,True)
    else:
        GPIO.output(LED,False)
