import bluetooth
import Car as Car
import RPi.GPIO as G

G.setmode(G.BOARD)

class OmniCar(Car.Car):
    def right(self, speed):
        self.wtl.fordward(speed)
        self.wtr.backward(speed)
        self.wbr.backward(speed)
        self.wbl.fordward(speed)
    
    def left(self, speed):
        self.wtl.backward(speed)
        self.wtr.fordward(speed)
        self.wbr.fordward(speed)
        self.wbl.backward(speed)

def createSocket(port) :
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.bind(("", port))
    sock.listen(1)
    return sock

def connectToClient(sock):
    client,address = sock.accept()
    print("Connected to {}".format(address))
    return client

def main():
    port = bluetooth.PORT_ANY
    print("Creating Socket")
    socket = createSocket(port)
    print("Connecting to Client {}".format(socket))
    client = connectToClient(socket)
    client.send("hello!!\r\n")

    wheels = {"top_right":{"name":"top_right","e":32,"f":24,"r":26},\
            "top_left":{"name":"top_left", "e":19,"f":23,"r":21},\
            "bottom_right":{"name":"bottom_right", "e":22,"f":18,"r":16},\
            "bottom_left":{"name":"bottom_left", "e":11,"f":15,"r":13}}
    car = OmniCar(wheels)
    speed = 70
    while True:
        try:
            data = client.recv(1024).decode()
            print("Data: %s" % data)
            if data == '0':
                print("Forward")
                car.fordward(speed)
            if data == '1':
                print("Backward")
                car.backward(speed)
            if data == '2':
                print("Right")
                car.right(speed)
            if data == '3':
                print("Left")
                car.left(speed)
            if data == '4':
                print("Stop")
                car.stop()
            client.send("rcv:{}\r\n".format(data))
        except KeyboardInterrupt:
            print("Keyboard interupt")
            client.close()
            socket.close()
            car.stop()
            break
        except Exception as e:
            print(e) 
            client.close()
            socket.close()
            car.stop()
            print("Closed client socked")
            print("Creating new socket")
            socket = createSocket(port)
            print("Waiting for client")
            client = connectToClient(socket)


if __name__ == '__main__':
    print("starting encoder main")
    main()
    G.cleanup()
    print("Closing encoder")
