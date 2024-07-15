'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Shared Motif
Rosalind ID: LCSM
Rosalind #: 014
URL: http://rosalind.info/problems/lcsm/
'''

from scripts.FASTA import ReadFASTA

def longest_common_substring(sequences):
    # Start with the first sequence as the base for comparison
    base_seq = sequences[0]
    longest_substr = ""
    
    # Generate all possible substrings of the base sequence
    length = len(base_seq)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substr = base_seq[i:j]
            # Check if this substring is present in all sequences
            if all(substr in seq for seq in sequences):
                if len(substr) > len(longest_substr):
                    longest_substr = substr
    return longest_substr

# Read sequences from FASTA file
filename = 'sequence.fasta'
sequences_dict = ReadFASTA(filename)
sequences = list(sequences_dict.values())

# Find and print the longest common substring
lcs = longest_common_substring(sequences)
print(f"Longest Common Substring: {lcs}")
