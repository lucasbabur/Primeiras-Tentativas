from DNAToolkit import *
import random

# Create a Random DNA String
randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(20)])

Reversed = DNAreversion("AAAACCCGGT")
print(Reversed)
Completed = DNAcompletion(Reversed)
print(Completed)