Nucleotides = ["A", "C", "G", "T"]


# Check to make sure it's a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return True

# Nucleotide Frequency
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

# Função que transforma um DNA em um RNA
def RNAtranscription(seq):
    RNA = ""
    if(validateSeq(seq)):
        for nuc in seq:
            if (nuc == 'T'):
                nuc = 'U'
            RNA = RNA + nuc
        return RNA
            
    else:
        raise("String is not a DNA! Please verify if it's an DNA [1]")

# Função de complementação de DNA
def DNAcompletion(seq):
    DNA = ""
    if (validateSeq(seq)):
        for nuc in seq:
            if (nuc == 'T'):
                nuc = 'A'
            elif (nuc == 'A'):
                nuc = 'T'
            elif (nuc == 'G'):
                nuc = 'C'
            else:
                nuc = 'G'
            DNA = DNA + nuc
        return DNA
    else:
        raise("String is not a DNA! Please verify if it's an DNA [1]")

# Função de reversão de DNA
def DNAreversion(seq):
    DNA = ""
    if (validateSeq(seq)):
        for nuc in seq:
            DNA = nuc + DNA
        return DNA
    else:
        raise("String is not a DNA! Please verify if it's an DNA [1]")

# Função que separa o LABEL do DNA
def FASTA_Separator(seq):
    label = ""
    DNA_String = ""
    start = 0
    number_sequence = False

    for letters in seq:
        
        if (letters.isdigit()):
            number_sequence = True

        if (number_sequence):
            if (letters.isdigit() == False):
                break
        
        label = label + letters
        

    number_sequence = False
    
    for letters in seq:
        if (start == 1):
            DNA_String = DNA_String + letters
        if (letters.isdigit()):
            number_sequence = True
        if (number_sequence):
            if (letters.isdigit() == False):
                start = 1
                DNA_String = DNA_String + letters
        

    return DNA_String, label

# Função que calcula o conteúdo de Guanina e Citosina de um DNA
def GCcontent(seq):
    return (seq.count('C') + seq.count('G')) / len(seq) * 100

def HammingDistance(seq1, seq2):

    hamming = 0

    if seq1 > seq2:
        for base in range(len(seq2)):
            if seq1[base] != seq2[base]:
                hamming += 1

    else:
        for base in range(len(seq1)):
            if seq1[base] != seq2[base]:
                hamming += 1
        

    return hamming
    
def mendel(x, y, z):
    #calculate the probability of recessive traits only
    total = x+y+z
    twoRecess = (z/total)*((z-1)/(total-1))
    twoHetero = (y/total)*((y-1)/(total-1))
    heteroRecess = (z/total)*(y/(total-1)) + (y/total)*(z/(total-1))

    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    print(1-recessProb) # take the complement

def RNAintoProtein(rna):

    rnaCodons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    codons = []
    for i in range(0,len(rna),3):
        codons.append(rna[i:i+3])
    protein = ''.join([rnaCodons[codon] for codon in codons])

    return protein
    
def FindInSEQ(seq, string):

    jumper = seq.split(string)
    total_len = 0
    index_array = []

    for ocurrences in jumper:
        index_array.append(len(ocurrences) + 1 + total_len)
        total_len = len(ocurrences) + 1 + total_len
    index_array.pop(len(index_array) - 1)
    return index_array


        

    
    

    



    


