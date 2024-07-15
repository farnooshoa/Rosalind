'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Enumerating Gene Orders
Rosalind ID: PERM
Rosalind #: 019
URL: http://rosalind.info/problems/perm/
'''
import itertools

def generate_permutations(n):
    # Generate the list of numbers from 1 to n
    numbers = list(range(1, n + 1))
    
    # Generate all permutations of the list of numbers
    permutations = list(itertools.permutations(numbers))
    
    # Print the total number of permutations
    print(len(permutations))
    
    # Print each permutation in the required format
    for perm in permutations:
        print(' '.join(map(str, perm)))

# Example usage
n = 5
generate_permutations(n)
