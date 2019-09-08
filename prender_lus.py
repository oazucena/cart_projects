import RPi.GPIO as GPIO
import time as T

GPIO.setmode(GPIO.BOARD)
mypin = 5
GPIO.setup(mypin, GPIO.OUT)

while True:
    print("Turn on or off")
    on = str(raw_input("Turn on? [Y/N]")).lower().strip()
    if on[0] == 'y':
        GPIO.output(mypin, True)
    else:
        GPIO.output(mypin, False)
    
