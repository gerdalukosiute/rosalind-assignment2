fasta_string = """#input in FASTA format"""

dna_string = ""
introns = []

sequences = fasta_string.strip().split('>')
for sequence in sequences:
    lines = sequence.split('\n')
    header = lines[0]
    seq = ''.join(lines[1:])
    if header.startswith("Rosalind_"):
        if not dna_string:
            dna_string = seq
        else:
            introns.append(seq)

for i in introns:
    dna_string = dna_string.replace(i, "")

def transcription(dna_string):
    return dna_string.replace("T", "U")

rna_string = transcription(dna_string)

def translation(rna_string):
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    protein = ""
    
    for idx in range(0, len(rna_string), 3):
        codon = rna_string[idx:idx+3]  
        a_a = codon_table[codon]
        if a_a == "Stop":
            break
        protein += a_a
        
    return protein

protein = translation(rna_string)
print(protein)