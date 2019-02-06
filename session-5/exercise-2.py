def count_bases(seq):

    counter_a = 0
    counter_t = 0
    counter_g = 0
    counter_c = 0

    for letter in seq:
        if letter == 'A':
            counter_a += 1
        if letter == 'T':    # In this loop we count the number of instances each base appears in the sequence
            counter_t += 1
        if letter == 'G':
            counter_g += 1
        if letter == 'C':
            counter_c += 1

    return counter_a, counter_t, counter_g, counter_c

s1 = input('Please introduce Sequence 1: ')
s2 = input('Please introduce Sequence 2: ')
s1 = s1.upper()
s2 = s2.upper()

length1 = len(s1)
length2 = len(s2)

na1 = count_bases(s1)[0]
nt1 = count_bases(s1)[1]      # We can index the return from the main function and get the counters
ng1 = count_bases(s1)[2]
nc1 = count_bases(s1)[3]

na2 = count_bases(s2)[0]
nt2 = count_bases(s2)[1]      # We can index the return from the main function and get the counters
ng2 = count_bases(s2)[2]
nc2 = count_bases(s2)[3]

perc_a1 = round((na1 * 100) / length1, 1)
perc_t1 = round((nt1 * 100) / length1, 1)  # The percentages are calculated by multiplying the counters of each base
perc_g1 = round((ng1 * 100) / length1, 1)  #     by 100, and all divided by the length of the input sequence
perc_c1 = round((nc1 * 100) / length1, 1)

perc_a2 = round((na2 * 100) / length2, 1)
perc_t2 = round((nt2 * 100) / length2, 1)  # The percentages are calculated by multiplying the counters of each base
perc_g2 = round((ng2 * 100) / length2, 1)  #     by 100, and all divided by the length of the input sequence
perc_c2 = round((nc2 * 100) / length2, 1)

print('\n\n     THE INFORMATION FOR ', s1, 'IS THE FOLLOWING:')
print('\nThe length of the sequence is:', length1)
print('\nBase A', '\n Counter:', na1, '\n Percentage:', perc_a1)
print('\nBase T', '\n Counter:', nt1, '\n Percentage:', perc_t1)
print('\nBase G', '\n Counter:', ng1, '\n Percentage:', perc_g1)
print('\nBase C', '\n Counter:', nc1, '\n Percentage:', perc_c1)

print('\n\n     THE INFORMATION FOR ', s2, 'IS THE FOLLOWING:')
print('\nThe length of the sequence is:', length2)
print('\nBase A', '\n Counter:', na2, '\n Percentage:', perc_a2)
print('\nBase T', '\n Counter:', nt2, '\n Percentage:', perc_t2)
print('\nBase G', '\n Counter:', ng2, '\n Percentage:', perc_g2)
print('\nBase C', '\n Counter:', nc2, '\n Percentage:', perc_c2)

