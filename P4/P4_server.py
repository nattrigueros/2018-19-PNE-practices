import socket
import termcolor

IP = "127.0.0.1"
PORT = 8093
MAX_OPEN_REQUESTS = 5

def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    split = str(msg).split(' ')    # SLIT IN ORDER TO SEE THE EXTENSION THE USER WANTS
    filename = split[1].replace('/','')
    print('FILENAME: ',filename)
    if (filename=='' or filename == 'index.html'):
        FILE_HTML = 'index.html'      # IF THERE IS ONLY A '/' WE WANT TO ACCESS DIRECTLY TO THE INDEX
    elif (filename == 'blue'):
        FILE_HTML = 'blue.html'       # IF THERE IS A 'BLUE' WE WANT TO ACCESS DIRECTLY TO THE BLUE SERVER
    elif (filename == 'pink'):
        FILE_HTML = 'pink.html'       # IF THERE IS A 'PINK' WE WANT TO ACCESS DIRECTLY TO THE PINK SERVER
    else:
        FILE_HTML = 'error.html'      # IF THERE IS SOMETHING DIFFERENT FROM THE ABOVE, WE WANT TO ACCESS DIRECTLY TO THE ERROR SERVER

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Build the HTTP response message. It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language

    with open(FILE_HTML, 'r') as f:     # READ CONTENTS DEPENDING OF FILE_HTML
        contents = f.read()

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)