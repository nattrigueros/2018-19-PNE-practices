from Seq import Seq
import http.client
import json

PORT = 80
SERVER = 'rest.ensembl.org'  # CONNECT TO THE IP OF THE WEBSITE

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request('GET', '/homology/symbol/human/FRAT1?content-type=application/json')  # SEND A PETITION TO WEB
r1 = conn.getresponse()
print('Response received!: {} {}\n'.format(r1.status,r1.reason))
data1 = r1.read().decode('utf-8')
answer = json.loads(data1)
id = answer['data'][0]['id']   # GET THE ID FROM THE WEB
print(id)

conn.request('GET','/sequence/id/'+id+'?content-type=application/json')  # SEND A PETITION TO THE WEB WITH THE ID
r1 = conn.getresponse()
data1 = r1.read().decode('utf-8')
answer = json.loads(data1)
print(answer)
sequence = answer['seq']   # RECIEVE THE SEQUENCE FROM THE WEB
print(sequence)

s1 = Seq(sequence) # CREATE AN OBJECT WITH THE SEQUENCE
print('Total number of bases:', len(sequence))  # CALCULATE THE TOTAL NUMBER OF BASES IN THE SEQUENCE
print('Number of bases T:', s1.count('T'))  # COUNT THE NUMBER OF T BASES

# THIS IS THE LOOP THAT IS GOING TO EVALUATE WHICH IS THE MOST POPULAR BASE AND PRINT ITS PERCENTAGE

if s1.perc('A')>s1.perc('C') and s1.perc('A')>s1.perc('T') and s1.perc('A')>s1.perc('G'):
    print('The most popular base is A, and its percentage is: ', s1.perc('A'))
if s1.perc('C')>s1.perc('A') and s1.perc('C')>s1.perc('T') and s1.perc('C')>s1.perc('G'):
    print('The most popular base is C, and its percentage is: ', s1.perc('C'))
if s1.perc('T')>s1.perc('C') and s1.perc('T')>s1.perc('A') and s1.perc('T')>s1.perc('G'):
    print('The most popular base is T, and its percentage is: ', s1.perc('T'))
if s1.perc('G')>s1.perc('A') and s1.perc('G')>s1.perc('C') and s1.perc('G')>s1.perc('T'):
    print('The most popular base is G, and its percentage is: ', s1.perc('G'))

# WE ARE GOING TO PRINT THE PERCENTAGE OF ALL BASES

print('Percentage of A: ', s1.perc('A'))
print('Percentage of C: ', s1.perc('A'))
print('Percentage of T: ', s1.perc('A'))
print('Percentage of G: ', s1.perc('A'))