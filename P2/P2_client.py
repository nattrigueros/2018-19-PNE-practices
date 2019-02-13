#SERVER  IP, PORT
import socket
from Seq import Seq

IP = '192.168.1.37'
PORT = 8087

while True:
    sequence = input('Give me a sequence: ')
    s1 = Seq(sequence)
    s2 = s1.complement()
    s3 = s1.reverse()
    # FIRST, CREATE THE SOCKET
    # WE WILL ALWAYS USE THIS PARAMETERS: AF_INET and SOCK_STREAM

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # ESTABLISH THE CONNECTION TO THE SERVER (IP, PORT)
    s.connect((IP, PORT))

    # SEND DATA. NO STRINGS CAN BE SEND, ONLY BYTES
    # IT IS NECESSARY TO ENCODE THE STRING INTO BYTES
    seq1='\n' + 'This is the complement sequence:' + s2.strbases + '\n'
    seq2='This is the reverse sequene:' + s3.strbases

    s.send(str.encode(seq1))
    s.send(str.encode(seq2))

    #  RECIEVE DATA FROM THE SERVER
    msg= s.recv(2048).decode('utf-8')
    print('Message from the server: ')
    print(msg)
    s.close