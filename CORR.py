fasta_input = """#input stuff here"""

def read_fasta(fasta_input):
    sequences = []
    fasta_sequences = fasta_input.strip().split('>')
    for sequence in fasta_sequences[1:]:
        lines = sequence.split('\n')
        header = lines[0]
        seq = ''.join(lines[1:])
        if header.startswith("Rosalind_"):
            sequences.append(seq)
    return sequences

def reverse_complement(seq):
    dict_conversion = {
    "A" : "T",
    "C" : "G",
    "T" : "A",
    "G" : "C"
}
    new_seq = ''
    for pos in range(len(seq) - 1, -1, -1):
        new_seq += dict_conversion[seq[pos]]
    return new_seq
    

def point_mutations(incorrect, correct):
    count = 0
    for i in range(len(correct)):
        if incorrect[i] != correct[i]:
            count += 1
    return count

sequences = read_fasta(fasta_input)

correct = []
incorrect = []
corrected = []

for seq in sequences:
    if sequences.count(seq) > 1: 
        correct.append(seq)
    elif reverse_complement(seq) in sequences:
        correct.append(seq)
    else:
        incorrect.append(seq)

for i in incorrect:
    count = 0
    for corr in correct:
        if point_mutations(i, corr) == 1:
            if count == 0:
                count += 1
                corrected.append(str(i)+"->"+str(corr))
        elif point_mutations(i, reverse_complement(corr)) == 1:
            if count == 0:
                count +=1
                corrected.append(str(i)+"->"+str(reverse_complement(corr)))
for corr in corrected:
    print(corr)
