from DNAToolkit import *
import random

# Create a Random DNA String
randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(20)])
randDNAStr2 = ''.join([random.choice(Nucleotides) for nuc in range(20)])

print(randDNAStr)
print(FindInSEQ(randDNAStr, 'T'))
    




    