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

print(HammingDistance("TCAACCCTTCACGCGGTGAATTCTACTGATTAGGAGTATACATTGAAAACCTTGCCAGTCATTATATAGGTGGGTGCACGTTTAGAGCCCATCCACGGCGTAGCTCTCAAGTCGTCCGTTCAATCGAGTTTCGAAGATCAGACAGTCCGTTAGGTCTGTACTGTAAGACATGCGACACGTCAAACAACGCTGTAACAGCGCCGGGCTATTTATACTATTCAATCCTGCATATAAAGGAAGGGAGATGGGAACATCTCTATACGAGTCGCGTTCGCGACTTTGGACGCACAGAACTGCTGGTCAAGGGGCTCCACTATATCCTTTCGTACCTGGCGACGGCATAAAAACATCCGTTGGTATTCCCCCCTCATAGGGACCGTGCTAGGGGTACCCACTTATTGAGGACAATTAGGATCGTACGCGAACACTAAGGGCACACGACAAAGCCTGCCGGAGTGGGAAATTAACGATGTACAGTCACCCAACTAGCGCGGGGTAGAGCGTTGTATGCATGTATGGTGGTCCTCGAGTATTGAGCCTATCGTATTCTTGTCCTAATGATCGGCGGTGATCCCATAGTCTTTCCAGATCAGGTGCATTTCGTGAAAGTGAATGGCCGACGTACAACGAAGCTTCTCGAGAGGCCCGGTGGAGTTAAATACTAACCGTAATCTCGCTTGGCATCTTGCACCACCCAGGTGTCCGCAATCACGACCGAGTAGCGATTGATGCCTTCGCTGCCCTGTCGCAATCAAAAGACGAATTATAGGCGATATGCATTGTGTTAGTTATCCGGCCAGTTGGACTCCCTGGTACTGCCGAACATGTTCGCAACCTCGGTAGACCAGAGATATAGAAATCTCCAAGAGTCACCCTCGGTGGGGGTATGCAGCTTAGAGCTTTTTAGTCATCCCCCAGCGAGC", "GGTGCCCTATCCGTGAAAATTTAGTCTGAGTGGGCATGTTCACGGCGAGCAGTGCCGGGCGGCAAATCGGTTTGCATAAGGATGGACTCCCGACAGGTCGTAAGGGAATTGGAGTTCCCTCAGTCAAACTTCGAGCTTTTATTTCTCCGTTCTTCATAGACTGAAAGGCGGGCTGCACCTCAAACAGTGCTGTTATTCGACCTGGGGATTCAAACGCTGAAAACGTGTAGATAAGTGACCAGTCTTCGTGACAAGTGCACGACAGAAACCTCCGCGTCGTTGGTTCCGACCACCCGTTGCTAAAGTAGCTGCAGCGGAGGAAGCCGTACCTCGGGATGCAATACAAAGTTCCCCAGGTCCCCCCCTTCGCATGGGAACGTACCATATTTCCCAACGACGTGGTCCCTTTGCTGTCTCGCGACGATCCCGTCGGGTCGATGAGCACTGCGCTAATAACAAGAATTTAACGAGGGCCCGGCGGCCCAGACTCCTGGACGCGACGGTCGCTGAGAACATGGCTACAGCCCCACTTGTGGTGCGCTGGTCTACGATTCCTTACGCGCGACCGTGGTAGCCTAATCATTCCGAACAGGGTCGATCTGATAAAAACGCATGCAATAGTGGCAACTCCGCAACTCGGGAGTGACGGTAGATTTATAACCTCGCTGAATTCTGGCATCGAATCATCAACCATAAAAGTGTCCGCAATGAAACCTAAGAATAACCTGATCATTCCGATCGCTTGCCCTAAATCACGCTATGAATATGTGACAAATTATCAGTCGCTGCCTTCAGCACGATAGGAATACTTGGCACCTCCACGCACGGTCGGAACCTATTAAAACATTAGCTACCACGTTTTCGACGACAGTTCAGGTGCCATGGTATGCAGTGTTTTGGTATTGACTGTTAACCCAGCACAT"))