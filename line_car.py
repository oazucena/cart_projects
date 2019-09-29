import bluetooth
import Bluetooth as B
import RPi.GPIO as G
import omni_car as oc

def applyCommand(command, car, speed) :
    if command == 0:
        print("fordward")
        car.fordward(speed)
    elif command == 1:
        print("backward")
        car.backward(speed)
    elif command == 2:
        print("left")
        car.left(speed)
    elif command == 3:
        print("right")
        car.right(speed)
    elif command == 4:
        print("stop")
        car.stop()
    elif command == 5:
        print("speed")
        speed = input("Speed ")
    elif command == 6:
        print("wheels")
        wheel = input("Specify wheel 0 1 2 3")
        car.spin(wheel, speed)

def main():
    print("line car")
    wheels = {"top_right":{"name":"top_right","e":32,"f":24,"r":26},\
            "top_left":{"name":"top_left", "e":19,"f":23,"r":21},\
            "bottom_right":{"name":"bottom_right", "e":22,"f":18,"r":16},\
            "bottom_left":{"name":"bottom_left", "e":11,"f":15,"r":13}}
    car = oc.OmniCar(wheels)
    speed = 30

    port = bluetooth.PORT_ANY
    blue = B.BlueTooth(port)
    
    blue.connectToClient()
    blue.send("hello!!\r\n")

    while True:
        try:
            data = blue.read()
            if data == None:
                pass
            else :
                data = int(data)
                applyCommand(data, car, speed)

        except bluetooth.btcommon.BluetoothError as btErr:
            print(btErr)
            blue.close()
            car.stop()
            print("Re-start")
            blue = B.BlueTooth(port)
            blue.connectToClient()
        except KeyboardInterrupt:
            print("Keyboard interupt")
            car.stop()
            break


if __name__ == '__main__':
    print("starting main")
    main()
    G.cleanup()
    print("Closing program")
