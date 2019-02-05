def count_a(seq):

    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    return result


# Main program

s = (input('Please, enter a valid sequence: '))
na = count_a(s)
print("The are {} As in the sequence".format(na))

# Calculate the total length
tl = len(s)

if tl>0:
    perc=round(100.0*n/tl,1)
else:
    perc=0

print("This sequence is {} bases in length".format(tl))
print("The percentages of As is {}%".format(perc))

    
print("This sequence is {} bases in length".format(tl))
print("The percentages of As is {}%".format(perc))
