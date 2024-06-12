# Structures
Nucleotides = ["A", "C", "G", "T"]
RNA_Nucleotides = ["A", "C", "G", "U"]
DNA_ReverseComplement = {"A":"T", "T":"A", "G":"C", "C":"G"}
# CHeck the sequence to see if it is a DNA string

def ValidateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq
    
 # Counting Nucleotides
def countNucFrequency(seq):
    tmpFreq = { "A":0 , "C":0, "G":0, "T":0}
    for nuc in seq:
        if nuc in tmpFreq:
            tmpFreq[nuc] += 1
        else:
            return False
    return tmpFreq
 