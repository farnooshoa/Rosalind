'''Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

def count_nt(Text):
    return Text.count("A"), Text.count("G"), Text.count("C"), Text.count("T")

Text = "GGGAATAGCTACGGACATCTGACATTCATTGTTGAGTCATTACTCGGTGTTGGGGAGGATACGGACAATCCCCCCGGGTTGATGGGACAAAATGTTCGCAATTGATACGCATAATCTAACAAAGTCCCGCGCTTTTGCCGAGGGTTGTCGACATAGTACCCAATCGTTCTCAAGACGTACACCGGGCTAAGTCTTCAAACATACCATCTCAAAGCGTCGGTCCCTTTATACTAAAGTCAGGGACTTGTCCCACGGTACACCTACAGAGGCAAAAAGGTTTTTCTTGGGGCGACCGGGCTTTATGCCACTCAACACAAATTCGCTCGTTAAGGTTGATCTCAACTAGAACCCGTAAGAAAGGATAGAGCTAGTAATGAGCCCAGTACGGTGAGCAAATGAGTTCCCTGAGGGTTGCTCAGTGTGTATGGCTACGGCGCCGCTATTCCCCTGAATTGAGCTTAGCGCCTCGCTCGGACGCCAAGCCATTACGAAGGCCTATGATGGTTTAATATCCGATGGCAGAAATAAGGGAAAGCTATCTGGACCGACTAACTAAATGTTGTTTAATCGAGCGCTACCAAGGGCGTGCGCAGCTGCAACGCGTCCGCAGTAATGACAGAGCAGTAAATACGCGATCTTACGTGCTGCTGAGCCTAAACTAGTGTCCATTTAATTTAATCCCAGTCATTAATAGGCCCCCAGGAATCACTAGGAATAGGGGCAGCCTTTGAACTAAGGCTACCTAAAGAAAAGTTGCGGCAGTCCTTGTACTCGCAATATAAATGGGGCGGCGATCCACTATATTAAGTACGTAGTACTGAGTCGGAAGTGACGCGCCGGCAGACGTCGGTGAGCGCTATGAAGATGGGACGATATGTGGTATGATATAGAGGAATTGAGTAAGTCGGGGTATGAATAGTCGATTTGGGGAAACGGCTCAACGCCAGCCGGCGTT"
print(count_nt (Text))
print(len(Text))
