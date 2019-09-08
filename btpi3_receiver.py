""" 
This python script will receive the data sent
from Android "Bluetooth Pi3 Terminal" app.

To run the program just open a terminal and type
sudo python btpi3_receiver.py

Then go to your Android app, connect to your Pi3

To get your Pi3 MAC Address, go to terminal and type
hciconfig 


And any character you type will be send to the Pi3 via Bluetooth
If you send letter e, this will end the script.

Note you need to install Blue on your Pi3, it should be installed by
default.

Rgds

Marco
"""

import bluetooth
print "Bluetooth Terminal with Voice"
print "Follow instructions on app to connect"
print "Waiting for connection..." 

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port=bluetooth.PORT_ANY
server_sock.bind(("",port))
server_sock.listen(1)
 
client_sock,address = server_sock.accept()
print "Accepted connection from",address
while True:
   data = client_sock.recv(1024)
   print "received: %s" % data
   client_sock.send(data);
   if (data == "exit"):
       client_sock.send("Stopped by android app");
       print ("Exit")
       break
 
client_sock.close()
server_sock.close()
