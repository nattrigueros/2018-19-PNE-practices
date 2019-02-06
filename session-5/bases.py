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