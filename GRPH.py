fasta_input = """#input FASTA string here"""

def read_fasta(fasta_input):
    sequences = []
    headers = []
    fasta_sequences = fasta_input.strip().split('>')
    for sequence in fasta_sequences:
        lines = sequence.split('\n')
        header = lines[0]
        seq = ''.join(lines[1:])
        if header.startswith("Rosalind_"):
                headers.append(header)
                sequences.append(seq)
    seq_dict = dict(zip(headers,sequences))
    return seq_dict

seq_dict = read_fasta(fasta_input)

def overlap_graph(seq_dict):
    adj_list = []
    for k1,s in seq_dict.items():
        for k2,t in seq_dict.items():
            if k1 != k2 and s[-3:] == t[:3]:
                adj_list.append((k1, k2))
    return adj_list

overlap_graph_list = overlap_graph(seq_dict)

for edge in overlap_graph_list:
    print(edge[0], edge[1])
