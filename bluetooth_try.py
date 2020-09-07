import bluetooth
import Car as Car
import RPi.GPIO as G

G.setmode(G.BOARD)
def createSocket(port):
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.bind(("", port))
    sock.listen(1)
    return sock

def connectToClient(sock):
    client,address = sock.accept()
    print("Connected to {}".format(address))
    return client

def main():
    devices = bluetooth.discover_devices()
    print(devices)
    port = bluetooth.PORT_ANY
    print("Creating Socket")
    socket = createSocket(port)
    print("Connecting to Client {}".format(socket))
    client = connectToClient(socket)
    client.send("hello!!\r\n")

    while True:
        try:
            data = client.recv(1024)
            print("Data: %s" % data)
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
