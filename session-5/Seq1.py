class Seq:
    # A class for representing sequences
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

s1 = Seq('ATTAAGGTTT')
s2 = Seq('AACCCTTTGGGG')

l1 = s1.len()
l2 = s2.len()

class Gene(Seq):
    #This class is dereived from the Seq All the objects of the class Gene will inheritage the methods from Seq Class
    pass

print('The length of the first sequence is:', l1)
print('The length of the second sequence is', l2)