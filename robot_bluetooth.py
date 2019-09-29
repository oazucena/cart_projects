import bluetooth
import Bluetooth as B
import Car as Car
import RPi.GPIO as G

G.setmode(G.BOARD)

def main():
    wheels = {"top_right":{"name":"top_right","e":32,"f":24,"r":26},\
            "bottom_left":{"name":"bottom_left", "e":22,"f":18,"r":16},\
            "bottom_right":{"name":"bottom_right", "e":19,"f":21,"r":23},\
            "top_left":{"name":"top_left", "e":11,"f":13,"r":15}}
    car = Car.Car(wheels)
    speed = 30

    port = bluetooth.PORT_ANY
    blue = B.BlueTooth(port)
    
    blue.connectToClient()
    blue.send("hello!!\r\n")

    while True:
        try:
            data = blue.read()
            print("Data: %s" % data)
            if data == '0':
                car.fordward(speed)
            if data == '1':
                car.backward(speed)
            if data == '2':
                car.right(speed)
            if data == '3':
                car.left(speed)
            if data == '4':
                car.stop()
            blue.send("rcv:{}\r\n".format(data))
        except KeyboardInterrupt:
            print("Keyboard interupt")
            blue.close()
            car.stop()
            break
        except Exception as e:
            print(e)
            blue.close()
            car.stop()
            print("Re-start")
            blue = B.BlueTooth(port)
            blue.connectToClient()


if __name__ == '__main__':
    print("starting main")
    main()
    G.cleanup()
    print("Closing program")
