'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Open Reading Frames
Rosalind ID: ORF
Rosalind #: 018
URL: http://rosalind.info/problems/orf/
'''
import re

def read_fasta(fasta_string):
    lines = fasta_string.strip().split('\n')
    dna_string = ''.join(lines[1:])
    return dna_string

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def translate_rna_to_protein(rna):
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUC': 'I',
        'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if codon_table[codon] == 'Stop':
            break
        protein.append(codon_table[codon])
    return ''.join(protein)

def find_orfs(dna):
    orfs = set()
    for frame in range(3):
        for i in range(frame, len(dna), 3):
            if dna[i:i+3] == 'ATG':  # start codon
                for j in range(i, len(dna), 3):
                    if dna[j:j+3] in ['TAA', 'TAG', 'TGA']:  # stop codons
                        rna = dna[i:j].replace('T', 'U')
                        protein = translate_rna_to_protein(rna)
                        if protein:
                            orfs.add(protein)
                        break
    return orfs

def find_candidate_proteins(dna):
    reverse_dna = reverse_complement(dna)
    orfs = set()
    orfs.update(find_orfs(dna))
    orfs.update(find_orfs(reverse_dna))
    return orfs

# Example usage
fasta_string = """>Rosalind_3958
GTTACGAAGTTACTGAGAAATCCAATTTCTGTATCACGATTCATCCATCCCTACTTCCGT
AATGGAATGTAACTTTATCAAAACTTCTTTACAGTATCTCTCTTTTGATTCGCTTACAGC
ATACGCACCTCTCCGTATCACTCTGAACAGGCCCCGCTCATGTTGCATTGCATTGCAATG
CATTGTGCTCGTCTTCCATCCGAAGTTCCTTCATACAATAGTACCCTTTCTACAATGCCC
CTTTTAGGTCTAGGTACGGGTCTCAGGCCTCCACGCTTATACTGCCAGAATCTTGGCTGG
ACTAGTGTCCGTCCCACTACCGTTAATCTGTTTTCTCTGGCCTTATAGTCCCGCACGAAC
TCTCGCGGCATTAGTGGGACAGTCTAGTTGCTAGAAGCTACGATATGCGGTCATCAAGTG
GGACAGAAGAGGGTTAGCTAACCCTCTTCTGTCCCACTTGATGACCGCATAAGCGTGAAT
TAGGGCCACCGTGCGGATCTTTTGCCCGCTCCAGAAACGGGAACCGGACAGTGACAACAA
ATGGAATAAACGTCGAAGACTGTAGGTGTTGACTCTTCCCAGGTAGCTACCCAGGCCCGA
TGAAGTCTATACGACTTTATGGATGTTGACCCCCACATCCGTTCCCGGGTGTCTGCAAAT
TTTCTCCGGACGGTACCACTGGATTGCTGATGACGTCCTCGGGAGAATATCTGAAGTTCC
GGCCAGAACTTTACATAGATTGGCCCTTGGTAGGAGAAAAGACCGTGTACCACGCGCGGA
GCAATTGCGACAGCTCTGTAGGTCATATCCATCGTTCTCCTACTAGATGTTGAACCGCTT
AGCCATATTTGTTAGTATATTCTCAAAAGAAATC
A"""
dna_sequence = read_fasta(fasta_string)
candidate_proteins = find_candidate_proteins(dna_sequence)
for protein in candidate_proteins:
    print(protein)
