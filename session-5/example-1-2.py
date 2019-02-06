from bases import count_bases   # Import the function count_bases from another file

s = input('Please introduce a valid sequence: ')
s= s.upper()

length = len(s)

na = count_bases(s)[0]
nt = count_bases(s)[1]      # We can index the return from the main function and get the counters
ng = count_bases(s)[2]
nc = count_bases(s)[3]

perc_a = round((na * 100) / length, 1)
perc_t = round((nt * 100) / length, 1)  # The percentages are calculated by multiplying the counters of each base
perc_g = round((ng * 100) / length, 1)  #     by 100, and all divided by the length of the input sequence
perc_c = round((nc * 100) / length, 1)

print('\n\n     THE INFORMATION FOR ', s, 'IS THE FOLLOWING:')
print('\nThe length of the sequence is:', length)
print('\nBase A', '\n Counter:', na, '\n Percentage:', perc_a)
print('\nBase T', '\n Counter:', nt, '\n Percentage:', perc_t)
print('\nBase G', '\n Counter:', ng, '\n Percentage:', perc_g)
print('\nBase C', '\n Counter:', nc, '\n Percentage:', perc_c)
