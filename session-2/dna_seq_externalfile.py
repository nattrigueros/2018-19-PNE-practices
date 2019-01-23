filename=str(input('Please introduce the name of the filename: '))
with open(filename,'r') as f:
    for line in f:
        line=line.strip('\n')
        length= len(line)
    print('The lenght of the introduced DNA sequence is: ', length)
    print('The number of times we can find A in the DNA sequence: ', line.count('A'))
    print('The number of times we can find C in the DNA sequence: ', line.count('C'))
    print('The number of times we can find T in the DNA sequence: ', line.count('T'))
    print('The number of times we can find G in the DNA sequence: ', line.count('G'))