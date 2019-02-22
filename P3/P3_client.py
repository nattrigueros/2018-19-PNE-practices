import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8091


while True:
    # Before connecting to the server, ask the user for the string
    sending = ''
    msg =str(input('> '))
    while len(msg)>0:
        sending = sending + msg + '\n'      # IF IT IS NOT AN EMPTY LINE
        msg = str(input(''))

    print("SENDING\n")
    if (len(sending)==0):                   # IF IT IS AN EMPTY LINE
        sending = '\n'


    # Now we can create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(sending))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
