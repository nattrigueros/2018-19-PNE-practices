import socket
import termcolor
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8091
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def valid_sequence(s):
    bases = 'ACTG'
    for letter in s:               # SEE IF THE SEQUENCE HAS VALID NITROGENOUS BASES (A, C, T & G)
        if letter not in bases:
            return False
    return True

def calculations(s1, command):

    print('Doing a command: ', command)

    if (command == 'len'):
        return s1.length()
    elif (command ==  'complement'):
        cadena= s1.complement().getBase()         # APPLYING SEQ CLASS FOR THE REQUESTED COMMAND
        print (cadena)
        return cadena
    elif (command ==  'reverse'):
        return s1.reverse().getBase()
    elif (command == 'countA'):
        return s1.count('A')
    elif (command == 'countC'):
        return s1.count('C')
    elif (command == 'countT'):
        return s1.count('T')
    elif (command == 'countG'):
        return s1.count('G')
    elif (command == 'percA'):
        return s1.perc('A')
    elif (command == 'percC'):
        return s1.perc('C')
    elif (command == 'percT'):
        return s1.perc('T')
    elif (command == 'percG'):
        return s1.perc('G')
    else:
        return 'ERROR'

def process_client(cs):

    # Read the client message.  Decode it as a string
    msg = cs.recv(2048).decode('utf-8')

    # Print the received message in color red
    termcolor.cprint(msg, 'red')

    response=''
    if (msg == '\n'):
        response = 'ALIVE'
    else:
        print ("Received", msg)
        separating = msg.split('\n')
        print('Attending request...', separating[0])
        if (valid_sequence(separating[0])):
            response = 'OK\n'
            s1 = Seq(separating[0])

            for i in range(1, len(separating)-1):
                print('LOOKING AT... ', i, separating[0])
                r = calculations(s1, separating[i])
                response = response + str(r) + '\n'
        else:                             # IF IT IS NOT A VALID SEQUENCE
            response = 'ERROR'

    cs.send(str.encode(response))
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