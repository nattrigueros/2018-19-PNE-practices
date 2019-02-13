#SERVER  IP, PORT
import socket
from Seq import Seq

PORT = 8085
IP = "192.168.1.37"

while True:
    sequence = input('Give me a sequence: ')


    # FIRST, CREATE THE SOCKET
    # WE WILL ALWAYS USE THIS PARAMETERS: AF_INET and SOCK_STREAM

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # ESTABLISH THE CONNECTION TO THE SERVER (IP, PORT)
    s.connect((IP, PORT))

    # SEND DATA. NO STRINGS CAN BE SEND, ONLY BYTES
    # IT NECESARY TO ENCODE THE STRING INTO BYTES
    s.send(str.encode(sequence))

    #  RECIEVE DATA FROM THE SERVER
    msg= s.recv(2048).decode('utf-8')
    print('Message from the server: ')
    print(msg)
    s.close()