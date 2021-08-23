Nucleotides = ["A", "C", "G", "T"]


# Check to make sure it's a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return True

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