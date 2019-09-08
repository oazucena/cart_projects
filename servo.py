import RPi.GPIO as OG
import numpy as np
import time as t
import random as ran
import ultrasonic as U
OG.setmode(OG.BOARD)



class Servo:
    def __init__(self,pin, start):
        self.debug = False
        self.p = pin
        OG.setup(pin, OG.OUT)
        self.f = 100
        self.pwm = OG.PWM(pin, self.f)
        self.current = 0
        self.pwm.start(0)
        self.min = .000350
        self.max = .002400
        self.max_d = 1.0/(self.f*self.min)
        self.min_d = 1.0/(self.f*self.max)
        self.start = start
        self.__change_duty_cycle(self.start)

    def __change_duty_cycle(self, to):
        delta = self.min_d + (self.max_d-self.min_d)*to/100.0
        self.current = to
        self.pwm.ChangeDutyCycle(delta)
        # for i in range(0,sign*delta):
        #     self.current += sign
        #     self.pwm.ChangeDutyCycle(self.current)
        if self.debug:
            print("Current PWM %d" % (self.current))
        
    def setDutyCycle(self, pwm):
        self.__change_duty_cycle(pwm)

    def stop(self):
        self.pwm.stop()                # stop the PWM output  
        OG.cleanup()

if __name__ == '__main__':
    echo = 31
    trigger = 29
    servo = Servo(12, 39)
    filter_window = 10
    ul = U.Ultrasonic(echo, trigger, None, filter_window=filter_window)
    #warm up ultra
    distance = ul.getDistance()
    wait = 1
    try:
        while True:
            print("------------------")
            servo.setDutyCycle(servo.start)
            t.sleep(wait)
            servo.setDutyCycle(100)
            t.sleep(wait)
            servo.setDutyCycle(0)
            t.sleep(wait)
            for i in range(100):
                val = ran.randint(0,100)
                servo.setDutyCycle(i)
                t.sleep(0.05)
                for c in range(filter_window):
                    distance = ul.getDistance()
                print("%d,%f" % (i,distance))
    except KeyboardInterrupt:
        servo.stop()
        print("Ending")