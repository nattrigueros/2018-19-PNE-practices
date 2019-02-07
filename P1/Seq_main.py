from Seq import Seq

s1= Seq('AATTCGG')   #SEQ 1
s2 = Seq('ACTGACTG') #SEQ 2
s3 = s1.complement() #SEQ 3
s4 = s2.reverse() #SEQ 4

#INFORMATION FOR SEQUENCE 1
print('SEQUENCE 1:', s1.strbases, '\n Length: ', s1.length())
print(' Bases Count: ','A:', s1.count('A'),',C:',s1.count('C'),',T:',s1.count('T'),',G:',s1.count('G'))
print(' Bases Percentage: ','A:',s1.perc('A'),'%,','C:',s1.perc('C'),'%,','T:',s1.perc('T'),'%,','G:',s1.perc('G'),'%,')

#INFORMATION FOR SEQUENCE 2
print('\nSEQUENCE 2:', s2.strbases, '\n Length: ', s2.length())
print(' Bases Count: ','A:', s2.count('A'),',C:',s2.count('C'),',T:',s2.count('T'),',G:',s2.count('G'))
print(' Bases Percentage: ','A:',s2.perc('A'),'%,','C:',s2.perc('C'),'%,','T:',s2.perc('T'),'%,','G:',s2.perc('G'),'%,')

#INFORMATION FOR SEQUENCE 3 (COMPLEMENT OF S1)
print('\nSEQUENCE 3:', s3.strbases, '\n Length: ', s3.length())
print(' Bases Count: ','A:', s3.count('A'),',C:',s3.count('C'),',T:',s3.count('T'),',G:',s3.count('G'))
print(' Bases Percentage: ','A:',s3.perc('A'),'%,','C:',s3.perc('C'),'%,','T:',s3.perc('T'),'%,','G:',s3.perc('G'),'%,')

#INFORMATION FOR SEQUENCE 4 (REVERSE OF S2)
print('\nSEQUENCE 4:', s4.strbases, '\n Length: ', s4.length())
print(' Bases Count: ','A:', s4.count('A'),',C:',s4.count('C'),',T:',s4.count('T'),',G:',s4.count('G'))
print(' Bases Percentage: ','A:',s4.perc('A'),'%,','C:',s4.perc('C'),'%,','T:',s4.perc('T'),'%,','G:',s4.perc('G'),'%,')