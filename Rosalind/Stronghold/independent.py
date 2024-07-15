'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Independent Alleles
Rosalind ID: LIA
Rosalind #: 015
URL: http://rosalind.info/problems/lia/
'''
from scipy.stats import binom

def probability_at_least_N_AaBb(k, N):
    # Number of offspring in the k-th generation
    num_offspring = 2**k
    
    # Probability of an offspring being Aa Bb
    p_AaBb = 1/4
    
    # Calculate the cumulative probability P(X < N)
    prob_less_than_N = binom.cdf(N-1, num_offspring, p_AaBb)
    
    # We need P(X >= N), which is 1 - P(X < N)
    prob_at_least_N = 1 - prob_less_than_N
    
    return prob_at_least_N

# Example usage
k = 7
N = 38
result = probability_at_least_N_AaBb(k, N)
print(f"The probability that at least {N} Aa Bb organisms will belong to the {k}-th generation is: {result:.4f}")
