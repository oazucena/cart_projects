import RPi.GPIO as G
import threading

G.setmode(G.BOARD)

def increse_counter(en):
    en.increaseCounter()

class EncoderIn:
    def __init__(self, p1, p2):
        self.lastGpio = None
        self.levA = 0
        self.levB = 0
        self.p1 = p1
        self.p2 = p2
        self.counter = 0
        self._lock = threading.Lock()
        G.setup(p1, G.IN,  pull_up_down=G.PUD_UP)
        G.setup(p2, G.IN,  pull_up_down=G.PUD_UP)
        self.state = G.input(self.p1)
        G.add_event_detect(p1, G.RISING, callback=self.increaseCounter)
        
    def increaseCounter(self, channel):
        #print("Channel {}".format(channel))
        level = G.input(channel)
        with self._lock:   
            self.levA = G.input(self.p1)
            self.levB = G.input(self.p2)  
            print("{} a {}, b {}".format(channel, self.levA, self.levB))
            # When both inputs are at 1, we'll fire a callback. If A was the most
            # recent pin set high, it'll be forward, and if B was the most recent pin
            # set high, it'll be reverse.
            self.lastGpio = channel
            if self.levB:
                if self.levA:
                    self.counter -= 1
                else:
                    self.counter += 1
            else :
                if self.levA:
                    self.counter += 1
                else:
                    self.counter -= 1
    
    def getCounter(self):
        count = 0
        with self._lock:
            count = self.counter
        return count

def main():
    p1 = 10
    p2 = 8
    en = EncoderIn(p1, p2)
    counter = en.getCounter()

    while True:
        try:
            current = en.getCounter()
            if (counter != current):
                counter = current
                print("counter {}".format(counter))
        except KeyboardInterrupt:
            print("Keyboard interupt")
            break
        except Exception as e:
            print(e)
            break 
        

if __name__ == '__main__':
    print("starting encoder main")
    main()
    G.cleanup()
    print("Closing encoder")