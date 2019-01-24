def sum(n):
    count = 0
    for i in range(n):
        count = count + i + 1

    return count

#Main program
num = int(input('PLease introduce a number'))
total_sum= sum(num)
print('The total sum is {}'.format(total_sum))