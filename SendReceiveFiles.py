

#Send data 

import socket
from sendfile import sendfile

file = open("somefile", "rb")
sock = socket.socket()
sock.connect(("127.0.0.1", 8021))
offset = 0

while True:
    sent = sendfile(sock.fileno(), file.fileno(), offset, 65536)
    if sent == 0:
        break  # EOF
    offset += sent

#Receive sendfile data

        while 1: 
            data = conn.recv(blocksize)
            if not data: 
                break
            callback(data)
        conn.close()

#Socket Server

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection
   
#Socket Client

