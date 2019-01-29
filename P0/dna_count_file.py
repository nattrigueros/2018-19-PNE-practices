seq0='AGTACACTGGT' \
     'ACCAGTGTACT' \
     'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'
seq0=seq0[:seq0.find('\n')]
seq=seq0.replace('\n','')
length= len(seq)
print('The lenght of the introduced DNA sequence is: ', length)
print('The number of times we can find A in the DNA sequence: ', seq.count('A'))
print('The number of times we can find C in the DNA sequence: ', seq.count('C'))
print('The number of times we can find T in the DNA sequence: ', seq.count('T'))
print('The number of times we can find G in the DNA sequence: ', seq.count('G'))