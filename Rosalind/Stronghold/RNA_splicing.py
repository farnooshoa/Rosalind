'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: RNA Splicing
Rosalind ID: SPLC
Rosalind #: 022
URL: http://rosalind.info/problems/splc/
'''
# Standard RNA Codon Table
codon_table = {
    'AUG': 'M', 'UGG': 'W', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def parse_fasta(fasta_string):
    fasta_dict = {}
    entries = fasta_string.strip().split('>')
    for entry in entries:
        if entry:
            lines = entry.split('\n')
            fasta_dict[lines[0]] = ''.join(lines[1:])
    return fasta_dict

def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna

def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')

def translate_rna_to_protein(rna):
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon_table.get(codon) == 'Stop':
            break
        protein.append(codon_table.get(codon, ''))
    return ''.join(protein)

# Example input in FASTA format
fasta_input = """>Rosalind_2677
ATGCGCACAGTATGGTCTCTGCCTGGTACTTAGCTATATCACTCAAACATAATGTTCTTG
CATTGGGGACCTCCAGCAAAGCATCTAGGGGGTTCACATCGTTCAAGACCTTCCTGAATC
TTGTTGAGTACTTTCCGACCAGCTACAAGACCGCCGAGAATCCGATATCAGAACAGGGAG
TATTCTCCGATATACCCGAATATGCAAGGGTGCGCGGAGTTGATCAGTTCTAACCCCACC
GTACCAGGCAACGGATAATGCCAAGAATCGTTTTCAACACTACTCAATGTGGAGCAGTGA
ATCGCATCTGAAATTGAACAATTCGAAATATTTCACGAAAGCAAAGCAGTGCCATCTGTG
TTCCTCATGGACTGGCTCTGTGCGGCGCCCGATCTAGTCGCCGTTAGAGTCGGTGTGGCA
CTTTGGCGAAGCCAGGGAATGAGAGCCTACGGTTCCAAAATACCAGGAACCCGTATTACG
GTGAAATGCATCGTGCGATCTCCAGGTCGTGTAAGCCTGTATGGGCTTGTAAATAAGCAA
TCGAGCACCAATCCCGCTGGTAAAAGAGATCTCTCTAGGATTTGAACCTCGATGTACGGT
TCTTGAGCAATTGTCGTGCGCAATTGCACTGAAGCTCGGCCGTTATTGGTCACAGCGACT
CAATCGGGATAAGAATTGCTGCTTCAGAATCACCTGTCCTGATAGCAGTGTTTTCCGGGG
CGCGGGAGGCACATTCGGTATTGCGGAACGAGAGGGAGCGCCCACGCCCTAAATTTACCT
TTGCTGTCCCTAACGCTTTTGGTCTGCGAAGACCCCTAACTTTCAAGCGGCTGGGAGAGC
GGAATTTGATCACAGAACCAGTTCTATAACTTAGTCTCAAGTACTACGCGTGCAACCAGG
GTGTACCGCAGGTAG
>Rosalind_1557
CCTAAATTTACCTTTGCTGTCCCTAACGCTTT
>Rosalind_3362
GACCGCCGAG
>Rosalind_4073
TGTAAGCCTGTATGGGCTTGTAAATA
>Rosalind_4702
CCTCGATGTACG
>Rosalind_8125
CTAGGGGGTTCACATCGTTCAAGACCTTCCTGAATCTTGTTGAGTACTT
>Rosalind_4837
TCAGAATCACCTGTCCTGATAGCAGTGTTT
>Rosalind_4182
TAGCTATATCAC
>Rosalind_1069
GCCTACGGTTC
>Rosalind_7236
GTGAATCGCATCTGAAATTGAACAATTCGAAATATTTCA
>Rosalind_5925
GGGAGAGCGGAATTTGATCACAG
>Rosalind_2655
GCCATCTGTGTTCCTCATGGACTGGCTCTGTGCGGCG
>Rosalind_8128
AGGGTGCGCGGAGTTGATCAGTTCTAACCC
>Rosalind_6014
GCACTGAAGCTCGGCCGTTATTGGTCACAGC
"""

fasta_data = parse_fasta(fasta_input)

# Extract the main DNA string and introns
main_dna = fasta_data.pop('Rosalind_2677')
introns = list(fasta_data.values())

# Process the DNA string
exon_dna = remove_introns(main_dna, introns)
rna_sequence = transcribe_dna_to_rna(exon_dna)
protein_string = translate_rna_to_protein(rna_sequence)

print(protein_string)
