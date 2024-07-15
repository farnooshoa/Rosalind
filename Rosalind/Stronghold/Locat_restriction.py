'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Locating Restriction Sites
Rosalind ID: REVP
Rosalind #: 021
URL: http://rosalind.info/problems/revp/
'''
def parse_fasta(fasta_string):
    lines = fasta_string.strip().split('\n')
    return ''.join(lines[1:])  # Join all lines except the first one

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna, min_len=4, max_len=12):
    palindromes = []
    n = len(dna)
    
    for length in range(min_len, max_len + 1):
        for i in range(n - length + 1):
            substring = dna[i:i + length]
            if substring == reverse_complement(substring):
                palindromes.append((i + 1, length))
                
    return palindromes

# Example FASTA input
fasta_input = """>Rosalind_9959
TATACGCCGCCTTCGGGAACAAGGCTTGCCACAGTGGCCCCCAGACCCCTGTGTGCATCC
AAACATATGTGAGGTTAGTCTCTTCCTTTAGACTGTGGGATGTGGAAGTTACGTCCGATC
TCTCCACTGGCTCCACCCCAGGGTCGGCGGGGTGTTCCCTTTGTCGCTTATTTAGCTGTT
AAGCTGTGCCTTTAGCATACGTGCCAACCTAGGCCCAGAAGGAATATGATCTGCCTTGGC
AGGACATGGGGCTGTTAGTTGTTCTAAATGCTTGCTATTGAGCGAGACCGCAAGTAGCGT
CGAAGCGGCATCTCAGAATAGGCGAACGTCAATACCATGTCCCACCAAACGGGGGGCTTC
GACATGCGCGGCATGCTATCGAAAATCTAGATTATTAACACCGTAGGCGTATAAGCACCA
CCTTCTATGGTGGCTTCCGCCGCATGGTCATCTACTCGTCCGATGTTATTGCTGGAGGTC
TACAGCATATGCTGATCTCTTTTGCATGTTCGCCTACATACTGTAGACAGTCGGAAGTCT
TGTTGCTCTTACAGGAGGAAACCGACGCGATGAGACGTACGTCATCCCGTGCACCTGAGG
CCTATACGGGGACGGGGTAACTGGTCCGAAGCGATCAGTTGCTCGGGGACTGCGTGGTAA
TGCTTCTGGGCAGTCACGGGATTGAGCTGCTACCCTACATGCACTAAACGAGACATATTC
CCGACTTACAAAATGGGTACCGGGTTCACCGCCCGTTCAATAAGCCTTGCTATTCCGAGA
CTACCACTTCTTTAACGACGCATCCGTTTACACGTCTGTAGACGAGCAAAGGAGCAGTAA
CACATAAGGTATGGTCTCGCCCCAAGGCCATACCCCAGTACTGTATCGTATTCTCCGACG
CTTGTCGGAAACGTTGGCGACGGGGTTTATCTAGTACGAAACGGAGCGACCAAGCTCCTG
CCTGAGCGGACGCGCG
"""

dna_string = parse_fasta(fasta_input)
palindromes = find_reverse_palindromes(dna_string)

# Print the results
for pos, length in palindromes:
    print(pos, length)
