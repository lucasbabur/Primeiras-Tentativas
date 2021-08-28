def GCcontent(seq):
    return (seq.count('C') + seq.count('G')) / len(seq) * 100

f = open("test.txt", "r")
strings = f.read()
separator = []
stringg = ""

for letters in strings:
    if letters == ">":
        separator.append(stringg)
        stringg = ""
    if letters != "\n":
        stringg = stringg + letters
    
separator.append(stringg)
separator.pop(0)

conteudo = 0
maior = 0
maior_label = ""
savior = 0

label = separator[2][0:14]
DNA = separator[2][14:len(separator[2]) - 1]



number = 0

for seqs in separator:
    
    

    label = seqs[0:14]
    DNA = seqs[14:len(separator[number])]
    

    conteudo = GCcontent(DNA)

    if conteudo > maior:
        maior = conteudo
        maior_label = label
    number += 1

print("Resultado: ")
print(maior_label)
print(maior)

#Rosalind_4350 52.335329%


    





    