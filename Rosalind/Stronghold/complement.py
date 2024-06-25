'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind #: 003
URL: http://rosalind.info/problems/revc/
'''

def complement (text):
   return text.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]


text = "AATATTAGTCTTAACCAGTATTTCCGATATTACGTAGCAAGGATTGTCTGCTTAGAACGCCTAAATACGCGTTGGACGTTACAGGGCCTCCATATTAAGTTGCGATCCTCGTTTCATTCGTTCTTGTCGTTATACGACGTCCATTTCAGGCCTCTATTTAAGCTCACCTAATTCATATGATAGGAGGGGCCGGATGGACCCGAGGTATTGGAAATAAGTTATGGATGGAGCCATCTTTGGAAAAAGTCAGCACATATGCAATTTTAGCTTGGAAAGATTCAGCTCCAGTCAAGGCCTCCTAGAACCTGTCCCGTGATCCACATAGGAGACTGATGGGCCACTGTATTTCAACGCTGAGTCGCATCAAGCAGCGTTTTACCTATGGTTGAGGTGAACGGAATTATTGTTCGACCCGGCTCAACCAAAAACGGGCGTACCCCGTGGGCCTGCTCTCTGGTGGCAGGCTTTCCCGCCGTTAACTATATGGTGGTAACCATTCCTCTATGGAGAGCCTACGTATCTTCCCAACTTATCGGCGGAGTGTGGAAACCATTCCCATAGCAATATGGGAAAAATCCGAAGGGATCAACATATATGAGCGCGTGTGGGGGTTAGAGCCTCCATTGTTCCCTTACTCTTTGCCAGTTGTGAGGGAGCTGCCGTCAAGTTGAGGATGTCGTGCTGTCACTAGAATAAAGATGATGATCTCTGACTATCCAGAGACCCTCCGAAGCTGCATCGATGTGATTCCAGCCGTGGCAGGTTCACATATGTAGTAAAACTCTAATTGTGGCCGCAAGTACTTTAGCGTCAACCTGCTATGCT"
print (complement(text))
