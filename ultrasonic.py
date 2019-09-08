
import threading
import random
import time
import RPi.GPIO as OG
import collections as col
import statistics
import filters as fil

OG.setmode(OG.BOARD)
echo = 31
trigger = 29
PERIOD = 0.00002
WAIT = 0.0183
SPEED_OF_SOUND = 34300


class Ultrasonic:
    def __init__(self, echo, trigger, queue, filter_window = 5):
        self.e = echo
        self.t = trigger
        self.distance = 0
        OG.setup(echo, OG.IN)
        OG.setup(trigger, OG.OUT)
        self.q = queue
        self.filter = fil.MedianFilter(filter_window)
        self.active = False
    
    def getDistance(self):
        if self.q == None:
            self.__getDistance()
            return self.distance
        if not self.active:
            self.run()
        try:
            exc = self.q.pop()
        except Exception:
            pass
        else:
            raise exc
        return self.distance

    def __getDistance(self):
        OG.output(self.t, True)
        time.sleep(PERIOD)
        OG.output(self.t, False)

        pulse_end = time.time()
        pulse_start = pulse_end
        dt = 0
        while OG.input(self.e) == 0 and dt < WAIT:
            pulse_start = time.time()
            dt = pulse_start - pulse_end
                    
        while OG.input(self.e) == 1 and dt < WAIT:
            pulse_end = time.time()
            dt = pulse_end - pulse_start

        delta_t = pulse_end - pulse_start
        distance = SPEED_OF_SOUND*delta_t/2.0
        distance = round(distance,2)
        distance = self.filter.filter(distance)
        self.distance = distance

    def calculateDistance(self):
        try:
            print("Starting to calc distance")
            OG.output(self.t, False)
            time.sleep(2)
            print("Starting to measure")
            
            while self.active:
               self.__getDistance()
            print("Ending to calc distance")
        except Exception as e:
            self.q.append(e)

    def stop(self):
        self.active = False
        self.thread.join()

    def run(self):
        self.active = True
        self.thread = threading.Thread(target=self.calculateDistance)
        self.thread.start()


if __name__ == '__main__':
    ul = Ultrasonic(echo, trigger, col.deque())
    #first get distance to start of sensor
    ul.getDistance()
    try:
        while True:
            print("distance: %f" % (ul.getDistance()),end="\n")
            time.sleep(.001)
    except KeyboardInterrupt:
        ul.stop()
        OG.cleanup()
        print("Ending")