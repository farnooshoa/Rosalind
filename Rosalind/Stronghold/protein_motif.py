'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Protein Motif
Rosalind ID: MPRT
Rosalind #: 016
URL: http://rosalind.info/problems/mprt/
'''
import re
import requests

def fetch_protein_sequence(uniprot_id):
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        fasta_data = response.text
        sequence = ''.join(fasta_data.split('\n')[1:])
        return sequence
    else:
        return None

def find_motif_locations(sequence, motif):
    motif_regex = re.compile(motif)
    matches = []
    # Iterate through the sequence and check for matches at each position
    for i in range(len(sequence) - len(motif) + 1):
        if motif_regex.match(sequence[i:i+len(motif)]):
            matches.append(i + 1)  # Adjusting to 1-based index
    return matches


def main(uniprot_ids):
    motif_pattern = r'N[^P][ST][^P]'
    for uniprot_id in uniprot_ids:
        sequence = fetch_protein_sequence(uniprot_id)
        if sequence:
            locations = find_motif_locations(sequence, motif_pattern)
            if locations:
                print(uniprot_id)
                print(' '.join(map(str, locations)))

# Example usage
uniprot_ids = [
    'A8F2D7',
    'Q8R1Y2',
    'Q2V4D9',
    'B5FPF2',
    'P17404_CHM1_BOVIN',
    'O08537_ESR2_MOUSE',
    'P10761_ZP3_MOUSE',
    'P10643_CO7_HUMAN',
    'P0A4Y7',
    'Q28409',
    'Q9LHF1',
    'P19835_BAL_HUMAN',
    'P04921_GLPC_HUMAN',
    'P00741_FA9_BOVIN',
    'C0Q5J8'
]






main(uniprot_ids)
