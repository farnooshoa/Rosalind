'''A ROSALIND bioinformatics script to extract sequence information FASTA format data.'''

import urllib
import contextlib

def ReadFASTA(sequence):
    sequences = {}
    with open(sequence, 'r') as file:
        sequence_id = None
        sequence_data = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id:
                    sequences[sequence_id] = ''.join(sequence_data)
                sequence_id = line[1:]
                sequence_data = []
            else:
                sequence_data.append(line)
        if sequence_id:
            sequences[sequence_id] = ''.join(sequence_data)
    return sequences


def ParseFASTA(f):
        '''Extracts the Sequence Name and Nucleotide/Peptide Sequence from the a FASTA format file or website.'''
        fasta_list=[]
        for line in f:

                # If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
                if line[0] == '>':
                        
                        # Using try/except because intially there will be no current DNA strand to append.
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass

                        current_dna = [line.lstrip('>').rstrip('\n'),'']

                # Otherwise, append the current DNA line to the current DNA
                else:
                        current_dna[1] += line.rstrip('\n')
        
        # Append the final DNA strand after reading all the lines.
        fasta_list.append(current_dna)