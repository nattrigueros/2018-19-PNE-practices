import socket

# SERVER IP, PORT
IP = "10.3.53.200"
PORT = 8082

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necessary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))

# Receive data from the server
msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)

s.close()