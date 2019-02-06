class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

    def length(self):
        return len(self.strbases)

    def complement(self):
        comp_seq = ''
        for letter in self.strbases:
            if letter == 'A':
                comp_seq += 'T'
            if letter == 'T':
                comp_seq += 'A'
            if letter == 'C':
                comp_seq += 'G'
            if letter == 'G':
                comp_seq += 'C'
        return Seq(comp_seq)

    def reverse(self):
        return Seq(self.strbases[::-1])

    def count(self, base):
        counter = 0
        for i in self.strbases:
            if i == base:
                counter += 1
        return counter

    def perc(self, base):
        return self.count(base)*100/self.length()

s1= Seq('AATTCGG')
length1 = s1.length()

complement = s1.complement()

reverse = s1.reverse()

count_C = s1.count('C')
count_T = s1.count('T')
count_G = s1.count('G')
count_A = s1.count('A')

perc = s1.perc('A')

print('The length of the sequence is: ', length1)
print('The complement sequence for the sequence is: ', complement.strbases)
print('The reverse sequence for the sequence is :', reverse.strbases)
print(perc)