'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/
'''
s1,s2 = open('rosalind_subs.txt').read().split('\r\n')

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print (i+1)