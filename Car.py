import bluetooth
import wheel as W
import RPi.GPIO as G

G.setmode(G.BOARD)

def setUpWheel(wsp):
    name = wsp["name"]
    e = wsp["e"]
    f = wsp["f"]
    r = wsp["r"]
    print("Wheel {} e:{} f:{} r:{}".format(name, e, f, r))
    return W.Wheel(e,f,r)

class Car:
    def __init__(self, wheelSetup):
        print("Setting up top_left wheel")
        wtls = wheelSetup["top_left"]
        self.wtl = setUpWheel(wtls) 
        print("Setting up top_right wheel")
        wtrs = wheelSetup["top_right"]
        self.wtr = setUpWheel(wtrs)

        print("Setting up bottom_left wheel")
        wbls = wheelSetup["bottom_left"]
        self.wbl = setUpWheel(wbls) 
        print("Setting up bottom_right wheel")
        wbrs = wheelSetup["bottom_right"]
        self.wbr = setUpWheel(wbrs)

    def fordward(self, speed):
        self.wtl.fordward(speed)
        self.wtr.fordward(speed)
        self.wbr.fordward(speed)
        self.wbl.fordward(speed)


    def backward(self, speed):
        self.wtl.backward(speed)
        self.wtr.backward(speed)
        self.wbr.backward(speed)
        self.wbl.backward(speed)

    def right(self, speed):
        self.wtl.fordward(speed)
        self.wtr.fordward(0)
        self.wbr.fordward(0)
        self.wbl.fordward(speed)
    
    def left(self, speed):
        self.wtl.fordward(0)
        self.wtr.fordward(speed)
        self.wbr.fordward(speed)
        self.wbl.fordward(0)

    def stop(self):
        self.wtl.fordward(0)
        self.wtr.fordward(0)
        self.wbr.fordward(0)
        self.wbl.fordward(0)

    def spin(self, w, speed):
        if w == 0:
            self.wtr.fordward(speed)
        if w == 1:
            self.wtl.fordward(speed)
        if w == 2:
            self.wbr.fordward(speed) 
        if w == 3:
            self.wbl.fordward(speed)

def main():
    wheels = {"top_right":{"name":"top_right","e":32,"f":24,"r":26},\
            "top_left":{"name":"top_left", "e":19,"f":23,"r":21},\
            "bottom_right":{"name":"bottom_right", "e":22,"f":18,"r":16},\
            "bottom_left":{"name":"bottom_left", "e":11,"f":15,"r":13}}
    car = Car(wheels)
    speed = 50
    while True:
        try:
            data = input("Command ")
            print "Data: %s"%data
            if data == 0:
                print("fordward")
                car.fordward(speed)
            if data == 1:
                print("backward")
                car.backward(speed)
            if data == 2:
                car.left(speed)
            if data == 3:
                car.right(speed)
            if data == 4:
                speed = input("Speed ")
            if data == 5:
                car.stop()
            if data == 6:
                wheel = input("Specify wheel 0 1 2 3")
                car.spin(wheel, speed)
        except KeyboardInterrupt:
            print("Keyboard interupt")
            car.stop()
            break


if __name__ == '__main__':
    print("starting main")
    main()
    G.cleanup()
    print("Closing program")
