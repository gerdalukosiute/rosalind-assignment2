def read_fasta(fasta_input):
    sequences = []
    fasta_sequences = fasta_input.strip().split('>')
    for sequence in fasta_sequences:
        lines = sequence.split('\n')
        header = lines[0]
        seq = ''.join(lines[1:])
        if header.startswith("Rosalind_"):
            sequences.append(seq)
    return sequences

def overlap(seq1, seq2):
    max_overlap = 0
    for i in range(1, len(seq1)):
        if seq2.startswith(seq1[i:]):
            max_overlap = len(seq1) - i
            break
    return max_overlap

def shortest_superstring(sequences):
    while len(sequences) > 1:
        max_overlap_length = -1
        best_1, best_2 = -1, -1

        for seq1 in range(len(sequences)):
            for seq2 in range(len(sequences)):
                if seq1 != seq2:
                    overlap_len = overlap(sequences[seq1], sequences[seq2])
                    if overlap_len > max_overlap_length:
                        max_overlap_length = overlap_len
                        best_1, best_2 = seq1, seq2

        if best_1 != -1 and best_2 != -1:
            merged_string = sequences[best_1] + sequences[best_2][max_overlap_length:]
            sequences.pop(best_1)
            sequences.pop(best_2 - 1 if best_2 > best_1 else best_2)
            sequences.append(merged_string)

    return sequences[0]

input_data = """#input fasta strings here"""

sequences = read_fasta(input_data)
shortest_superstring = shortest_superstring(sequences)
print(shortest_superstring)