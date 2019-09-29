import bluetooth

class BlueTooth :
    def __init__(self, port):
        self.port = port
        print("Creating Socket")
        self.createSocket()
        print("Created Socket")

    def createSocket(self) :
        self.sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.sock.bind(("", self.port))
        self.sock.listen(1)

    def connectToClient(self):
        print("Connecting to client")
        client,address = self.sock.accept()
        self.client = client
        self.address = address
        print("Connected to {}".format(address))
    
    def send(self, data):
        self.client.send(data)

    def read(self):
        data = None
        #ox40 to skip wait
        data = self.client.recv(1024)
        print("data %s" % (data))
        return data

    def close(self):
        self.client.close()
        self.sock.close()
