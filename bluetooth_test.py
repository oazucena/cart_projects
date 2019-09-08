import bluetooth
import RPi.GPIO as G

G.setwarnings(False)
G.setmode(G.BCM)
G.setup(6, G.OUT)

port = bluetooth.PORT_ANY

def createSocket(port) :
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.bind(("", port))
    sock.listen(1)
    return sock

def connectToClient(sock):
    client,address = sock.accept()
    print("Connected to {}".format(address))
    return client

print("Creating Socket")
socket = createSocket(port)
print("Connecting to Client")
client = connectToClient(socket)

client.send("hello!!\r\n")

while True:
    try:
        data = client.recv(1024)
        print "Data: %s"%data
        if data == '1':
            G.output(6, True)
        if data == '0':
            G.output(6, False)
        client.send("rcv:{}\r\n".format(data))
    except KeyboardInterrupt:
        print("Keyboard interupt")
        client.close()
        socket.close()
        break
    except:
        client.close()
        socket.close()
        print("Closed client socked")
        print("Creating new socket")
        socket = createSocket(port)
        print("Waiting for client")
        client = connectToClient(socket)
print("Closing program")
