with open('CPLX2.txt','r') as f:

    counter_A=0
    counter_C=0
    counter_T=0
    counter_G=0

    for line in f:
        if line[0]=='>':
            continue

        counter_A+=line.count('A')
        counter_C+=line.count('C')
        counter_G+=line.count('G')
        counter_T+=line.count('T')

    print('We can find', counter_A, 'A\'s in CPLX2 gene sequence')
    print('We can find', counter_C, 'C\'s in CPLX2 gene sequence')
    print('We can find', counter_T, 'T\'s in CPLX2 gene sequence')
    print('We can find', counter_G, 'G\'s in CPLX2 gene sequence')
